#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""三套体系通用的成品体检。

用法:
    python3 check.py <成品.docx>              # 通用检查（字体四槽 + 空行）
    python3 check.py <成品.docx> --kind 01    # 讲义：另查 keep/numPr/配色
    python3 check.py <成品.docx> --kind 02    # 批改：另查红蓝字/五章节
    python3 check.py <成品.docx> --kind 03    # 试卷：另查页边距

退出码 0 = 通过，1 = 不合格。
"""
import sys
import re
import zipfile


def check(path, kind=None):
    zf = zipfile.ZipFile(path)
    xml = zf.read('word/document.xml').decode('utf-8')
    problems = []
    # 模板与成品的标准不同：模板允许靠主题继承字体、允许表格 auto 宽度，
    # 那是作者有意留的；成品才要求四槽写死、表宽固定。
    is_template = '模板' in str(path)

    # ---- 1) 字体四槽（三套体系通用）----
    fonts = re.findall(r'<w:rFonts[^>]*>', xml)
    # 只查"有没有显式设"，不限制字体名：
    # 讲义允许最大标题用黑体，正文用宋体，两者都是合规的。
    # 真正要防的是靠主题继承（缺 w:eastAsia / w:hint）。
    bad = [m for m in fonts
           if 'w:eastAsia="' not in m or 'w:hint="eastAsia"' not in m]

    # 判断字体是否主要靠主题继承（模板就是这种）
    theme_based = False
    try:
        styles = zf.read('word/styles.xml').decode('utf-8')
        defaults = re.search(r'<w:docDefaults>.*?</w:docDefaults>', styles, re.S)
        if defaults and 'Theme=' in defaults.group(0):
            theme_based = True
    except KeyError:
        pass

    if bad and not (is_template and theme_based):
        msg = f'字体四槽不合格 {len(bad)}/{len(fonts)} 处（缺 w:eastAsia 或 w:hint）'
        if theme_based:
            msg += '｜该文档字体主要靠主题继承（w:*Theme），模板属正常，成品必须显式写四槽'
        problems.append(msg)

    # ---- 2) 讲义 ----
    if kind == '01':
        if 'w:keepNext' in xml:
            problems.append('存在 w:keepNext（Word 会显示黑方块标记）')
        if 'w:keepLines' in xml:
            problems.append('存在 w:keepLines')
        if 'w:numPr' in xml:
            problems.append('存在 w:numPr（全文不应有编号/项目符号）')
        for c in ('C00000', '7030A0', '008040', '104B90'):
            if c not in xml.upper():
                problems.append(f'缺少颜色 {c}')

    # ---- 3) 作文批改 ----
    if kind == '02':
        if 'FF0000' not in xml.upper():
            problems.append('没有红字（原文需改处）')
        if '1F4E79' not in xml.upper():
            problems.append('没有蓝色编号〔〕')
        for t in ('一、作文要求', '二、学生作文', '三、修改意见', '四、终稿', '五、参考翻译'):
            if t not in xml:
                problems.append(f'缺章节：{t}')

    # ---- 4) 试卷识别：页边距 ----
    if kind == '03':
        m = re.search(r'<w:pgMar[^>]*>', xml)
        if m:
            # 2.2cm ≈ 1247 twips
            for edge in ('top', 'left', 'bottom', 'right'):
                v = re.search(rf'w:{edge}="(\d+)"', m.group(0))
                if v and abs(int(v.group(1)) - 1247) > 30:
                    problems.append(f'页边距 {edge}={v.group(1)} twips，应为 ~1247（2.2cm）')
        else:
            problems.append('找不到 w:pgMar（未设置页边距）')

    # ---- 4.5) 表格宽度 ----
    # 换算坑：tblW / gridCol 的单位是 twips，1 cm = 567。写成 cm÷2.54×567 会让表只剩一半宽。
    # 模板不查这条：模板里的 auto 是作者有意留的「随内容伸缩」，按成品标准要求固定宽会改掉它原本的行为。
    pg = re.search(r'<w:pgSz[^>]*w:w="(\d+)"', xml)
    mar = re.search(r'<w:pgMar[^>]*>', xml)
    text_w = None
    if pg and mar:
        l = re.search(r'w:left="(\d+)"', mar.group(0))
        r = re.search(r'w:right="(\d+)"', mar.group(0))
        if l and r:
            text_w = int(pg.group(1)) - int(l.group(1)) - int(r.group(1))
    for i, tbl in enumerate([] if is_template else re.findall(r'<w:tbl>.*?</w:tbl>', xml, re.S), 1):
        mw = re.search(r'<w:tblW([^>]*)/>', tbl)
        cols = [int(x) for x in re.findall(r'<w:gridCol[^>]*w:w="(\d+)"', tbl)]
        if not mw:
            problems.append(f'第 {i} 张表没有 w:tblW（宽度未固定）')
            continue
        typ = re.search(r'w:type="(\w+)"', mw.group(1))
        wv = re.search(r'w:w="(\d+)"', mw.group(1))
        if (typ and typ.group(1) != 'dxa') or not wv:
            problems.append(f'第 {i} 张表宽未固定（type={typ.group(1) if typ else "?"}）')
            continue
        tw = int(wv.group(1))
        if cols and abs(tw - sum(cols)) > 20:
            problems.append(f'第 {i} 张表 tblW={tw} 与列宽之和 {sum(cols)} 不一致')
        if text_w and tw < text_w * 0.6:
            problems.append(f'第 {i} 张表只有 {tw / 567:.1f}cm，版心 {text_w / 567:.1f}cm'
                            f'（疑似 twips 换算写错）')

    # ---- 5) 空行统计（必须先剔除表格）----
    body = re.sub(r'<w:tbl>.*?</w:tbl>', '', xml, flags=re.S)
    text = re.sub(r'<[^>]+>', '', body.replace('</w:p>', '\n'))
    lines = text.split('\n')
    empties = sum(1 for l in lines if not l.strip())
    paras = len(re.findall(r'<w:p[ >]', body))

    print(f'文件: {path}')
    print(f'段落数 {paras} ｜ 空段落 {empties} ｜ rFonts {len(fonts)} 处')

    if problems:
        print('❌ 不合格：')
        for p in problems:
            print('   -', p)
        return 1

    print('✅ 全部通过')
    return 0


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    kind = None
    if '--kind' in args:
        i = args.index('--kind')
        if i + 1 >= len(args):
            print('--kind 后面要跟 01 / 02 / 03')
            return 2
        kind = args[i + 1]
        args = args[:i] + args[i + 2:]
    return check(args[0], kind)


if __name__ == '__main__':
    sys.exit(main())
