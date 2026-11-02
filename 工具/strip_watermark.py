#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
docx 去水印工具（页眉/页脚里的水印与 logo 一律清除，页码保留）

用法:
    python3 strip_watermark.py 输入.docx [输出.docx]
    python3 strip_watermark.py 输入.docx --inplace

做的事:
  1. 删除 header/footer/document 中标记为 Watermark 的 w:drawing（含其空的 w:r）
  2. 删除 VML 水印形状（v:shape + v:imagedata 且不含文本框内容的）
  3. 删除只被页眉/页脚引用的 media 图片及其 Relationship（正文图不动）
  4. 自检：全部 XML 可解析、Watermark 残留为 0、r:embed 无悬空引用
注意: 页脚里的「页码文本框」（wps 形状 + PAGE 域）不是水印，保留。
"""
import os
import re
import sys
import zipfile
from lxml import etree

NS = {
    'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'v': 'urn:schemas-microsoft-com:vml',
    'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships',
    'rel': 'http://schemas.openxmlformats.org/package/2006/relationships',
}


def _q(tag):
    p, l = tag.split(':')
    return '{%s}%s' % (NS[p], l)


def strip_xml(data):
    """删除水印图形，返回 (新字节, 删除数量)"""
    root = etree.fromstring(data)
    removed = 0

    # 1) DrawingML 水印：docPr/@name 含 watermark
    for dr in list(root.iter(_q('w:drawing'))):
        names = [(d.get('name') or '') for d in dr.iter(_q('wp:docPr'))]
        if any('watermark' in n.lower() for n in names):
            parent = dr.getparent()
            if parent is None:
                continue
            parent.remove(dr)
            removed += 1
            if parent.tag == _q('w:r') and len(parent) == 0:
                gp = parent.getparent()
                if gp is not None:
                    gp.remove(parent)

    # 2) VML 水印：带 imagedata 且没有文本框内容的 shape
    for sh in list(root.iter(_q('v:shape'))):
        has_img = sh.find('.//' + _q('v:imagedata')) is not None
        has_txt = sh.find('.//' + _q('w:txbxContent')) is not None
        if has_txt:
            continue
        sid = ((sh.get('id') or '') + (sh.get('{urn:schemas-microsoft-com:office:office}spid') or '')).lower()
        if has_img or 'watermark' in sid:
            parent = sh.getparent()
            if parent is not None:
                parent.remove(sh)
                removed += 1

    if not removed:
        return data, 0
    return etree.tostring(root, xml_declaration=True, encoding='UTF-8', standalone=True), removed


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    if not args:
        print(__doc__)
        return 1
    src = args[0]
    inplace = '--inplace' in sys.argv
    dst = args[1] if len(args) > 1 else (src if inplace else src.rsplit('.', 1)[0] + '-无水印.docx')

    zin = zipfile.ZipFile(src)
    infos = zin.infolist()
    parts = {i.filename: zin.read(i.filename) for i in infos}
    order = [i.filename for i in infos]
    zin.close()

    # --- 1. 去水印图形 ---
    total = 0
    for name in list(parts):
        if not name.startswith('word/') or not name.endswith('.xml'):
            continue
        if not ('header' in name or 'footer' in name or name == 'word/document.xml'):
            continue
        new, n = strip_xml(parts[name])
        if n:
            print('  %-28s 移除 %d 处水印' % (name, n))
            parts[name] = new
            total += n
    print('  合计移除 %d 处水印图形' % total)

    # --- 2. 找出只被页眉/页脚引用的 media ---
    media_refs = {}
    for name, data in parts.items():
        if not name.endswith('.rels'):
            continue
        try:
            root = etree.fromstring(data)
        except etree.XMLSyntaxError:
            continue
        for rel in root.iter(_q('rel:Relationship')):
            tgt = rel.get('Target') or ''
            if 'media/' not in tgt:
                continue
            base = os.path.dirname(os.path.dirname(name))
            full = os.path.normpath(os.path.join(base, tgt)).replace('\\', '/')
            media_refs.setdefault(full, set()).add(name)

    drop_media = {f for f, owners in media_refs.items()
                  if f in parts and all(('footer' in o or 'header' in o) for o in owners)}
    for m in sorted(drop_media):
        print('  删除水印图片 %s (%d bytes)' % (m, len(parts[m])))
        del parts[m]

    # --- 3. 清掉指向被删图片的关系条目 ---
    drop_names = {os.path.basename(m) for m in drop_media}
    if drop_names:
        for name in list(parts):
            if not name.endswith('.rels'):
                continue
            t = parts[name].decode('utf-8')
            t2 = t
            for b in drop_names:
                t2 = re.sub(r'<Relationship[^>]*Target="[^"]*%s"[^>]*/>' % re.escape(b), '', t2)
            if t2 != t:
                parts[name] = t2.encode('utf-8')

    # --- 4. 写回（保持原部件顺序） ---
    tmp = dst + '.tmp'
    with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as zout:
        for name in order:
            if name in parts:
                zout.writestr(name, parts[name])
    os.replace(tmp, dst)

    # --- 5. 自检 ---
    z = zipfile.ZipFile(dst)
    names = z.namelist()
    xmls = [n for n in names if n.endswith(('.xml', '.rels'))]
    for n in xmls:
        etree.fromstring(z.read(n))
    left_wm = [n for n in xmls if b'Watermark' in z.read(n)]

    dangling = []
    for n in xmls:
        if n.endswith('.rels'):
            continue
        ids = set(re.findall(rb'r:(?:embed|id|link)="([^"]+)"', z.read(n)))
        if not ids:
            continue
        rels_name = os.path.join(os.path.dirname(n), '_rels', os.path.basename(n) + '.rels').replace('\\', '/')
        have = set()
        if rels_name in names:
            have = set(re.findall(rb'Id="([^"]+)"', z.read(rels_name)))
        miss = ids - have
        if miss:
            dangling.append((n, sorted(miss)))
    z.close()

    print('  自检: XML 部件 %d 个全部可解析 | Watermark 残留 %d | 悬空引用 %d'
          % (len(xmls), len(left_wm), len(dangling)))
    if left_wm or dangling:
        print('  !! 有问题:', left_wm, dangling)
        return 2
    print('  完成 ->', dst)
    return 0


if __name__ == '__main__':
    sys.exit(main())
