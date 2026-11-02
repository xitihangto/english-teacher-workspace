# -*- coding: utf-8 -*-
"""生成练习版：复用《试卷识别版》的内容，套用讲义版式，去掉答案。"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from docx import Document
from docx.shared import Emu, Pt
from docx.oxml.ns import qn
import practice_style as S

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, 'build', 'build_jdfz.py'), encoding='utf-8').read()
start = src.index('# ---------- 卷头 ----------')
end = src.index('# ---------- 参考答案 ----------')
content = src[start:end]

# 卷头换成练习版标题
old_head = """para(doc, '上海市上海交通大学附属中学 2026-2027 学年高三上学期', bold=True, center=True, size=TITLE)
para(doc, '第一次调研测试英语试卷', bold=True, center=True, size=TITLE, after=10)"""
assert old_head in content
content = content.replace(old_head, "para(doc, '交大附中2026-2027学年高三上第一次调研测试英语（练习版）', bold=True, center=True, size=TITLE)")

doc = Document()
s = doc.sections[0]
s.page_width = Emu(7772400)
s.page_height = Emu(10058400)
s.top_margin = Emu(685800)
s.bottom_margin = Emu(685800)
s.left_margin = Emu(731520)
s.right_margin = Emu(731520)
st = doc.styles['Normal']
st.font.name = S.TNR
st.font.size = Pt(10.5)
rF = st.element.get_or_add_rPr().get_or_add_rFonts()
rF.set(qn('w:ascii'), S.TNR)
rF.set(qn('w:hAnsi'), S.TNR)
rF.set(qn('w:eastAsia'), S.SONG)
rF.set(qn('w:hint'), 'eastAsia')

ns = {
    'doc': doc, 'para': S.para, 'blank': S.blank, 'rule': S.rule,
    'box_table': S.box_table, 'one_cell_box': S.one_cell_box,
    'fix_layout': S.fix_layout, 'cell_text': S.cell_text,
    'TITLE': S.TITLE, 'BODY': S.BODY, 'MISS': S.MISS,
}
exec(compile(content, 'practice_content', 'exec'), ns)

out = os.path.join(ROOT, '生成物', '交大附中2026-2027学年高三上第一次调研测试英语（练习版）.docx')
doc.save(out)
print('saved:', out)
