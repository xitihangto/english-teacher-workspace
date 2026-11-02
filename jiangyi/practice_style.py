# -*- coding: utf-8 -*-
"""练习版渲染层：与 build_jdfz.py 的 para/box_table 接口兼容，但套用《标准模式讲义》版式。"""
import re
from docx.shared import Pt, Emu, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SONG, HEI, TNR = '宋体', '黑体', 'Times New Roman'
INK = '104B90'      # 墨绿：标题
BODY = 10.5
TITLE = 14
MISS = 16


def set_run(run, size=BODY, bold=False, italic=False, color=None, hei=False):
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = RGBColor.from_string(color)
    rF = run._element.get_or_add_rPr().get_or_add_rFonts()
    rF.set(qn('w:ascii'), TNR)
    rF.set(qn('w:hAnsi'), TNR)
    rF.set(qn('w:eastAsia'), HEI if hei else SONG)
    rF.set(qn('w:hint'), 'eastAsia')


def _p(doc, before, after, align=None):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = 1.15
    if align == 'center':
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    return p


ROMAN = re.compile(r'^(I|II|III|IV|V|VI|VII)\.\s')


def para(doc, text='', indent=False, bold=False, center=False, size=BODY,
         color=None, before=0, after=0, italic_marks=True):
    if size == TITLE:
        p = _p(doc, 6, 3, 'center')
        set_run(p.add_run(text), 15.0, True, color=INK, hei=True)
        return p
    if center:
        p = _p(doc, 3, 3, 'center')
        set_run(p.add_run(text), 11.5, True, color='000000')
        return p
    if bold and ROMAN.match(text):
        p = _p(doc, 8, 3)
        set_run(p.add_run(text), 13.0, True, color=INK)
        return p
    if bold and (text.startswith('Section') or text.startswith('第II卷')):
        p = _p(doc, 5, 2)
        set_run(p.add_run(text), 11.5, True, color=INK)
        return p
    if bold:
        p = _p(doc, 2, 2)
        set_run(p.add_run(text), 10.5, True, color='000000')
        return p
    p = _p(doc, 2, 3)
    if indent:
        p.paragraph_format.first_line_indent = Pt(21)
    if italic_marks and '*' in text:
        parts = text.split('*')
        for i, seg in enumerate(parts):
            if not seg:
                continue
            set_run(p.add_run(seg), BODY, False, italic=(i % 2 == 1))
    else:
        set_run(p.add_run(text), BODY, False)
    return p


def blank(doc, before=0, after=0):
    p = _p(doc, before, after)
    set_run(p.add_run(''), BODY)
    return p


def rule(doc, before=2, after=6):
    p = _p(doc, before, after)
    set_run(p.add_run(''), BODY)
    pPr = p._p.get_or_add_pPr()
    pBdr = OxmlElement('w:pBdr')
    bottom = OxmlElement('w:bottom')
    bottom.set(qn('w:val'), 'single')
    bottom.set(qn('w:sz'), '6')
    bottom.set(qn('w:space'), '1')
    bottom.set(qn('w:color'), '000000')
    pBdr.append(bottom)
    pPr.insert_element_before(pBdr, 'w:shd', 'w:tabs', 'w:suppressAutoHyphens',
                              'w:kinsoku', 'w:wordWrap', 'w:overflowPunct',
                              'w:topLinePunct', 'w:autoSpaceDE', 'w:autoSpaceDN',
                              'w:bidi', 'w:adjustRightInd', 'w:snapToGrid',
                              'w:spacing', 'w:ind', 'w:contextualSpacing',
                              'w:mirrorIndents', 'w:suppressOverlap', 'w:jc',
                              'w:textDirection', 'w:textAlignment',
                              'w:textboxTightWrap', 'w:outlineLvl', 'w:divId',
                              'w:cnfStyle', 'w:rPr', 'w:sectPr', 'w:pPrChange')
    return p


def clear_cell(cell):
    cell.text = ''
    p = cell.paragraphs[0]
    for r in list(p.runs):
        r._element.getparent().remove(r._element)
    return p


def cell_text(cell, text, bold=False, center=False, size=9.5):
    p = clear_cell(cell)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.line_spacing = 1.15
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run(p.add_run(text), size, bold, color='333333')


def fix_layout(t, widths_cm):
    tblPr = t._tbl.tblPr
    for tag in ('w:tblW', 'w:tblLayout'):
        for el in tblPr.findall(qn(tag)):
            tblPr.remove(el)
    tblW = OxmlElement('w:tblW')
    tblW.set(qn('w:type'), 'dxa')
    tblW.set(qn('w:w'), str(int(sum(widths_cm) * 567)))
    tblPr.insert_element_before(tblW, 'w:jc', 'w:tblCellSpacing', 'w:tblInd',
                                'w:tblBorders', 'w:shd', 'w:tblLayout',
                                'w:tblCellMar', 'w:tblLook', 'w:tblCaption',
                                'w:tblDescription')
    layout = OxmlElement('w:tblLayout')
    layout.set(qn('w:type'), 'fixed')
    tblPr.insert_element_before(layout, 'w:tblCellMar', 'w:tblLook',
                                'w:tblCaption', 'w:tblDescription')
    grid = t._tbl.find(qn('w:tblGrid'))
    if grid is not None:
        for gc in list(grid):
            grid.remove(gc)
        for w in widths_cm:
            gc = OxmlElement('w:gridCol')
            gc.set(qn('w:w'), str(int(w * 567)))
            grid.append(gc)
    for row in t.rows:
        for c, w in enumerate(widths_cm):
            row.cells[c].width = Emu(int(w * 360000))


def box_table(doc, rows, widths=None, center=True):
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell_text(t.cell(r, c), val)
    return t


def one_cell_box(doc, text, width_cm, size, color, before=0, after=0, pad=None):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    cell = t.cell(0, 0)
    tcPr = cell._tc.get_or_add_tcPr()
    borders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right'):
        el = OxmlElement(f'w:{edge}')
        el.set(qn('w:val'), 'single')
        el.set(qn('w:sz'), '8')
        el.set(qn('w:space'), '0')
        el.set(qn('w:color'), '000000')
        borders.append(el)
    tcPr.append(borders)
    p = clear_cell(cell)
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(pad if pad else 18)
    p.paragraph_format.space_after = Pt(pad if pad else 18)
    p.paragraph_format.line_spacing = 1.15
    set_run(p.add_run(text), size, False, color=color)
    fix_layout(t, [width_cm])
    return t
