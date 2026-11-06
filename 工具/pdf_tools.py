#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PDF 四件事：合并 / 转图片 / 抽内嵌图 / Word 转 PDF。

一律通过 ./工具/py 运行（它负责依赖环境），不要直接 python3：

    ./工具/py 工具/pdf_tools.py info     <in.pdf>
    ./工具/py 工具/pdf_tools.py merge    <out.pdf> <in1.pdf> <in2.pdf> ...
    ./工具/py 工具/pdf_tools.py toimg    <in.pdf> <outdir> [--dpi 200] [--pages 1-3]
    ./工具/py 工具/pdf_tools.py extract  <in.pdf> <outdir>
    ./工具/py 工具/pdf_tools.py topdf    <in.docx> [--out out.pdf]

合并 / 转图 / 抽图只用 pymupdf，纯 pip，无外部程序。
topdf 需要 LibreOffice：先找 PATH 里的 soffice，再找 /Applications/LibreOffice.app。
找不到就报错退出（码 2），并打印国内镜像地址——**本脚本不会自己下载或安装 LibreOffice**。

退出码：0 成功 / 2 缺外部程序 / 3 输入有问题 / 4 处理失败
"""
import os
import shutil
import subprocess
import sys

try:
    import pymupdf
except ImportError:  # 老版本只有 fitz 这个名字
    import fitz as pymupdf


SOFFICE_CANDIDATES = [
    "soffice",
    "/Applications/LibreOffice.app/Contents/MacOS/soffice",
    "/usr/bin/soffice",
    "/usr/local/bin/soffice",
    "/opt/homebrew/bin/soffice",
]

MIRROR_HINT = """\
装 LibreOffice（806 MB，本脚本不代劳）：
  Apple 芯片：https://mirrors.tuna.tsinghua.edu.cn/libreoffice/libreoffice/stable/
              进版本目录选 mac/aarch64/LibreOffice_x.y.z_MacOS_aarch64.dmg
  Intel 芯片：同一目录选 mac/x86-64/...
  下载后拖进「应用程序」即可，不需要 brew（brew 走官方源，实测 0.4 MB/s）。
或者更省事：在 Word 里打开该 docx，文件 → 另存为 → PDF，零安装。"""


FONTS_CONF = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts.conf")

# PDF 里出现这些字体名，才说明中文字体真的接上了
CJK_HINT = (
    "simsun", "simhei", "songti", "stsong", "heiti", "sthei", "pingfang",
    "kaiti", "fangsong", "ming", "noto sans cjk", "noto serif cjk",
    "source han", "hiragino", "yuanti", "libian", "baoli", "wawati",
    "xingkai", "yuppy", "hannari", "weibei", "lantinghei",
)


def die(msg, code=3):
    print(f"[pdf] {msg}", file=sys.stderr)
    sys.exit(code)


def soffice_env():
    """macOS 上 LibreOffice 自带的 fontconfig 把配置目录编译死在
    /usr/local/etc/fonts，这个目录默认不存在，于是它读不到任何系统字体
    （中文整段空白）。这时用仓库自带的 fonts.conf 兜底。

    Linux 有 /etc/fonts/fonts.conf，自带完整的中文回退规则，
    千万不要覆盖，否则反而丢了字体替换链。"""
    env = os.environ.copy()
    if env.get("FONTCONFIG_FILE"):
        return env
    if os.path.exists("/etc/fonts/fonts.conf"):
        return env
    if os.path.isfile(FONTS_CONF):
        env["FONTCONFIG_FILE"] = FONTS_CONF
    return env


def warn_if_no_cjk_font(path):
    """转完体检：正文有中文、PDF 里却一个中文字体都没嵌，等于白转。"""
    doc = pymupdf.open(path)
    fonts, text = set(), ""
    for page in doc:
        for f in page.get_fonts(full=True):
            fonts.add(f[3].lower())
        if len(text) < 3000:
            text += page.get_text()
    doc.close()
    has_cjk_text = any("\u4e00" <= ch <= "\u9fff" for ch in text)
    has_cjk_font = any(h in name for name in fonts for h in CJK_HINT)
    if has_cjk_text and not has_cjk_font:
        print(
            "[pdf] 警告：这份 PDF 有中文，但没嵌入任何中文字体，中文会显示为空白。\n"
            f"[pdf] 检查 FONTCONFIG_FILE={FONTS_CONF} 是否可用，"
            "或把宋体/黑体装进 ~/Library/Fonts 后重转。",
            file=sys.stderr,
        )
        return False
    return True


def need_file(path):
    if not os.path.isfile(path):
        die(f"找不到文件：{path}")


def cmd_info(args):
    need_file(args.input)
    doc = pymupdf.open(args.input)
    print(f"页数 {doc.page_count}｜加密 {'是' if doc.is_encrypted else '否'}")
    for i, page in enumerate(doc):
        w, h = page.rect.width, page.rect.height
        imgs = len(page.get_images(full=True))
        print(f"  第 {i + 1} 页 {w:.0f}×{h:.0f}pt  内嵌图 {imgs}")
    doc.close()
    return 0


def cmd_merge(args):
    if len(args.inputs) < 2:
        die("至少给两个输入 PDF")
    for f in args.inputs:
        need_file(f)
    out = pymupdf.open()
    for f in args.inputs:
        src = pymupdf.open(f)
        out.insert_pdf(src)
        src.close()
    os.makedirs(os.path.dirname(os.path.abspath(args.output)) or ".", exist_ok=True)
    out.save(args.output)
    out.close()
    print(f"已合并 {len(args.inputs)} 份 → {args.output}")
    return 0


def parse_pages(spec, total):
    """'1-3' / '2' / '1,4,7' → [0,1,2] / [1] / [0,3,6]"""
    if not spec:
        return list(range(total))
    out = []
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            out.extend(range(int(a) - 1, int(b)))
        elif part:
            out.append(int(part) - 1)
    return [i for i in out if 0 <= i < total]


def cmd_toimg(args):
    need_file(args.input)
    os.makedirs(args.outdir, exist_ok=True)
    doc = pymupdf.open(args.input)
    pages = parse_pages(args.pages, doc.page_count)
    stem = os.path.splitext(os.path.basename(args.input))[0]
    for n, i in enumerate(pages, 1):
        pix = doc[i].get_pixmap(dpi=args.dpi)
        path = os.path.join(args.outdir, f"{stem}-{i + 1:03d}.png")
        pix.save(path)
        print(f"  {path}  {pix.width}×{pix.height}")
    doc.close()
    print(f"共 {len(pages)} 张，DPI {args.dpi}")
    return 0


def cmd_extract(args):
    need_file(args.input)
    os.makedirs(args.outdir, exist_ok=True)
    doc = pymupdf.open(args.input)
    seen, n = set(), 0
    for pno in range(doc.page_count):
        for img in doc[pno].get_images(full=True):
            xref = img[0]
            if xref in seen:
                continue
            seen.add(xref)
            info = doc.extract_image(xref)
            ext = info.get("ext", "png")
            path = os.path.join(args.outdir, f"p{pno + 1:03d}-x{xref}.{ext}")
            with open(path, "wb") as fh:
                fh.write(info["image"])
            n += 1
            print(f"  {path}  {info['width']}×{info['height']}")
    doc.close()
    if n == 0:
        print("没有内嵌位图（纯矢量页面）。要图片请用 toimg 整页渲染。")
    else:
        print(f"共抽出 {n} 张内嵌图")
    return 0


def find_soffice():
    for c in SOFFICE_CANDIDATES:
        p = shutil.which(c) if os.sep not in c else (c if os.path.isfile(c) else None)
        if p:
            return p
    return None


def cmd_topdf(args):
    need_file(args.input)
    if not args.input.lower().endswith((".docx", ".doc")):
        die("topdf 只接 docx / doc")
    exe = find_soffice()
    if not exe:
        print("[pdf] 没找到 LibreOffice（soffice）。\n" + MIRROR_HINT, file=sys.stderr)
        return 2
    outdir = os.path.dirname(os.path.abspath(args.out or args.input)) or "."
    os.makedirs(outdir, exist_ok=True)
    cmd = [exe, "--headless", "--norestore", "--convert-to", "pdf", "--outdir", outdir, args.input]
    r = subprocess.run(cmd, capture_output=True, text=True, env=soffice_env())
    if r.returncode != 0:
        die(f"转换失败：{(r.stderr or r.stdout).strip()[:400]}", 4)
    produced = os.path.join(outdir, os.path.splitext(os.path.basename(args.input))[0] + ".pdf")
    if args.out and os.path.abspath(args.out) != os.path.abspath(produced):
        os.replace(produced, args.out)
        produced = args.out
    ok = warn_if_no_cjk_font(produced)
    print(f"已转出 {produced}" + ("" if ok else "（中文字体缺失，见上方警告）"))
    return 0


def main():
    import argparse
    ap = argparse.ArgumentParser(prog="pdf_tools.py", description="PDF 合并 / 转图 / 抽图 / Word 转 PDF")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("info", help="看页数与内嵌图数量")
    p.add_argument("input")
    p.set_defaults(func=cmd_info)

    p = sub.add_parser("merge", help="按顺序合并多个 PDF")
    p.add_argument("output")
    p.add_argument("inputs", nargs="+")
    p.set_defaults(func=cmd_merge)

    p = sub.add_parser("toimg", help="逐页渲染成 PNG")
    p.add_argument("input")
    p.add_argument("outdir")
    p.add_argument("--dpi", type=int, default=200)
    p.add_argument("--pages", default="", help="如 1-3 或 1,4,7，默认全部")
    p.set_defaults(func=cmd_toimg)

    p = sub.add_parser("extract", help="抽内嵌位图（不渲染）")
    p.add_argument("input")
    p.add_argument("outdir")
    p.set_defaults(func=cmd_extract)

    p = sub.add_parser("topdf", help="docx → pdf（需 LibreOffice）")
    p.add_argument("input")
    p.add_argument("--out", default="")
    p.set_defaults(func=cmd_topdf)

    args = ap.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
