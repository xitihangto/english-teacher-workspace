# -*- coding: utf-8 -*-
"""生成《上海市上海交通大学附属中学 2026-2027 学年高三上学期第一次调研测试英语试卷》Word 版。"""
import copy
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

SONG, TNR = '宋体', 'Times New Roman'
BODY = 10.5
TITLE = 14
MISS = 16


def set_run(run, size=BODY, bold=False, italic=False, color=None):
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = RGBColor.from_string(color)
    rPr = run._element.get_or_add_rPr()
    rF = rPr.get_or_add_rFonts()
    rF.set(qn('w:ascii'), TNR)
    rF.set(qn('w:hAnsi'), TNR)
    rF.set(qn('w:eastAsia'), SONG)
    rF.set(qn('w:hint'), 'eastAsia')


def para(doc, text='', indent=False, bold=False, center=False, size=BODY,
         color=None, before=0, after=0, italic_marks=True):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = 1.0
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    if indent:
        ind = p._p.get_or_add_pPr().get_or_add_ind()
        ind.set(qn('w:firstLineChars'), '200')
        ind.set(qn('w:firstLine'), '420')
    # *...* 包起来的走斜体
    if italic_marks and '*' in text:
        parts = text.split('*')
        for i, seg in enumerate(parts):
            if not seg:
                continue
            set_run(p.add_run(seg), size, bold, italic=(i % 2 == 1), color=color)
    else:
        set_run(p.add_run(text), size, bold, color=color)
    return p


def blank(doc, before=0, after=0):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(before)
    p.paragraph_format.space_after = Pt(after)
    p.paragraph_format.line_spacing = 1.0
    set_run(p.add_run(''), BODY)
    return p


def rule(doc, before=2, after=6):
    """整行下边线，模拟答题横线。"""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
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


def cell_text(cell, text, bold=False, center=False, size=BODY):
    p = clear_cell(cell)
    p.paragraph_format.space_before = Pt(1)
    p.paragraph_format.space_after = Pt(1)
    p.paragraph_format.line_spacing = 1.0
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_run(p.add_run(text), size, bold)


def fix_layout(t, widths_cm):
    """固定列宽 + 表宽，避免 Word 自动重算。"""
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
            row.cells[c].width = Cm(w)


def box_table(doc, rows, widths=None, center=True):
    t = doc.add_table(rows=len(rows), cols=len(rows[0]))
    t.style = 'Table Grid'
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            cell_text(t.cell(r, c), val)
    if widths:
        for r in range(len(rows)):
            for c, w in enumerate(widths):
                t.cell(r, c).width = Cm(w)
    return t


def one_cell_box(doc, text, width_cm, size, color, before=0, after=0, pad=None):
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    cell = t.cell(0, 0)
    cell.width = Cm(width_cm)
    # 黑框 0.5pt
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
    p.paragraph_format.line_spacing = 1.0
    set_run(p.add_run(text), size, False, color=color)
    fix_layout(t, [width_cm])
    return t


doc = Document()

# ---------- 页面设置 ----------
sec = doc.sections[0]
sec.page_width = Cm(21.0)
sec.page_height = Cm(29.7)
sec.top_margin = Cm(2.2)
sec.bottom_margin = Cm(2.2)
sec.left_margin = Cm(2.2)
sec.right_margin = Cm(2.2)
sec.gutter = Cm(0)

# Normal 样式也写死四槽，避免主题继承
st = doc.styles['Normal']
st.font.name = TNR
st.font.size = Pt(BODY)
rF = st.element.get_or_add_rPr().get_or_add_rFonts()
rF.set(qn('w:ascii'), TNR)
rF.set(qn('w:hAnsi'), TNR)
rF.set(qn('w:eastAsia'), SONG)
rF.set(qn('w:hint'), 'eastAsia')

# ---------- 卷头 ----------
para(doc, '上海市上海交通大学附属中学 2026-2027 学年高三上学期', bold=True, center=True, size=TITLE)
para(doc, '第一次调研测试英语试卷', bold=True, center=True, size=TITLE, after=10)

# ---------- 缺页占位 ----------
one_cell_box(doc, '此处可能缺页', 13.3, MISS, '0000FF')
blank(doc, before=6)

# ---------- II ----------
para(doc, 'II. Grammar and Vocabulary', bold=True)
para(doc, 'Section B  选词填空', bold=True, after=6)
para(doc, '(A)', bold=True, center=True, after=4)
para(doc, 'Directions: Fill in each blank with the correct word from the box. Each word can be used only once. Note that there are two more words than you need.', after=6)
fix_layout(box_table(doc, [['A. carries', 'B. experienced', 'C. implies', 'D. involved', 'E. integrating', 'F. longing'],
                ['G. overwhelmed', 'H. perspective', 'I. release', 'J. touching', 'K. throwing', '']],
          widths=[2.75] * 6), [2.75] * 6)
blank(doc, before=4)
para(doc, 'A recipe for peace', bold=True, center=True, after=4)
para(doc, 'French filmmaker Francois Truffaut once claimed most war films glorify violence. To break this paradox, Chinese director Wen Muye presents a unique anti-war ___1___ through ordinary food and humanity in his new blockbuster *Once Upon a Time in the Middle East*.', indent=True)
para(doc, 'Starring famous actor Shen Teng, the film has achieved remarkable success since its ___2___. It has grossed over 1.6 billion yuan and dominated China\u2019s daily box office for 14 straight days, earning an impressive 8.6 rating on Douban. Audiences speak highly of its nuanced description of human nature in wars and profound reflection on people\u2019s ___3___ for peace.', indent=True)
para(doc, 'Different from traditional domestic war works, the film creatively combines overseas warfare with Chinese cuisine. It centers on Xu Fu, a(n) ___4___ chef who works in a Middle East restaurant to pay off debts. For Chinese people, food is never merely to relieve hunger. It ___5___ family memories, cultural traditions and sincere blessings, symbols deeply rooted in Chinese culture.', indent=True)
para(doc, 'Peaceful daily life soon collapses as war breaks out, ___6___ the country into chaos. Trapped in gunfire and ruins, Xu and his friend get ___7___ in dangerous crises and bond with war orphans suffering from extremist forces\u2019 brainwashing.', indent=True)
para(doc, 'Throughout the chaotic war scenes, food always serves as a symbol of reunion, harmony and connection. The director explains that Chinese dining culture ___8___ stopping conflicts and embracing peace. The warm custom of sharing meals reflects ordinary people\u2019s humble wish for safety and reunion amid turbulence.', indent=True)
para(doc, 'Devoted to authentic creation, the crew made great efforts in scene setting and food design. By ___9___ northeastern Chinese cooking skills with local foreign styles, the film vividly shows cultural integration. Ultimately, it conveys a(n) ___10___ core message: in chaotic times, the simple wish of \u201ceating well\u201d represents the deepest love and sincere hope for surviving hardships and returning home safely.', indent=True)

blank(doc, before=8)
para(doc, '(B)', bold=True, center=True, after=4)
para(doc, 'Directions: Fill in each blank with the correct word from the box. Each word can be used only once. Note that there are one more words than you need.', after=6)
fix_layout(box_table(doc, [['A. appreciation', 'B. boast', 'C. bridge', 'D. creativity', 'E. crosses', 'F. cutting-edge'],
                ['G. exposing', 'H. houses', 'I. knowledge-focused', 'J. updated', 'K. waking', '']],
          widths=[2.75] * 6), [2.75] * 6)
blank(doc, before=4)
para(doc, 'Night reveals beauty of Longmen Grottoes', bold=True, center=True, after=4)
para(doc, 'As darkness descends over the Yi River, the stone carvings of the Longmen Grottoes, a UNESCO World Heritage Site in Luoyang, Henan province, begin glowing softly in hidden-lamp light, as if ___11___ to life.', indent=True)
para(doc, 'Among its numerous wonders, Fengxian Temple stands out, with nine giant Buddhist-deity statues dominating a cliff face. The carvings ___12___ staggering scale and strikingly lifelike facial expressions. UNESCO states that the extraordinary stone carvings perfectly reflect the high cultural level and sophisticated society of Tang-Dynasty China. The grand Vairocana Buddha gazes across the river, having endured nearly 1,300 years of wind, rain and historical changes.', indent=True)
para(doc, 'For night-tour visitors, the route resembles a slowly unfurling scroll painting. Niches (\u58c1\u9f9b) carved 1,500 years ago receive subtle lighting, ___13___ delicate ancient chisel (\u51ff\u523b) marks. A tour guide comments that night-time sightseeing brings visitors spiritual resonance for people of all nationalities share a common ___14___ for such timeless beauty.', indent=True)
para(doc, 'Longmen Grottoes launched night tours in 2007 and has repeatedly ___15___ facilities. China\u2019s 240-hour visa-free transit policy brought a sharp rise in overseas tourists, turning Luoyang into an unmistakable travel destination. To ___16___ cultural gaps, the site has built a professional multilingual-guide team, and night tours have become its major attraction.', indent=True)
para(doc, 'Spanning 400 years of creation, Longmen Grottoes ___17___ over 100,000 Buddhist statues within 2,345 caves and niches. UNESCO regards these sculptures as an outstanding manifestation of human artistic ___18___, showing the perfection of a mature art form that greatly influenced Asian cultural evolution. Its sculptural charm ___19___ borders and strikes a chord with audiences from diverse cultural backgrounds.', indent=True)
para(doc, 'On global social-media platforms, overseas creators share videos of the hand-carved grottoes. Many tourists arrange full-experience trips: viewing relics in daylight before enjoying night scenes; some wear hanfu to immerse themselves in Tang-style atmospheres. Nowadays, more visitors favour ___20___ immersive cultural travel rather than simple photo-taking. When night falls, lit stone figures keep their silent vigil, with the Yi River reflecting flickering lights.', indent=True)

# ---------- III ----------
blank(doc, before=10)
para(doc, 'III. Reading Comprehension', bold=True)
para(doc, 'Section A  完形填空', bold=True, after=6)
para(doc, 'Directions: For each blank in the following passage there are four words or phrases marked A, B, C and D. Fill in each blank with the word or phrase that best fits the context.', after=6)
para(doc, 'Why Saying \u201cLate Bloomer\u201d Is Wrong', bold=True, center=True, after=4)
para(doc, 'Doree Shafrir considers herself to be a late bloomer. She got married at 38, had her first child at 41, and generally sees herself as having been late \u201cto finding the kind of work I ___21___ like to do.\u201d While the road has not always been smooth, the Los Angeles-based author, 44, now feels gratitude for her journey, along with a new outlook on the ___22___ that she once felt she was missing. \u201cThese goals are relatively arbitrary (\u6b66\u65ad\u7684) and culturally prescribed,\u201d Shafrir says. \u201cI now see that the things I saw as \u2018mistakes\u2019 were just another part of my story.\u201d', indent=True)
para(doc, 'Shafrir views her memoir, *Thanks for Waiting: The Joy (& Weirdness) of Being a Late Bloomer*, as a \u201cgentle corrective to the idea that we\u2019re supposed to do things on a schedule.\u201d Yet it is a notion that is ___23___. Many of us feel\u2014consciously or otherwise\u2014that our paths should ___24___ a rigid timeline of professional and personal milestones. We may judge ourselves negatively if we hit these milestones \u201clate,\u201d in part because of a societal tendency to ___25___ youthful achievement.', indent=True)
para(doc, 'Yet plenty of people find professional fulfillment, financial prosperity, or rewarding relationships within their own time frames. In fact, research shows that people today are increasingly likely to ___26___ major life events at a later age than previous generations.', indent=True)
para(doc, 'Given that we are living longer, switching ___27___ more often, and seeking more meaning in our work, it makes sense for more people to \u201cbloom\u201d later in life. And as they do, the stigma (\u6c61\u540d) of succeeding at an older age\u2014including the idea that it is more surprising than doing so young\u2014has become an outdated view of age and achievement. The concept of late bloomers can also be toxic to those who do succeed later in life. Such people may ___28___ with feelings of failure, negative self-comparison to others, and even the sense that they have been forgotten.', indent=True)
para(doc, 'Removing the pressure to succeed within a given timeline is good for our mental health. It can also enable the people we currently label \u201clate bloomers\u201d to ___29___ the distinct successes that come with the achievements that are made later in life. Many of these strengths and skills are a direct result of spending more time on self-discovery, learning and even failure. \u201cLate bloomers may have faced ___30___ challenges on their pathway to achievement, leading them then to develop more resilience (\u9002\u5e94\u529b),\u201d says Chia-Jun Tsay, an associate professor at University College London. \u201cSuch people may be more ___31___ to adapt to difficult circumstances.\u201d Beyond increased ___32___, a longer road to success also brings opportunities to discover and cultivate meaningful values and passions that are personally resonant (\u5f15\u8d77\u5171\u9e23\u7684), rather than what society pushes us towards.', indent=True)
para(doc, 'Clearly, we are ___33___ for a shift in how we view achievements in terms of age. We simply can\u2019t afford to maintain a bias that leads to ___34___ a whole band of the population\u2019s untapped (\u672a\u5f00\u53d1\u7684) potential. Shafrir learned this lesson in her own time. However, she hopes that future generations will be ___35___ from the age-related achievement pressure she faced\u2014particularly as a woman.', indent=True)

blank(doc, before=6)
opts = [
    ('21.', 'A. mainly', 'B. broadly', 'C. roughly', 'D. truly'),
    ('22.', 'A. expectations', 'B. rewards', 'C. milestones', 'D. possessions'),
    ('23.', 'A. cold-blooded', 'B. deep-rooted', 'C. far-sighted', 'D. single-minded'),
    ('24.', 'A. fit into', 'B. break into', 'C. account for', 'D. make for'),
    ('25.', 'A. admire', 'B. doubt', 'C. envy', 'D. strike'),
    ('26.', 'A. encounter', 'B. expect', 'C. accomplish', 'D. undertake'),
    ('27.', 'A. routines', 'B. locations', 'C. identities', 'D. careers'),
    ('28.', 'A. interfere', 'B. correspond', 'C. cope', 'D. struggle'),
    ('29.', 'A. obtain', 'B. enjoy', 'C. secure', 'D. witness'),
    ('30.', 'A. additional', 'B. emotional', 'C. intentional', 'D. optional'),
    ('31.', 'A. entitled', 'B. tempted', 'C. prepared', 'D. qualified'),
    ('32.', 'A. accessibility', 'B. flexibility', 'C. productivity', 'D. sensibility'),
    ('33.', 'A. grateful', 'B. renowned', 'C. due', 'D. answerable'),
    ('34.', 'A. comprising', 'B. overlooking', 'C. realizing', 'D. sacrificing'),
    ('35.', 'A. benefited', 'B. drawn', 'C. received', 'D. spared'),
]
for n, a, b, c, d in opts:
    para(doc, f'{n} {a}    {b}    {c}    {d}')

# ---------- III Section B ----------
blank(doc, before=10)
para(doc, 'Section B  阅读理解', bold=True, after=6)
para(doc, 'Directions: Read the following passages. Each passage is followed by several questions or unfinished statements. For each of them there are four choices marked A, B, C and D. Choose the one that fits best according to the information given in the passage.', after=6)
para(doc, '(A)', bold=True, center=True, after=4)
para(doc, 'Rest in the Present', bold=True, center=True, after=4)
para(doc, 'Last summer, I was suffering from too much stress. I had just graduated from a challenging doctoral program and was exhausted from the years of research. My wife and I took a vacation after graduation to celebrate, but the academic intensity had become a habit and my brain couldn\u2019t seem to shut off.', indent=True)
para(doc, 'We vacationed on Mackinac Island in Michigan, where the pace of life slows considerably. Ordinarily, the clip-clop (\u5496\u55d2\u58f0) of horses, the lack of cars and the old shops would have relaxed me, but I could not slow down\u2014I was too tired, and distracted.', indent=True)
para(doc, 'We took a day away from the crowds and sat on the beautiful back lawn of our hotel. I had my phone with me to look at e-mails and then put it down. I needed to relax, but why couldn\u2019t I? My lovely wife sat next to me on a sofa. I had a cool glass of lemonade to enjoy. A breeze stirred up whitecaps (\u767d\u6d6a) on the lake. Yet my shoulders were tense, raised up to my ears, and I could not put them down.', indent=True)
para(doc, 'A dragonfly buzzed around us. Those creatures are special to me because they are a symbol of living in the present: they live most of their lives underwater as larvae (\u5e7c\u866b) and emerge with only months ahead to enjoy a colorful adulthood. This one\u2019s brightly colored wings reminded me of the dragonfly tattooed on my wife\u2019s right ankle. Then, the dragonfly came to rest on a piece of grass in front of me.', indent=True)
para(doc, 'I needed to slow down, I thought, to take inspiration from the persistent wind of life and just relax, if only for a short while. I looked out over the bridge, gazed at the clouds and took a deep breath. Maybe I could slow down. I turned to my wife to tell her about my realization when I felt a touch on my leg. I looked down and saw colorful wings\u2014the dragonfly stopped on my right ankle in the exact position of my wife\u2019s tattoo.', indent=True)
para(doc, 'I could have sworn that dragonfly looked at me and communicated. \u201cIt\u2019s not a matter of relaxing,\u201d it seemed to say. \u201cIt\u2019s a matter of appreciating the now. Life is so fleeting. Be here in the moment and let the future take care of itself.\u201d', indent=True)
para(doc, 'Suddenly, I could appreciate what was here now and let that appreciation guide me into a sense of peace, and I felt my shoulders descend to their normal place. The dragonfly seemed satisfied that its message had been delivered so it sprang off my ankle and flew away. I decided not to tell my wife about the experience because I needed to let it sit for a while so it could sink in.', indent=True)
para(doc, 'Months later, I finally told my wife about it and added that I wanted to get my first and only tattoo\u2014a dragonfly on my right ankle. I have it now, and every time I see it, I take a breath and smile. It says, \u201cJust live in the present.\u201d', indent=True)

blank(doc, before=6)
qa = [
    ('36. Why couldn\u2019t the author relax during the vacation on Mackinac Island?',
     ['A. The noisy clip-clop of horses and old shops disturbed his rest.',
      'B. He was still used to the stress of academic research.',
      'C. He kept checking e-mails on his phone throughout the trip.',
      'D. The strong lake breeze made his shoulders physically tense.']),
    ('37. What did the author notice about the dragonfly before it landed on him?',
     ['A. Its bright wings looked like his wife\u2019s ankle tattoo.',
      'B. It buzzed among the crowds of tourists on the hotel lawn.',
      'C. It had spent most of its life living underwater as larvae.',
      'D. It rested on the lake-side grass to escape the strong lake wind.']),
    ('38. What does the underlined word \u201cfleeting\u201d in Paragraph 6 most probably mean?',
     ['A. Meaningful and truly unforgettable forever.',
      'B. Lasting for a very short period of time.',
      'C. Boring and extremely tiring to experience.',
      'D. Colorful and visually attractive to the eyes.']),
    ('39. What is the main message the author wants to convey through this story?',
     ['A. Hard-working scholars need to escape academic pressure via island vacations.',
      'B. Dragonflies are the perfect symbol for people suffering long-term mental stress.',
      'C. Tattoos serve as the best reminder for people\u2019s important life-changing experiences.',
      'D. We ought to value the present moment rather than worry about the future.']),
]
for q, os_ in qa:
    para(doc, q, after=2)
    for o in os_:
        para(doc, o)

# ---------- (B) ----------
blank(doc, before=10)
para(doc, '(B)', bold=True, center=True, after=4)
para(doc, 'AquaExplorer X1: Your Personal Underwater Drone', bold=True, center=True, after=4)
para(doc, 'Price: 99    Cable length: 18 ft (5.5m) or 8.5 ft (2.6m)    Quantity: 1', after=4)
para(doc, 'Description', bold=True, after=2)
para(doc, 'Explore the depths, effortlessly. The AquaExplorer X1 provides a fully immersive underwater viewing experience for both hobbyists and professionals. Unlike traditional diving gear, this compact drone allows for versatile exploration, including ship hull inspections, underwater photography, and marine life observation.', indent=True)
para(doc, 'Monitor your dive duration with the app and receive real-time alerts when the battery level is low. Wireless connectivity enables live streaming and seamless integration with your smartphone. AquaExplorer X1 offers the best companion for underwater adventures.', indent=True)
para(doc, 'Durable ABS or aluminum alloy cable options are available. See \u201cChoosing Location\u201d for insight on what environment works best for your underwater mission.', indent=True)
para(doc, 'Features', bold=True, before=6, after=2)
for b in ['Up to 4K Ultra HD camera with 150\u00b0wide-angle lens',
          'Built-in 1000-lumen LED lights for dark environments',
          'Up to 2 hours of continuous operation on a single charge',
          'Maximum diving depth of 100 meters',
          'Compatible with both iOS and Android devices',
          'Two powerful motors for stable movement in strong currents',
          'Wireless range of up to 50 meters (line of sight)',
          'Sleek orange or navy blue finish',
          'Built-in GPS for surface positioning']:
    para(doc, '\u2022 ' + b)
para(doc, 'Choosing Location', bold=True, before=6, after=2)
para(doc, 'Deploy AquaExplorer X1 in a location that allows clear visibility and calm currents.', indent=True)
para(doc, '\u2022 Orange finish: Recommended for freshwater lakes and swimming pools.')
para(doc, '\u2022 Navy blue finish: Recommended for deep-sea exploration and marine environments.')
para(doc, 'Installation Guidance', bold=True, before=6, after=2)
para(doc, 'AquaExplorer X1 must be paired with its dedicated app by a registered user. Visit our official support page to download the manual. If needed, detailed video tutorials are available online.', indent=True)

blank(doc, before=6)
qb = [
    ('40. Which of the following is NOT a feature of the AquaExplorer X1?',
     ['A. It has 50-meter line-of-sight wireless range and supports Android.',
      'B. It has motors for strong currents and GPS for underwater positioning.',
      'C. It provides 2-hour runtime and a 4K Ultra-HD wide-angle camera.',
      'D. It is iOS-compatible and equipped with built-in LED lights.']),
    ('41. What can we learn from the passage?',
     ['A. Its two powerful motors guarantee stable movement at its maximum diving depth.',
      'B. The orange model is made for deep-sea exploration and marine environments.',
      'C. Buyers may choose ABS or aluminum alloy cables for their diving location.',
      'D. The dedicated app must be installed and paired before watching tutorials.']),
    ('42. Where can you most probably find this page?',
     ['A. On an e-commerce site where buyers select cable length and quantity.',
      'B. In a printed user manual placed inside the retail box of the AquaExplorer X1.',
      'C. On the official website of the drone manufacturer\u2019s support section.',
      'D. In a consumer tech magazine reviewing the latest underwater drones.']),
]
for q, os_ in qb:
    para(doc, q, after=2)
    for o in os_:
        para(doc, o)

# ---------- (C) ----------
blank(doc, before=10)
para(doc, '(C)', bold=True, center=True, after=4)
para(doc, 'It\u2019s fashionable to talk about ideas as if they were diseases. Some pop songs are infectious, and some products are contagious. To that end, advertisers and song producers have developed a theory of \u201cviral\u201d marketing, which assumes that a great idea is self-distributing, and word of mouth can take a little thing and turn it into a phenomenon. But do ideas and products really go viral?', indent=True)
para(doc, 'Not really. A few years ago, several researchers studied the spread of millions of messages on a social media app. More than 90 percent of the messages didn\u2019t spread at all. A tiny percentage, about 1 percent, was shared more than seven times. But nothing really went fully viral\u2014not even the most popular shared messages. Around 95 percent of the news that people see on the social media app comes directly from its original source.', indent=True)
para(doc, 'In other words, popularity on the Internet is mostly driven, not by a million one-to-one shares, but rather by a handful of one-to-one-million outputs. These are what I call \u201cdark broadcasters\u201d: critical, but often hidden, outputs inside the information chain which are responsible for broadcasting a piece of content to many people at once, a fraction of whom might pass it on.', indent=True)
para(doc, 'The information chain leads to a more reasonable definition of the word \u201cviral.\u201d Popularity is still driven by broadcasts\u2014by publishers, celebrities, and other broadcasters who can reach thousands or even millions of people at once.', indent=True)
para(doc, 'Seeing beyond the viral myth has important implications for media literacy at a time when people are concerned about fake news. As confidence in traditional news outlets has declined, people have moved their trust to peers and social networks. But they must be careful not to mistake popularity for truth. That which would seem to go viral due to its inherent truth or interestingness is typically pushed by broadcasters with hidden motives, because such content seems uplifting.', indent=True)
para(doc, 'It promises small-time writers, photographers, and videographers that a moment\u2019s inspiration can transform into sudden fame. It holds up the Internet as a perfect democracy, where anybody can become a star at a moment\u2019s notice if they make something good enough. But in the end, the viral myth is a dragon-gate-leap tale (a Chinese legend of ordinary people gaining instant fame) hiding the fact that the Internet is still run by powerful giants.', indent=True)

blank(doc, before=6)
qc = [
    ('43. Which of the following statements demonstrates the phenomenon of going viral according to the \u201cviral\u201d marketing theory?',
     ['A. A product recommended by a celebrity becomes known to everyone.',
      'B. A funny video is shared a million times among common netizens.',
      'C. A new theory of marketing impresses and is adopted by a big firm.',
      'D. A groundbreaking idea is well received at an academic conference.']),
    ('44. Which of the following statements about \u201cdark broadcasters\u201d is true?',
     ['A. They are critical of and responsible for the content they broadcast.',
      'B. They are able to convince content receivers to pass on information.',
      'C. They play a vital role in determining what becomes a hit.',
      'D. They compete with traditional broadcasters for online shares.']),
    ('45. What does the author mean by saying \u201cbe careful not to mistake popularity for truth\u201d in paragraph 5?',
     ['A. People should only trust news released by authoritative traditional media.',
      'B. People must not confuse selfish motives with the pursuit of truth.',
      'C. People must be able to tell traditional media from social networks.',
      'D. People must be aware what is popular may not be true or interesting.']),
    ('46. Why is the viral myth difficult to cope with?',
     ['A. Because it gives people false hope of sudden success.',
      'B. Because it helps make the Internet a democratic place.',
      'C. Because it promises the creation of inspirational works.',
      'D. Because it reveals the dominant force on the Internet.']),
]
for q, os_ in qc:
    para(doc, q, after=2)
    for o in os_:
        para(doc, o)

# ---------- Section C ----------
blank(doc, before=10)
para(doc, 'Section C  六选四', bold=True, after=6)
para(doc, 'Directions: Complete the following passage by using the sentences given below. Each sentence can be used only once. Note that there are two more sentences than you need.', after=6)
t = doc.add_table(rows=6, cols=1)
t.style = 'Table Grid'
t.autofit = False
for i, s in enumerate(['A. Yet a summer storm can undo weeks of clear test results.',
                       'B. Designated swimming areas are often the safest choice.',
                       'C. But health authorities regularly issue warnings about pollution in lakes and rivers.',
                       'D. They are at higher risk than adults because they swallow more water while swimming.',
                       'E. Mental benefits outweigh physical risks for some swimmers.',
                       'F. The reality is more complicated, especially for rivers.']):
    cell_text(t.cell(i, 0), s)
fix_layout(t, [16.6])
blank(doc, before=6)
para(doc, 'Open water swimming is booming, but is it bad for your health?', bold=True, center=True, after=4)
para(doc, 'Open-water swimming, also known as wild swimming, has boomed in countries from the UK and the US to Australia in the past decade, fuelled by social media and urban \u201cblue space\u201d campaigns. Studies suggest that spending time in natural water is associated with better mental health. ___47___', indent=True)
para(doc, 'Despite these warnings, rivers, once treated as open sewers, are now increasingly seen as \u2018clean and swimmable\u2019. Paris has invested about \u20ac1.4bn in cleaning up the Seine, building a vast underground basin at Austerlitz that can hold about 50,000 cubic metres of stormwater. London\u2019s Tideway \u201csuper sewer\u201d can store around 1.6 million cubic metres of combined sewage and rainwater before sending it for treatment.', indent=True)
para(doc, '___48___ \u201cAfter heavy rain and storms events, urban rivers typically become microbiologically unsafe for swimming for at least 24 to 72 hours,\u201d says Isabel Soler, a senior lecturer at the University of Sheffield. When there is too much rain, water companies release sewage-polluted water directly into rivers.', indent=True)
para(doc, 'Studies on wild swimming show a consistent pattern: the more contact people have with the water, the higher the risk of gastrointestinal illness, with children facing the greatest danger. ___49___ Leptospirosis, a bacterial disease carried in the urine of rodents and livestock, can cause organ failure and death.', indent=True)
para(doc, 'Many swimmers assume that official tests will capture most of these risks. ___50___ The current approach to monitoring is designed to track longer-term trends, and works best at stable coastal sites. It\u2019s less useful for on-the-spot decisions, because short pollution events can be missed by routine sampling.', indent=True)
para(doc, 'In short, alerts help, but they don\u2019t replace making a personal judgement. The pleasures of wild swimming are best preserved when enthusiasm is matched by caution, timing and local knowledge.', indent=True)

# ---------- IV ----------
blank(doc, before=10)
para(doc, 'IV. Grammar  语法填空', bold=True, after=6)
para(doc, 'Directions: After reading the passage below, fill in the blanks to make the passage coherent and grammatically correct. For the blanks with a given word, fill in each blank with the proper form of the given word; for the other blanks, use one word that best fits each blank.', after=6)
para(doc, 'Standing Out and Fitting In', bold=True, center=True, after=4)
para(doc, 'I have always thought that if you can survive high school, you can survive anything. It is the time in a young person\u2019s life ___51___ they not only are faced with the mounting pressures of school, but also have to deal with their own physical and mental development as they navigate the rocky paths of personal self-discovery.', indent=True)
para(doc, 'It is a difficult time when they want to stand out and show their stuff while hoping to be able to find a place where they can fit in, ___52___ fit in with both their peers and society.', indent=True)
para(doc, 'This problem of \u201cstanding out\u201d and \u201cfitting in\u201d can be especially difficult in China which is, as sociologists call it, a \u201chigh-context\u201d society. In a nutshell, a high-context society is one in which the group ___53___ (favor) over the individual as a result of a great many unwritten social rules and understandings. It is a kind of code that people learn to adopt as they grow up in that culture. A \u201clow-context\u201d society, on the other hand, prioritizes the individual over the group, which encourages people to be specific in their social interactions. This is probably ___54___ why Western societies, most of which are multi-cultural, are known for being plain-spoken.', indent=True)
para(doc, 'Does this mean that Chinese society is too conformist? I don\u2019t think so. Western societies ___55___ (adopt) the word \u201cdiversity\u201d as their motto. This has led to certain individuals and small groups within these respective societies ___56___ (demand) that special rights and social status be conferred upon them, which has gone on to create a significant amount of social chaos. China\u2019s high-context society, however, provides a solid basis wherein individuals can express their personalities while still ___57___ (make) positive contributions to society.', indent=True)
para(doc, 'The Eight Eccentrics were Chinese artists who, in the middle of the Qing dynasty, altered the traditions of ink brush painting through their broad brush strokes and use of bright colours. They were \u201ceccentric\u201d because they were not trained artists who painted in the traditional way. For instance, Jin Nong, one of the most famous painters in the group, was so poor during his childhood that he did not start painting ___58___ he was more than fifty years old. Eccentric though they may have been, Jin and the other seven artists would over time become ___59___ (incorporate) into Chinese culture and would go on to have significant influence over more modern painters such as Qi Baishi.', indent=True)
para(doc, 'Being a little different and \u201cstanding out\u201d \u2014 whether it\u2019s you or someone else \u2014 is not necessarily a bad thing. ___60___ is important is that we tolerate these differences and remember that, in this big country and big world, we all belong and we all \u201cfit in.\u201d', indent=True)

# ---------- V ----------
blank(doc, before=10)
para(doc, 'V. Summary Writing  概要写作', bold=True, after=6)
para(doc, '61. Directions: Read the following passage. Summarize the main idea and the main point(s) of the passage in no more than 60 words. Use your own words as far as possible.', after=6)
para(doc, 'A Wise Way to Make Families Rules', bold=True, center=True, after=4)
para(doc, 'All groups, of whatever size or nature, need standard operating procedures. Without them, groups may very well fall into confusion, chaos and conflict. The functions that rules can serve are indispensable. When it comes to parenting, making rules can make a big difference in our family as well. Actually, the issue is not whether our families need rules. We do need them. The real issue is how to motivate all family members to comply with (\u9075\u5b88) them.', indent=True)
para(doc, 'At some time in our lives we all have felt unmotivated to comply with some rule or policy that we had no voice in making. Denied the opportunity to participate in establishing a rule, most people feel imposed upon and resentful of the new rule. But when people actively participate in setting a rule or making a decision that will affect them, they are more highly motivated to comply with it. We call this the Principle of Participation, and it has proven its effectiveness in families as well.', indent=True)
para(doc, 'When children are given the opportunity to participate in setting rules or making decisions that will affect them, several good things happen. Children feel better about themselves \u2014 having more self-esteem (\u81ea\u5c0a\u5fc3) and self-confidence. Such a good effect is due to their feeling that they have gained more \u201cfate control\u201d over their own lives. They also feel they are equal members of the family with an equal voice in making decisions and establishing rules \u2014 they\u2019re part of a team, not second-class citizens. This means that families that function collaboratively and democratically will have closer and warmer relationships than those in which the adults act as bosses or authorities expecting the children to obey the rules made for them.', indent=True)
para(doc, 'Another important reason for encouraging the full participation of family members in decision making is that it often produces higher-quality solutions to problems. Two heads (or three, or four) are better than one. Shared decisions will be based not only on the knowledge and experience of the adults but also on those of the children. The admonition (\u544a\u8beb) that father knows best should be challenged now.', indent=True)

# ---------- VI ----------
blank(doc, before=10)
para(doc, 'VI. Translation  翻译', bold=True, after=6)
para(doc, 'Directions: Translate the following sentences into English, using the words given in the brackets.', after=6)
para(doc, '62.  \u65e0\u8bba\u673a\u5668\u4eba\u662f\u5728\u5de5\u5382\u3001\u519c\u7530\u3001\u533b\u9662\u8fd8\u662f\u5bb6\u5ead\u4e2d\u5de5\u4f5c\uff0c\u8fd9\u4e00\u539f\u5219\u90fd\u540c\u6837\u9002\u7528\u3002(apply)(\u6c49\u8bd1\u82f1)')
rule(doc)
para(doc, '63.  \u6bcf\u9022\u5468\u672b\u665a\u95f4\uff0c\u5c45\u6c11\u4eec\u5728\u516c\u56ed\u5357\u89d2\u7684\u6e56\u7554\u4f11\u606f\u533a\u5185\u54c1\u8317\u53d9\u65e7\uff0c\u95f2\u8bdd\u5bb6\u5e38\u3002(gather) (\u6c49\u8bd1\u82f1)')
rule(doc)
para(doc, '64.  \u9177\u70ed\u7684\u5c71\u5730\u5bf8\u8349\u4e0d\u751f\uff0c\u800c\u79cd\u6ee1\u8461\u8404\u7684\u5c71\u8c37\u5374\u7eff\u610f\u76ce\u7136\uff0c\u5f62\u6210\u201c\u706b\u201d\u4e0e\u201c\u7eff\u201d\u4ea4\u76f8\u8f89\u6620\u7684\u72ec\u7279\u98ce\u8c8c\u3002(where)(\u6c49\u8bd1\u82f1)')
rule(doc)
para(doc, '65.  \u56de\u671b\u738b\u8679\u4e00\u8def\u8d70\u6765\u7684\u6c42\u5b66\u5f81\u9014\uff0c\u6211\u4eec\u7ec8\u5c06\u660e\u767d\uff0c\u666e\u5a03\u4e0e\u5929\u624d\u7684\u7ec8\u6781\u5dee\u8ddd\uff0c\u4e0e\u5176\u8bf4\u5728\u4e8e\u5148\u5929\u667a\u5546\u7684\u9ad8\u4f4e\uff0c\u4e0d\u5982\u8bf4\u5728\u4e8e\u540e\u5929\u52c7\u6c14\u7684\u6df1\u6d45\u3001\u575a\u5b88\u7684\u957f\u77ed\u548c\u524d\u884c\u7684\u7b03\u5b9a\u3002(so much...as)(\u6c49\u8bd1\u82f1)')
rule(doc)

# ---------- VII ----------
blank(doc, before=10)
para(doc, 'VII. Guided Writing  指导写作', bold=True, after=6)
para(doc, '66. Directions: Write an English composition in 120-150 words according to the instructions given below in Chinese.', after=4)
para(doc, '\u5047\u8bbe\u4f60\u662f\u660e\u542f\u4e2d\u5b66\u9ad8\u4e09\u5b66\u751f\u674e\u534e\u3002\u4f60\u7684\u82f1\u56fd\u7b14\u53cb Mike \u5728\u6700\u8fd1\u7684\u4e00\u5c01\u4fe1\u4e2d\u5411\u4f60\u62b1\u6028\u4ed6\u7684\u5ba4\u53cb\u7ecf\u5e38\u4e0d\u5f81\u5f97\u4ed6\u7684\u540c\u610f\u5c31\u628a\u4ed6\u653e\u5728\u51b0\u7bb1\u91cc\u7684\u98df\u7269\u5403\u6389\u3002\u8bf7\u56de\u4e00\u5c01\u4fe1\uff0c\u5185\u5bb9\u5305\u62ec\uff1a', indent=True)
para(doc, '1. \u4f60\u5bf9\u5982\u4f55\u5904\u7406\u8fd9\u4e2a\u95ee\u9898\u7684\u5efa\u8bae\uff1b')
para(doc, '2. \u4f60\u7684\u7406\u7531\u3002')
blank(doc, before=6)
for _ in range(6):
    rule(doc, before=2, after=14)

# ---------- 参考答案 ----------
blank(doc, before=10)
para(doc, '参考答案', bold=True, center=True, after=6)
answers = [
    '\u3010\u7b54\u6848\u30111. H   2. I   3. F   4. B   5. A   6. K   7. D   8. C   9. E   10. J',
    '\u3010\u7b54\u6848\u301111. K   12. B   13. G   14. A   15. J   16. C   17. H   18. D   19. E   20. I',
    '\u3010\u7b54\u6848\u301121. D   22. C   23. B   24. A   25. A   26. C   27. D   28. D   29. B   30. A   31. C   32. B   33. C   34. B   35. D',
    '\u3010\u7b54\u6848\u301136. B   37. A   38. B   39. D',
    '\u3010\u7b54\u6848\u301140. B   41. C   42. A',
    '\u3010\u7b54\u6848\u301143. B   44. C   45. D   46. A',
    '\u3010\u7b54\u6848\u301147. C   48. A   49. D   50. F',
    '\u3010\u7b54\u6848\u301151. when   52. to   53. is favored   54. the reason   55. have adopted   56. demanding   57. making   58. until   59. incorporated   60. What',
]
for a in answers:
    para(doc, a)
para(doc, '\u3010\u7b54\u6848\u301161. The passage emphasizes the importance of establishing family rules through active participation of all family members, which fosters a sense of self-esteem, self-confidence, and equality among them, leading to a more collaborative and democratic family environment. It also highlights the benefits of collective decision-making in generating higher-quality solutions to family problems.')
para(doc, '\u3010\u7b54\u6848\u301162. Whether robots work in factories, farmlands, hospitals or homes, this principle applies equally.')
para(doc, '\u3010\u7b54\u6848\u301163. Every weekend evening, residents gather in the lakeside rest area at the southern corner of the park to drink tea, reminisce about old times and chat about daily life.')
para(doc, '\u3010\u7b54\u6848\u301164. The scorching mountains are totally barren where not even a blade of grass grows, while the valleys planted with grapes are lush with green, forming a unique landscape where \u201cfire\u201d and \u201cgreen\u201d set each other off beautifully.')
para(doc, '\u3010\u7b54\u6848\u301165. Looking back on Wang Hong\u2019s learning journey along the way, we will finally understand that the ultimate gap between ordinary students and geniuses lies not so much in the level of innate IQ as in the depth of acquired courage, the length of perseverance and the determination to move forward.')
para(doc, '\u3010\u7b54\u6848\u301166. Dear Mike,', after=2)
para(doc, 'I\u2019m sorry to hear that your roommate often eats your food kept in the fridge without asking for your permission. It must be really annoying, so I\u2019m writing to offer some practical suggestions.', indent=True)
para(doc, 'First, I suggest you have a sincere and gentle talk with him. Many people do such things just out of carelessness instead of bad intentions. If you calmly tell him how uncomfortable this makes you feel, he will probably stop doing it. Second, you can label your food with your name and store it in a closed container. The clear mark will remind him to respect your belongings. If he still ignores your words, you can ask your dorm manager for help to solve the conflict properly.', indent=True)
para(doc, 'Good roommate relationships rely on mutual respect. I hope my advice will help you deal with the problem smoothly.', indent=True)
p = para(doc, 'Yours,')
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p = para(doc, 'Li Hua')
p.alignment = WD_ALIGN_PARAGRAPH.RIGHT

out = '/Users/linquin/WorkBuddy AI/EnglishTeacher-Workspace/生成物/交大附中2026-2027学年高三上第一次调研测试英语试卷（识别版）.docx'
doc.save(out)
print('saved:', out)
