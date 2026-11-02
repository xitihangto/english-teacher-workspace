# -*- coding: utf-8 -*-
"""讲义渲染层：把《标准模式讲义》的版式固化成可复用的 Book 类。

用法：
    from jy_builder import Book
    b = Book()
    b.title('…')
    b.h1('II. Grammar and Vocabulary (20分)')
    b.quick('【本节答案速查】 …')
    b.rich([('原文', 'n'), ('答案', 'r'), ('解析', 'g')], indent=True)
    b.save('xxx.docx')

run 类型见 KINDS。颜色三位一体固定：
红 C00000=正确答案 / 紫 7030A0=干扰项 / 绿 008040=解析 / 墨绿 104B90=标题与标签。
"""
from docx import Document
from docx.shared import Pt, Cm, Emu, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

SONG, HEI, TNR = '宋体', '黑体', 'Times New Roman'

# kind: (color, bold, underline, size_pt)
KINDS = {
    'title':   ('104B90', True,  False, 15.0),
    'h1':      ('104B90', True,  False, 13.0),
    'h2':      ('104B90', True,  False, 11.5),
    'pt':      ('000000', True,  False, 11.5),
    'label':   ('104B90', True,  False, 10.0),
    'label20': ('104B90', True,  False, 10.0),
    'b20':     ('000000', True,  False, 10.0),
    'n':       ('000000', False, False, 10.5),
    'b':       ('000000', True,  False, 10.5),
    'r':       ('C00000', True,  True,  10.5),
    'ru':      ('C00000', True,  False, 10.5),
    'r0':      ('C00000', False, False, 10.5),
    'p':       ('7030A0', False, False, 10.5),
    'p19':     ('7030A0', False, False, 9.5),
    'g':       ('008040', False, False, 9.5),
    'gb':      ('008040', True,  False, 9.5),
    't333':    ('333333', False, False, 9.5),
}

# 段前/段后（pt）
SPACING = {
    'title': (6, 3), 'h1': (8, 3), 'h2': (5, 2), 'pt': (3, 3),
    'quick': (4, 3), 'dir': (2, 3), 'n': (2, 3), 'b': (2, 3),
    'label': (1, 1), 'g': (0, 2), 't333': (0, 3),
}


class Book:
    def __init__(self):
        self.doc = Document()
        s = self.doc.sections[0]
        s.page_width = Emu(7772400)      # 8.5in
        s.page_height = Emu(10058400)    # 11in
        s.top_margin = Emu(685800)       # 0.75in
        s.bottom_margin = Emu(685800)
        s.left_margin = Emu(731520)      # 0.8in
        s.right_margin = Emu(731520)
        # Normal 样式写死字体，防止主题继承
        st = self.doc.styles['Normal']
        st.font.name = TNR
        st.font.size = Pt(10.5)
        rF = st.element.get_or_add_rPr().get_or_add_rFonts()
        rF.set(qn('w:ascii'), TNR)
        rF.set(qn('w:hAnsi'), TNR)
        rF.set(qn('w:eastAsia'), SONG)
        rF.set(qn('w:hint'), 'eastAsia')

    # ---------- 底层 ----------
    def _run(self, p, text, kind):
        color, bold, underline, size = KINDS[kind]
        r = p.add_run(text)
        r.font.size = Pt(size)
        r.bold = bold
        r.underline = underline
        r.font.color.rgb = RGBColor.from_string(color)
        rF = r._element.get_or_add_rPr().get_or_add_rFonts()
        rF.set(qn('w:ascii'), TNR)
        rF.set(qn('w:hAnsi'), TNR)
        rF.set(qn('w:eastAsia'), HEI if kind == 'title' else SONG)
        rF.set(qn('w:hint'), 'eastAsia')
        return r

    def rich(self, parts, indent=False, align=None, before=None, after=None,
             line=1.15, kind='n'):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        b, a = SPACING.get(kind, (2, 3))
        pf.space_before = Pt(b if before is None else before)
        pf.space_after = Pt(a if after is None else after)
        pf.line_spacing = line
        if align == 'center':
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        elif align == 'right':
            p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        else:
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        if indent:
            pf.first_line_indent = Pt(21)
        for text, k in parts:
            self._run(p, text, k)
        return p

    # ---------- 快捷方法 ----------
    def title(self, text):
        return self.rich([(text, 'title')], align='center', kind='title')

    def h1(self, text):
        return self.rich([(text, 'h1')], kind='h1')

    def h2(self, text):
        return self.rich([(text, 'h2')], kind='h2')

    def pt(self, text):
        return self.rich([(text, 'pt')], align='center', kind='pt')

    def quick(self, text):
        p = self.doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(4)
        pf.space_after = Pt(3)
        pf.line_spacing = 1.15
        r = self._run(p, text, 'label')
        r.bold = True
        r.font.size = Pt(10.5)
        return p

    def dir(self, text):
        return self.rich([(text, 'n')], kind='dir')

    def p(self, text, indent=False, kind='n'):
        return self.rich([(text, kind)], indent=indent, kind=kind)

    def green(self, text):
        return self.rich([(text, 'g')], kind='g')

    def label(self, text):
        return self.rich([(text, 'label')], kind='label')

    def blank(self, before=0, after=0):
        p = self.doc.add_paragraph()
        p.paragraph_format.space_before = Pt(before)
        p.paragraph_format.space_after = Pt(after)
        p.paragraph_format.line_spacing = 1.15
        self._run(p, '', 'n')
        return p

    def save(self, path):
        self.doc.save(path)
        return path
