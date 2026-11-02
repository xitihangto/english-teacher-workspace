# -*- coding: utf-8 -*-
"""生成答案版：从《备课讲义版》中抽掉阅读原文与词汇框，只留答案、选项与解析。"""
import copy, os, re, sys
from docx import Document
from docx.shared import Pt, Emu
from docx.oxml.ns import qn

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, '生成物', '交大附中2026-2027学年高三上第一次调研测试英语（备课讲义版）.docx')
OUT = os.path.join(ROOT, '生成物', '交大附中2026-2027学年高三上第一次调研测试英语（答案版）.docx')

src = Document(SRC)
out = Document()
s = out.sections[0]
s.page_width = Emu(7772400)
s.page_height = Emu(10058400)
s.top_margin = Emu(685800)
s.bottom_margin = Emu(685800)
s.left_margin = Emu(731520)
s.right_margin = Emu(731520)
st = out.styles['Normal']
st.font.name = 'Times New Roman'
st.font.size = Pt(10.5)
rF = st.element.get_or_add_rPr().get_or_add_rFonts()
rF.set(qn('w:ascii'), 'Times New Roman')
rF.set(qn('w:hAnsi'), 'Times New Roman')
rF.set(qn('w:eastAsia'), '宋体')
rF.set(qn('w:hint'), 'eastAsia')

body = out.element.body
sectPr = body.find(qn('w:sectPr'))


def runs_info(p):
    """返回 (文字, [(颜色, 加粗, 字号), ...])"""
    from docx.text.paragraph import Paragraph
    par = Paragraph(p, src)
    info = []
    for r in par.runs:
        c = r.font.color.rgb if r.font.color and r.font.color.rgb else None
        info.append((str(c) if c else None, bool(r.bold),
                     r.font.size.pt if r.font.size else None))
    return par.text, info


def _keep_reading(p, t):
    """阅读 Section B 白名单：只留题号、选项、解析、速查与居中小标题。"""
    from docx.text.paragraph import Paragraph
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    par = Paragraph(p, src)
    if par.alignment == WD_ALIGN_PARAGRAPH.CENTER:
        return True
    if re.match(r'^\d{2}\.\s', t):
        return True
    if re.match(r'^[A-D]\.\s', t):
        return True
    if t.startswith('【解析定位】') or t.startswith('【本节答案速查】'):
        return True
    if t.startswith('Directions:') or t.startswith('Section B'):
        return True
    return False


region = None
dropped = kept = 0
first_title = True
for child in list(src.element.body.iterchildren()):
    if not child.tag.endswith('}p'):
        continue
    text, info = runs_info(child)
    t = text.strip()

    # 区域切换
    if t.startswith('Section B (30分)'):
        region = 'reading_B'
    elif t.startswith('Section C (10分)'):
        region = 'reading_C'
    elif t.startswith('IV. Grammar'):
        region = 'grammar'
    elif t.startswith('V. Summary'):
        region = 'summary'
    elif t.startswith('VI. Translation'):
        region = 'trans'
    elif t.startswith('VII. Guided Writing'):
        region = 'writing'

    drop = False
    colors = {i[0] for i in info}
    only_plain = bool(info) and all((c in (None, '000000') and not b) for c, b, sz in info)

    if t.startswith('【原始备选词汇框】'):
        drop = True
    elif info and all(c == '333333' for c, b, sz in info):
        drop = True                                   # 备选词框灰字
    elif region == 'reading_B' and not _keep_reading(child, t):
        drop = True                                   # 阅读三篇原文、栏目名与项目符号
    elif region == 'summary' and only_plain:
        drop = True                                   # 概要原文（范文已保留）

    if drop:
        dropped += 1
        continue

    new = copy.deepcopy(child)
    if t.startswith('【卷面说明】'):
        new = copy.deepcopy(child)
        from docx.text.paragraph import Paragraph
        par = Paragraph(new, out)
        for r in par.runs:
            if '本讲义' in r.text:
                r.text = r.text.replace('本讲义', '本答案版')
        body.insert(list(body).index(sectPr), new)
        kept += 1
        continue
    if first_title:
        # 标题改成答案版
        from docx.text.paragraph import Paragraph
        par = Paragraph(new, out)
        if par.runs:
            par.runs[0].text = '交大附中2026-2027学年高三上第一次调研测试英语（答案版）'
            for extra in par.runs[1:]:
                extra.text = ''
        first_title = False
    body.insert(list(body).index(sectPr), new)
    kept += 1

out.save(OUT)
print('saved:', OUT, '| kept', kept, 'dropped', dropped)
