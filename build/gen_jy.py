# -*- coding: utf-8 -*-
"""生成「周中练习八」备课讲义版 docx。
规则来源：规范/01-讲义制作规则.md
"""
import sys
from docx import Document
from docx.shared import Pt, Twips, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

# ---------- 样式表（对应规则 §1 字号与颜色） ----------
S = {
    'title': dict(size=15.0, bold=True,  color='104B90', cn='黑体'),
    'h1':    dict(size=13.0, bold=True,  color='104B90'),
    'h2':    dict(size=11.5, bold=True,  color='104B90'),
    'pt':    dict(size=11.5, bold=True,  color='000000'),
    'l':     dict(size=10.5, bold=True,  color='104B90'),
    'l20':   dict(size=10.0, bold=True,  color='104B90'),
    'n':     dict(size=10.5, bold=False, color='000000'),
    'b':     dict(size=10.5, bold=True,  color='000000'),
    'r':     dict(size=10.5, bold=True,  color='C00000', underline=True),
    'ru':    dict(size=10.5, bold=True,  color='C00000'),
    'p':     dict(size=10.5, bold=False, color='7030A0'),
    'p19':   dict(size=9.5,  bold=False, color='7030A0'),
    'g':     dict(size=9.5,  bold=False, color='008040'),
    'gb':    dict(size=9.5,  bold=True,  color='008040'),
    't333':  dict(size=9.5,  bold=False, color='333333'),
    'b20':   dict(size=10.0, bold=True,  color='000000'),
}


def set_font(run, size=10.5, bold=False, color='000000', underline=False, cn='宋体'):
    """四槽对齐：全角字符走中文（w:hint=eastAsia），半角走英文。"""
    run.font.name = 'Times New Roman'
    rPr = run._element.get_or_add_rPr()
    rF = rPr.get_or_add_rFonts()
    rF.set(qn('w:ascii'), 'Times New Roman')
    rF.set(qn('w:hAnsi'), 'Times New Roman')
    rF.set(qn('w:cs'), 'Times New Roman')
    rF.set(qn('w:eastAsia'), cn)
    rF.set(qn('w:hint'), 'eastAsia')
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.underline = underline
    run.font.color.rgb = RGBColor.from_string(color)
    return run


def P(doc, *runs, indent=False, align=None, before=60, after=20, line=1.15):
    """runs: (text, kind) 或 (text,) 默认 n。indent=True 首行缩进 2 字符。"""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Twips(before)
    pf.space_after = Twips(after)
    pf.line_spacing = line
    if align is not None:
        p.alignment = align
    if indent:
        pPr = p._p.get_or_add_pPr()
        ind = pPr.get_or_add_ind()
        ind.set(qn('w:firstLineChars'), '200')
        ind.set(qn('w:firstLine'), '420')      # 21pt
    for item in runs:
        if isinstance(item, str):
            text, kind = item, 'n'
        else:
            text, kind = item[0], item[1]
        st = S[kind]
        set_font(p.add_run(text), st['size'], st['bold'], st['color'],
                 st.get('underline', False), st.get('cn', '宋体'))
    return p


def new_doc():
    doc = Document()
    # 清掉 python-docx 默认样式残留：Normal 显式写四槽
    st = doc.styles['Normal']
    st.font.name = 'Times New Roman'
    st.font.size = Pt(10.5)
    rPr = st.element.get_or_add_rPr()
    rF = rPr.get_or_add_rFonts()
    rF.set(qn('w:ascii'), 'Times New Roman')
    rF.set(qn('w:hAnsi'), 'Times New Roman')
    rF.set(qn('w:cs'), 'Times New Roman')
    rF.set(qn('w:eastAsia'), '宋体')
    rF.set(qn('w:hint'), 'eastAsia')

    sec = doc.sections[0]
    sec.page_width = Twips(12240)      # Letter 8.5"
    sec.page_height = Twips(15840)     # Letter 11"
    sec.top_margin = Twips(1080)
    sec.bottom_margin = Twips(1080)
    sec.left_margin = Twips(1152)
    sec.right_margin = Twips(1152)
    sec.gutter = Twips(0)
    return doc


def quick(doc, text):
    """【本节答案速查】行"""
    return P(doc, ('【本节答案速查】 ', 'l'), (text, 'ru'), before=60, after=40)


C = WD_ALIGN_PARAGRAPH.CENTER
R = WD_ALIGN_PARAGRAPH.RIGHT
J = WD_ALIGN_PARAGRAPH.JUSTIFY

# ============================================================
doc = new_doc()

P(doc, ('2024届高三英语走向成功 周中练习八（备课讲义版）', 'title'), align=C, before=0, after=120)

# ============================================================
# II. Grammar and Vocabulary
# ============================================================
P(doc, ('II. Grammar and Vocabulary', 'h1'), before=160, after=60)
P(doc, ('Section A', 'h2'), before=80, after=40)
quick(doc, '21. from/through   22. it   23. to taste   24. raised   25. because   26. were harvested   27. whether/if   28. where   29. more bearable   30. can/may/could/might')

P(doc, ('Directions: After reading the passage below, fill in the blanks to make the passage coherent and grammatically correct. For the blanks with a given word, fill in each blank with the proper form of the given word; for the other blanks, use one word that best fits each blank.', 'n'), after=40)

P(doc, ('The Food of Space', 'pt'), align=C, before=80, after=40)

P(doc,
  ('Humans have been living and working on the space station for over 20 years. Their meals are packaged, though sometimes astronauts receive fresh treats (21) ', 'n'),
  ('from/through', 'r'),
  (' 【介词。from/through resupply missions 意为"从补给任务中（获得）"，表示来源或途径；through 强调"经由"，from 强调"来自"，两者均可接受】', 'g'),
  (' resupply missions. The longer that packaged food is stored, the more (22) ', 'n'),
  ('it', 'r'),
  (' 【代词。指代前文不可数名词 packaged food；"the + 比较级, the + 比较级"句式中主语用 it 避免重复，句意为"包装食品存放越久，它可能流失的营养越多"】', 'g'),
  (' may lose nutrients.', 'n'),
  indent=True)

P(doc,
  ('Astronauts have successfully grown 10 different crops on the space station since 2015 and had the chance (23) ', 'n'),
  ('to taste', 'r'),
  (' 【非谓语动词。have the chance to do sth 为固定搭配，动词不定式作后置定语修饰 chance，意为"有机会品尝"】', 'g'),
  (' (taste) each one. The International Space Station hosted a party for astronauts on Friday as they celebrated the harvest of the first chili peppers (24) ', 'n'),
  ('raised', 'r'),
  (' 【非谓语动词。句中已有谓语 hosted，空处用非谓语；peppers 与 raise 之间是被动关系（辣椒被种植），用过去分词 raised 作后置定语，相当于 which were raised in space】', 'g'),
  (' (raise) in space.', 'n'),
  indent=True)

P(doc,
  ('Plant Habitat-04 was one of the most complex plant experiments on the orbiting laboratory (25) ', 'n'),
  ('because', 'r'),
  (' 【连词。前后为因果关系：因为辣椒的生长周期比之前的实验植物长得多，所以它是最复杂的实验之一；用 because 引导原因状语从句，不可用 for（for 表补充说明且不用于句首分句）】', 'g'),
  (' peppers took much longer to grow than the previous experiment plants there. After growing for four months, the peppers (26) ', 'n'),
  ('were harvested', 'r'),
  (' 【时态与语态。时间状语 on Friday 指向过去，主语 peppers 与 harvest 为被动关系，用一般过去时的被动语态；注意 harvest 也可作不及物动词，但此处强调"被采收"，被动更贴切】', 'g'),
  (' (harvest) on Friday. When the vegetables were ready to eat, the astronauts also completed a sensory assessment. They rated the flavor, color, appearance, and taste of the produce to see (27) ', 'n'),
  ('whether/if', 'r'),
  (' 【名词性从句。see 后接宾语从句，句意为"看看他们在绿叶菜上付出的辛劳是否被证明有价值"，用 whether 或 if 引导；whether 更正式，与 or not 连用时只能用 whether】', 'g'),
  (' the labor over their greens proved fruitful as a supplement to prepackaged space food.', 'n'),
  indent=True)

P(doc,
  ('Fresh greens, like peppers, provide a great source of key nutrients, which are essential to human bodies. Fresh greens also have psychological benefits. They can help to keep morale (士气) and provide a sense of normalcy (正常) on missions (28) ', 'n'),
  ('where', 'r'),
  (' 【定语从句。先行词 missions 表示抽象地点，从句 all the conditions are distinctively different from the earth 结构完整、不缺主宾，缺地点状语，故用关系副词 where，相当于 on which】', 'g'),
  (' all the conditions are distinctively different from the earth. Fresh greens make a long-duration mission (29) ', 'n'),
  ('more bearable', 'r'),
  (' 【形容词比较级。与上文的 prepackaged space food 及长期驻留的艰苦形成对照，"让长期任务更易忍受"；bearable 为多音节形容词，比较级加 more】', 'g'),
  (' (bearable) by providing a taste of home.', 'n'),
  indent=True)

P(doc,
  ('Looking to the future, the plant experiments have the potential to significantly impact the sustainability of space exploration. They (30) ', 'n'),
  ('can/may/could/might', 'r'),
  (' 【情态动词。one day 表明是对未来的推测，主语 They 指代 the plant experiments，其后 provide 为动词原形，故填表"可能"的情态动词；can 表客观可能性，may/might/could 表推测，四者均成立】', 'g'),
  (', one day, provide a food source for long-term habitation of Mars and other planets.', 'n'),
  indent=True)

# ---------- Section B 选词填空 ----------
P(doc, ('Section B', 'h2'), before=120, after=40)
quick(doc, '31-35: F G E I J    36-40: A H C K B    [多余项：D. innovate]')

P(doc, ('Directions: Complete the following passage by using the words in the box. Each word can only be used once. Note that there is one word more than you need.', 'n'), after=40)

P(doc, ('【原始备选词汇框】', 'b20'), before=60, after=20)
P(doc, ('A. content    B. overextend    C. develop    D. innovate    E. pursued    F. top', 't333'), after=0)
P(doc, ('G. surface    H. addiction    I. emerge    J. cloud    K. licensed', 't333'), after=40)

P(doc, ('The Trap of Self-care', 'pt'), align=C, before=80, after=40)

P(doc,
  ('On TikTok, "Self-care" has 28.2 billion views, while the hashtag (主题标签) can be found on over 66 million Instagram posts. Also, books about self-care often ', 'n'),
  ('31 F. top 位居……之首', 'r'),
  (' 【动词。top 作及物动词意为"位居……之首、居……第一位"；books about self-care often top many people\'s shopping lists 意为"关于自我关怀的书常常高居许多人的购物清单首位"】', 'g'),
  (' many people\'s shopping lists.', 'n'),
  indent=True)

P(doc,
  ('On the ', 'n'),
  ('32 G. surface 表面', 'r'),
  (' 【名词。on the surface 为固定搭配，意为"表面上、从表面看"，用于引出下文看似合理的说法】', 'g'),
  (', it makes complete sense. Who wouldn\'t like the idea of making oneself feel better and taking care of their mind, body and soul? Yet, we have to be careful not to view self-care as a cure-all solution to our problems. Self-care ', 'n'),
  ('33 E. pursued 被追求的', 'r'),
  (' 【非谓语动词。主句已有谓语 can cause，空处用过去分词 pursued 作后置定语修饰 Self-care，相当于 which is pursued；pursue 意为"追求、践行"】', 'g'),
  (' without awareness of your specific needs and consistent (一致的) evaluation can cause emotional, financial, mental and physical consequences.', 'n'),
  indent=True)

P(doc, ('【就近选项参考池】 [F] top (位居……之首) - 对应31空：top many people\'s shopping lists 高居购物清单首位   |   [G] surface (表面) - 对应32空：on the surface 表面上', 'l20'), before=40, after=40)

P(doc,
  ('According to Zishan Khan, a psychologist with Mindpath Health, self-care can lead to a person becoming frustrated when met with a sea of suggestions, which ', 'n'),
  ('34 I. emerge 出现', 'r'),
  (' 【动词。which 引导定语从句指代 a sea of suggestions，emerge 意为"出现、涌现"，emerging everywhere from podcasts to self-help books 即"从播客到自助类书籍随处可见"】', 'g'),
  (' everywhere from podcasts to self-help books. "So, don\'t allow what others suggest to ', 'n'),
  ('35 J. cloud 蒙蔽', 'r'),
  (' 【动词。cloud 本义"使模糊"，引申为"蒙蔽、干扰"；cloud your internal voice 意为"干扰你内心的声音"，与后文"自我关怀须与自身目标价值一致"呼应】', 'g'),
  (' your internal voice," says Khan. "Self-care can only benefit a person if it\'s consistent with their goals and values."', 'n'),
  indent=True)

P(doc, ('【就近选项参考池】 [I] emerge (出现/涌现) - 对应34空：which emerge everywhere 到处涌现   |   [J] cloud (蒙蔽/干扰) - 对应35空：cloud your internal voice 蒙蔽你内心的声音', 'l20'), before=40, after=40)

P(doc,
  ('Khan further emphasizes the danger of uncontrolled physically-centered self-care advice, such as from influencers. "Their ', 'n'),
  ('36 A. content 内容', 'r'),
  (' 【名词。their 指代 influencers（网红），content 意为"（发布）内容"；社交媒体语境下 content 是高频词，指博主产出的文字、视频等】', 'g'),
  (' often overly focuses on beauty and improving one\'s looks. This can unintentionally lead to body image concern and thus actually worsen one\'s mental health," she says.', 'n'),
  indent=True)

P(doc,
  ('Another danger can come when self-care actions reach the level of ', 'n'),
  ('37 H. addiction 成瘾', 'r'),
  (' 【名词。reach the level of addiction 意为"达到成瘾的程度"；下文 spend a large amount of time thinking about or practicing 正是成瘾的典型表现】', 'g'),
  (', says Melissa Boudin, a psychologist of Choosing Therapy. "When you spend a large amount of time thinking about or practicing a certain self-care behavior, this may be that self-care has gone from beneficial to harmful," she says, using the example of self-care through healthy eating and then going so far as to ', 'n'),
  ('38 C. develop 患上', 'r'),
  (' 【动词。develop 除"发展"外，还可表示"患上（疾病）、养成（习惯）"；develop an eating disorder 意为"患上进食障碍"，是 go so far as to do 的宾语】', 'g'),
  (' an eating disorder.', 'n'),
  indent=True)

P(doc, ('【就近选项参考池】 [A] content (内容) - 对应36空：Their content often overly focuses on beauty 她们的内容常过度关注美貌   |   [H] addiction (成瘾) - 对应37空：reach the level of addiction 达到成瘾程度   |   [C] develop (患上/养成) - 对应38空：develop an eating disorder 患上进食障碍', 'l20'), before=40, after=40)

P(doc,
  ('Lena Suarez-Angelino, a(n) ', 'n'),
  ('39 K. licensed 持证的', 'r'),
  (' 【形容词。licensed 意为"持有执照的、有执业资格的"，licensed clinical social worker 即"持证临床社工"，是对从业者资质的限定说明】', 'g'),
  (' clinical social worker, has recommended creating a list of activities that make you feel better but don\'t ', 'n'),
  ('40 B. overextend 使过度消耗', 'r'),
  (' 【动词。overextend 意为"使过度消耗、使力不从心"；but 前后构成对比——让自己感觉更好，但不至于透支自己，呼应末句 it should not be overdone】', 'g'),
  (' you. Worthwhile and beneficial self-care may include anything from time with loved ones to walking. While self-care is important, it should not be overdone.', 'n'),
  indent=True)

P(doc, ('【就近选项参考池】 [K] licensed (持证的) - 对应39空：a licensed clinical social worker 持证临床社工   |   [B] overextend (使过度消耗) - 对应40空：activities that don\'t overextend you 不会让你透支的活动   ｜  多余未选干扰项：[D] innovate (创新)', 'l20'), before=40, after=40)

# ============================================================
# III. Reading Comprehension
# ============================================================
P(doc, ('III. Reading Comprehension', 'h1'), before=200, after=60)
P(doc, ('Section A  完形填空', 'h2'), before=80, after=40)
quick(doc, '41-45: B B D A C    46-50: B D A C B    51-55: D A D C A')

P(doc, ('Directions: For each blank in the following passage there are four words or phrases marked A, B, C and D. Fill in each blank with the word or phrase that best fits the context.', 'n'), after=40)

P(doc, ('What Determines How Much We Eat', 'pt'), align=C, before=80, after=40)


def cloze_q(num, opts, ans, analysis, before=50):
    """一空一组：题干句已单独成段，此处输出选项行 + 思路精析。"""
    runs = [('【第 %d 题】 ' % num, 'b')]
    for letter, text, cn in opts:
        hit = (letter == ans)
        runs.append(('%s. %s (%s)%s    ' % (letter, text, cn, ' ★' if hit else ''),
                     'ru' if hit else 'p'))
    P(doc, *runs, before=before, after=20)
    P(doc, ('思路精析：' + analysis, 'g'), after=50)


# ---- 第 1 段 ----
P(doc, ('What will you do when you are hungry? Of course, anyone would go and grab something to eat. And then, what determines the ', 'n'),
  ('41 B. amount', 'r'),
  (' of food you take in? You may not be right if your answer is the degree of hunger. The conventional concept that ', 'n'),
  ('42 B. hunger', 'r'),
  (' is the key factor is open to challenge. In recent years, a growing body of research has shown that our appetite and food intake (摄入) are influenced by a large number of factors besides our ', 'n'),
  ('43 D. biological', 'r'),
  (' need for energy. Some of the factors include our eating ', 'n'),
  ('44 A. environment', 'r'),
  (' and our perception of the food in front of us.', 'n'),
  indent=True)

cloze_q(41, [('A', 'quality', '质量'), ('B', 'amount', '数量'), ('C', 'nutrient', '营养物'), ('D', 'variety', '种类')], 'B',
        '空格后的 of food you take in 说明此处问的是"吃进去多少"，即数量；下句 you may not be right if your answer is the degree of hunger 讨论的正是"量由什么决定"，与 amount 直接对应。quality（质量）、nutrient（营养物）、variety（种类）均无法与 degree of hunger 形成对照。')

cloze_q(42, [('A', 'deliciousness', '美味'), ('B', 'hunger', '饥饿'), ('C', 'nutrition', '营养'), ('D', 'flavor', '味道')], 'B',
        '上句刚提到 the degree of hunger，本句 the conventional concept that ___ is the key factor 是承接该说法的复指，故填 hunger。且下文 besides our biological need for energy 也指向"饥饿＝能量需求"这一传统认知，随后被作者质疑。')

cloze_q(43, [('A', 'occasional', '偶尔的'), ('B', 'potential', '潜在的'), ('C', 'external', '外部的'), ('D', 'biological', '生理的')], 'D',
        'besides our ___ need for energy 中，need for energy 属于身体层面的生理需求，biological 意为"生理的、生物的"，与后文 external factors（进食环境、视觉线索）形成"内在生理 vs 外在环境"的对照。')

cloze_q(44, [('A', 'environment', '环境'), ('B', 'content', '内容'), ('C', 'time', '时间'), ('D', 'ability', '能力')], 'A',
        '本句列举影响因素，eating ___ 与 our perception of the food 并列；下一段立刻以 plate size and lighting（盘子大小、灯光）举例，这些都属于进食"环境"，故填 environment。')

# ---- 第 2 段 ----
P(doc, ('Studies have shown that ', 'n'),
  ('45 C. unfocused', 'r'),
  (' eating, for instance, eating while watching TV, or a similar distraction, can increase both hunger and food consumption. Even simple ', 'n'),
  ('46 B. visual', 'r'),
  (' clues, like plate size and lighting, have been shown to affect consumption.', 'n'),
  indent=True)

cloze_q(45, [('A', 'habitual', '习惯性的'), ('B', 'purposeful', '有目的的'), ('C', 'unfocused', '无意识的/不专注的'), ('D', 'absorbed', '全神贯注的')], 'C',
        '空后 for instance, eating while watching TV 是对该词的解释——边看电视边吃，注意力不在食物上；且破折号后 a similar distraction（类似的干扰）进一步印证，故选 unfocused（不专注的）。absorbed 意为"全神贯注"，与"分心"恰好相反。')

cloze_q(46, [('A', 'optional', '可选的'), ('B', 'visual', '视觉的'), ('C', 'hidden', '隐藏的'), ('D', 'flexible', '灵活的')], 'B',
        'plate size and lighting（盘子大小、灯光）都是眼睛能看到的信息，属于"视觉线索"，故选 visual。与上一句"注意力分散"形成递进：不只是分心，连视觉上的暗示都会影响进食量。')

# ---- 第 3 段 ----
P(doc, ('A new study suggested that our short-term ', 'n'),
  ('47 D. memory', 'r'),
  (' also may play a role in appetite. Several hours after a meal, people\'s hunger levels were predicted not by how much they\'d eaten but rather by how much food they\'d seen in front of them — ', 'n'),
  ('48 A. in other words', 'r'),
  (', how much they remembered eating.', 'n'),
  indent=True)

cloze_q(47, [('A', 'vacancy', '空缺'), ('B', 'hunger', '饥饿'), ('C', 'supply', '供给'), ('D', 'memory', '记忆')], 'D',
        '破折号后 how much they remembered eating（他们记得自己吃了多少）直接解释了空处所指，remembered 与 memory 同源；且下文 the recall of our previous meal 再次复现"回忆"这一概念，故选 memory。')

cloze_q(48, [('A', 'in other words', '换言之'), ('B', 'as a whole', '总体上'), ('C', 'by all means', '务必'), ('D', 'all in all', '总之')], 'A',
        '破折号后 how much they remembered eating 是对前半句 how much food they\'d seen in front of them 的换一种说法，二者是解释关系而非总结或递进，故选 in other words。')

# ---- 第 4 段 ----
P(doc, ('This difference suggests that the recall of our previous meal may have a bigger influence on our ', 'n'),
  ('49 C. appetite', 'r'),
  (' than the actual size of the meal, says Jeffrey M. Brunstrom, a professor of experimental psychology at the University of Bristol.', 'n'),
  indent=True)

cloze_q(49, [('A', 'motive', '动机'), ('B', 'growth', '成长'), ('C', 'appetite', '食欲'), ('D', 'health', '健康')], 'C',
        '本段讨论的是"吃了多少"与"记得吃了多少"哪一个对饥饿感影响更大，influence on our ___ 应指食欲；且第三段开头 appetite 已点明讨论对象，此处为同一话题的延续，故选 appetite。')

# ---- 第 5 段 ----
P(doc, ('These findings agree with the earlier research that suggests our perception of food can sometimes ', 'n'),
  ('50 B. trick', 'r'),
  (' our body\'s response to the food itself. In a 2011 study, for instance, people who drank the same 380-calorie milkshake on two ', 'n'),
  ('51 D. separate', 'r'),
  (' occasions produced different levels of hunger-related hormones (荷尔蒙), depending on whether the shake\'s ', 'n'),
  ('52 A. label', 'r'),
  (' said it contained 620 or 140 calories. Moreover, the participants reported feeling ', 'n'),
  ('53 D. fuller', 'r'),
  (' when they thought they\'d consumed a higher-calorie shake.', 'n'),
  indent=True)

cloze_q(50, [('A', 'advocate', '提倡'), ('B', 'trick', '欺骗'), ('C', 'justify', '证明……合理'), ('D', 'enhance', '增强')], 'B',
        '紧接着的 2011 年实验是本句的例证：同样 380 卡的奶昔，只因标签写着 620 卡或 140 卡，受试者的饥饿激素与饱腹感就不同——说明"对食物的认知"能"欺骗"身体的真实反应，故选 trick。enhance（增强）无法解释"同样的食物产生不同反应"这一反差。')

cloze_q(51, [('A', 'identical', '完全相同的'), ('B', 'alternative', '交替的'), ('C', 'dependent', '依赖的'), ('D', 'separate', '不同的/分开的')], 'D',
        'on two ___ occasions 指"在两个不同场合"各喝一次，强调两次实验相互独立，故选 separate。identical occasions 与语境矛盾——正因为是两次不同场合，才可能出现不同结果。')

cloze_q(52, [('A', 'label', '标签'), ('B', 'function', '功能'), ('C', 'usage', '用法'), ('D', 'material', '材料')], 'A',
        'the shake\'s ___ said it contained 620 or 140 calories，能"标示热量"的只能是包装上的"标签"，故选 label。这正是实验中被人为操控的变量。')

cloze_q(53, [('A', 'wiser', '更明智的'), ('B', 'healthier', '更健康的'), ('C', 'happier', '更快乐的'), ('D', 'fuller', '更饱的')], 'D',
        '本段核心是"感知影响生理反应"：受试者以为自己喝的是 620 卡的高热量奶昔，于是报告"感觉更饱"，与上文 hunger-related hormones 的变化方向一致，故选 fuller。')

# ---- 第 6 段 ----
P(doc, ('What does this mean to our eating habits? Although it hardly seems practical to cheat ourselves into eating less, the new findings do highlight the benefit of focusing on our food, avoiding TV and multitasking while eating. The so-called mindful-eating strategies can fight against ', 'n'),
  ('54 C. distraction', 'r'),
  (' while we are eating. By ', 'n'),
  ('55 A. employing', 'r'),
  (' mindful eating techniques, you have the opportunity to change your current eating habits by becoming more self-aware and in tune to your body\'s hunger cues.', 'n'),
  indent=True)

cloze_q(54, [('A', 'distress', '痛苦'), ('B', 'waste', '浪费'), ('C', 'distraction', '分心'), ('D', 'fullness', '饱腹感')], 'C',
        '上文给出的做法是 focusing on our food, avoiding TV and multitasking，即排除干扰、专注进食；mindful-eating 要对抗的正是"分心"，与第二段 a similar distraction 前后呼应，故选 distraction。')

cloze_q(55, [('A', 'employing', '采用'), ('B', 'perceiving', '感知'), ('C', 'clarifying', '澄清'), ('D', 'assuming', '假定')], 'A',
        'By ___ techniques 表示"通过采用某种方法"，介词 by 后接动名词表手段；employ 意为"使用、采用（方法）"，employing mindful eating techniques 即"运用正念饮食技巧"，与后半句"有机会改变现有饮食习惯"构成手段—结果关系。')

# ---------- Section B 阅读理解 ----------
P(doc, ('Section B  阅读理解', 'h2'), before=200, after=40)
quick(doc, 'Passage (A): 56-59 C B D A    Passage (B): 60-62 D B A    Passage (C): 63-66 B C A D')

P(doc, ('Directions: Read the following three passages. Each passage is followed by several questions or unfinished statements. For each of them there are four choices marked A, B, C and D. Choose the one that fits best according to the information given in the passage you have just read.', 'n'), after=40)


def choice_q(num, stem, opts, ans, analysis):
    """选择题：正确项提到最前并标 [正确答案]，其余按原顺序。"""
    P(doc, ('%d. %s' % (num, stem), 'b'), before=80, after=20)
    ordered = [o for o in opts if o[0] == ans] + [o for o in opts if o[0] != ans]
    for letter, text in ordered:
        if letter == ans:
            P(doc, ('%s. %s  [正确答案]' % (letter, text), 'ru'), after=0)
        else:
            P(doc, ('%s. %s' % (letter, text), 'p'), after=0)
    P(doc, ('【解析定位】 ' + analysis, 'g'), before=20, after=60)


# ===== Passage A =====
P(doc, ('(A)', 'pt'), before=100, after=40)

P(doc, ('When I step out onto the deck, I definitely feel the Arctic chill. That\'s not surprising. I\'m a good hundred miles inside the Arctic Circle; in fact, you can\'t get much farther north and still be in Sweden. This is Abisko Mountain Station, perhaps the crown jewel of the Swedish mountain lodges (小屋). I\'m back for a second time to this remote, scenic spot.', 'n'),
  indent=True)

P(doc, ('Last Autumn, a heavy snowstorm trapped me in my tent for days and eventually forced me to go to the station, a comfortable place. ', 'n'),
  ('[56C 首段交代初次到访的原因：暴风雪把我困在帐篷里数日，最终"迫使我"前往该站——即被天气所迫，与 C 项 forced there by the weather 完全对应]', 'gb'),
  (' I discovered a different side to Abisko. People come here for many reasons – some to hike, some to climb, some to cross-country ski. But there\'s yet another entirely different attraction here. Looking out from the deck of the train station, above a huge lake, in the upper sky of the North Pole, the Aurora, as we often refer to the northern light, mixed with green and red, was giving off ghostly light, rolling across the dark night sky.', 'n'),
  indent=True)

P(doc, ('The Aurora may be old hat to those who live this far north, but for the rest of us it is an unforgettable experience. ', 'n'),
  ('[57B old hat 与后半句 for the rest of us it is an unforgettable experience 构成对比：对极北居民而言是"见惯不怪、不足为奇"的寻常事物，故为 familiar and unexciting]', 'gb'),
  (' The lights here were so appealing to us we quickly forgot the discomfort of the cold.', 'n'),
  indent=True)

P(doc, ('One of the attractions in Abisko is the Tornetrask. It\'s a huge lake, which extends more than 70 kilometres long just north of the station, creates an unusual weather phenomenon that keeps the skies above the station clear even when fog or clouds blanket most of northern Sweden. The sky in this area is mostly clear all year around.', 'n'),
  indent=True)

P(doc, ('Abisko has a lot to offer to make it an ideal place to view the Aurora. It is far from any city lights. ', 'n'),
  ('[58D 末段列举的优势是：远离城市灯光（C 项）、山顶观景平台（A 项）、每晚发布极光预报（B 项）。咖啡馆本身不是观极光的条件——它是被"改建成观景平台"之后才成为观景点，D 项偷换了概念，故为 NOT 项]', 'gb'),
  (' The station operates a ski lift to the top of Nuolja Peak, more than 3,000 feet high. For the first time this year, a cafe at the top of the mountain has been turned into a viewing platform for the Northern Lights, called the Aurora Sky Station. Also, the station posts forecasts each night of expected Aurora activity, collected from scientific observations arriving via computer, so visitors may choose the best viewing time.', 'n'),
  indent=True)

choice_q(56, 'What was the reason for the author\'s first visit to the lodge?',
         [('A', 'He went there in search of the Aurora.'), ('B', 'He needed equipment to keep him warm.'),
          ('C', 'He was forced there by the weather.'), ('D', 'He had to make his food supply there.')], 'C',
         '细节理解题。定位第2段首句："a heavy snowstorm trapped me in my tent for days and eventually forced me to go to the station"。forced 一词直接对应 C 项。A 项是第二次到访及后来的收获，非初次原因；B、D 项文中无据。故选 C。')

choice_q(57, 'The phrase "old hat" in 3rd paragraph probably mean "________".',
         [('A', 'severe and struggling'), ('B', 'familiar and unexciting'),
          ('C', 'strange and shocking'), ('D', 'mysterious and adventurous')], 'B',
         '词义猜测题。定位第3段首句："The Aurora may be old hat to those who live this far north, but for the rest of us it is an unforgettable experience." but 前后对比：对极北居民是 old hat，对我们却是难忘体验，可见 old hat 意为"司空见惯、不足为奇"。故选 B。')

choice_q(58, 'According to the last paragraph, which of the following is NOT a factor that makes Abisko an ideal place to view the Aurora?',
         [('A', 'There is a mountain viewing platform.'), ('B', 'Weather forecasts are available.'),
          ('C', 'There are no city lights nearby.'), ('D', 'There is a café shop there.')], 'D',
         '细节理解题（否定型）。末段列出三项优势：far from any city lights（C）、山顶咖啡馆"被改建成"观景平台 Aurora Sky Station（A）、每晚发布极光活动预报（B）。D 项把"咖啡馆"本身当作观极光的因素，而原文说的是改建后的观景平台，属于偷换概念。故选 D。')

choice_q(59, 'The author\'s overall opinion of Abisko is that ________.',
         [('A', 'despite the severe weather, it\'s an impressive place'),
          ('B', 'people have overestimated its popularity'),
          ('C', 'it\'s not as popular as it deserves to be'),
          ('D', 'the cold weather worsens the Aurora viewing experience there')], 'A',
         '推理判断题（作者态度）。全文既写严寒（Arctic chill、暴风雪困住数日、forgot the discomfort of the cold），又反复表达赞叹（crown jewel、unforgettable experience、so appealing），且"第二次到访"本身即为认可。B、C 项文中无据；D 项与"quickly forgot the discomfort"相悖。故选 A。')

# ===== Passage B =====
P(doc, ('(B)', 'pt'), before=120, after=20)
P(doc, ('(You may read the questions first.)', 'n'), after=40)

# 原文为 1×1 表格，按规则用 Table Grid 原样保留
tb = doc.add_table(rows=1, cols=1)
tb.style = 'Table Grid'
tb.alignment = WD_TABLE_ALIGNMENT.CENTER
cell = tb.rows[0].cells[0]
first = True


def cell_p(cell, runs, indent=False, before=20, after=20):
    global first
    if first:
        p = cell.paragraphs[0]
        first = False
    else:
        p = cell.add_paragraph()
    pf = p.paragraph_format
    pf.space_before = Twips(before)
    pf.space_after = Twips(after)
    pf.line_spacing = 1.15
    if indent:
        pPr = p._p.get_or_add_pPr()
        ind = pPr.get_or_add_ind()
        ind.set(qn('w:firstLineChars'), '200')
        ind.set(qn('w:firstLine'), '420')
    for item in runs:
        text, kind = (item, 'n') if isinstance(item, str) else item
        st = S[kind]
        set_font(p.add_run(text), st['size'], st['bold'], st['color'],
                 st.get('underline', False), st.get('cn', '宋体'))


cell_p(cell, [('Four types of learners', 'b')], before=40, after=40)

cell_p(cell, [('Type A Learner', 'b')])
cell_p(cell, [('People in this group adapt observations into complex but logical theories. They think problems through in a logical way. They tend to be perfectionists who won\'t rest easy until everything is reasonable. They like to analyze and are keen on basic principles and theories. They pay great attention to logic, so questions they frequently ask are: "', 'n'),
              ('Does it make sense?', 'r'),
              ('", and "How does this go with that?". ', 'n'),
              ('[60D 首段空白处需填一个与"重视逻辑、凡事要合理"相呼应的问句，与后文"How does this go with that?"构成并列设问]', 'gb'),
              (' They tend to be objective, approaching problems in a consistently logical manner. This is their "mental set" and they reject anything that conflicts with it. They prefer to maximize certainty and feel uncomfortable with subjective judgements.', 'n')],
       indent=True, after=40)

cell_p(cell, [('Type B Learner', 'b')])
cell_p(cell, [('These people are keen on trying out ideas, theories and techniques to see if they work in practice. They positively search out new ideas and take the first opportunity to experiment with applications. They want to try out the new ideas in the courses in practice. They also tend to be impatient with random discussions, and their attention soon begins to wander if they feel they are going round in circles. They are practical, down to earth and like making practical decisions and solving problems. They see problems and opportunities as a challenge, and their philosophy is: "There is always a better way" and "If it works, it\'s good".', 'n')],
       indent=True, after=40)

cell_p(cell, [('Type C Learner', 'b')])
cell_p(cell, [('People in this group involve themselves fully in new experiences. They are open-minded, and this tends to make them enthusiastic about anything new. Their philosophy is: "I\'ll try anything once", so they tend to act first and consider the consequences afterwards. Their days are filled with activities. As soon as the excitement from one activity has died down they are busy looking for the next, as they are only interested in gaining new experiences but are bored with carrying out their plans and they lack perseverance. They constantly involve themselves with others but, in doing so, they seek to center all activities around themselves.', 'n')],
       indent=True, after=40)

cell_p(cell, [('Type D Learner', 'b')])
cell_p(cell, [('They collect data, both first-hand and from others, and prefer to think about it thoroughly before coming to a conclusion. The thorough collection and analysis of data about experiences and events is what counts so they tend to postpone making definitive judgments for as long as possible. Their philosophy is to be cautious. They like to consider all possible angles before making a move, and will be reluctant to become involved in activities that others put forward without having carefully considered the likely outcome.', 'n')],
       indent=True, after=40)

choice_q(60, 'Which of the following can be put into the blank in the first paragraph?',
         [('A', 'Do we need more experiments?'), ('B', 'Do you understand me?'),
          ('C', 'Do you believe the theory?'), ('D', 'Does it make sense?')], 'D',
         '推理判断题。空格位于 Type A Learner 的描述中，该段强调"They think problems through in a logical way""won\'t rest easy until everything is reasonable""pay great attention to logic"，与其并列的另一问句是"How does this go with that?"（这与那如何相容）。两个问句都应体现"合乎逻辑、说得通"的追问，故选 D（这讲得通吗）。')

choice_q(61, 'Suppose John is a person with fresh ideas and willing to check everything out to see what happens. Which type of learner is John?',
         [('A', 'Type A Learner'), ('B', 'Type B Learner'), ('C', 'Type C Learner'), ('D', 'Type D Learner')], 'B',
         '推理判断题（人物匹配）。题干关键词"有新想法 + 愿意把一切试一遍看会发生什么"，对应 Type B 段的"positively search out new ideas and take the first opportunity to experiment with applications""keen on trying out ideas... to see if they work in practice"，故选 B。注意与 Type C 区分：C 型是"先做后想、缺乏毅力"，题干强调"验证是否可行"，属 B 型。')

choice_q(62, 'Which of the following is NOT true about Type D learner?',
         [('A', 'They are keen on making immediate conclusion.'), ('B', 'Their conclusion comes after data analysis.'),
          ('C', 'They outline a possible outcome before taking an activity.'), ('D', 'They prefer not to give out their viewpoints randomly.')], 'A',
         '细节理解题（否定型）。Type D 段明确写道"prefer to think about it thoroughly before coming to a conclusion""tend to postpone making definitive judgments for as long as possible"，即刻意推迟下结论，与 A 项"急于下结论"完全相反，故 A 为 NOT true。B 项对应"collect data... and analyze"；C 项对应"consider all possible angles before making a move"；D 项对应"postpone making definitive judgments"，均属实。')

# ===== Passage C =====
P(doc, ('(C)', 'pt'), before=120, after=40)

P(doc, ('In recent years, a lot of "business thinking" books have been published, all of which search for new answers on how to run organizations effectively. Obliquity tells us that the most profitable companies are not the most aggressive in chasing profits. Wikinomics demonstrates new models of production based on community and collaboration. Peter Miller\'s new book, Smart Swarm, however, challenges leaders to think differently. He studied creatures, like bees and ants and he found their habits, actions and instincts can be applied to business. ', 'n'),
  ('[63B 首段先并列三本"商业思维"著作，再用 however 转出 Smart Swarm 的不同：Miller"研究蜜蜂蚂蚁，发现其习性可应用于商业"，并以"the science behind management theory"作支撑——差别在于用生物学的科学证据支撑管理理论]', 'gb'),
  ('Miller believes his book is the first time anyone has explained the science behind management theory. "The examples of how ant colonies (蚁群) or beehives (蜂窝) work are appealing models for organizations and systems that can be applied in a business context," he says.', 'n'),
  indent=True)

P(doc, ('So how exactly can bees help run organizations? "By the way they work independently before they work together," Miller says. "Picture a huge beehive hanging on a tree, with about 5,000 bees competing for space. They know their population is getting too big, leaving them unsafe. They must all agree to find a new home. In today\'s business environment, managers need to be able to make the right decisions under intense pressure. Yet, it is clear that some of the best-paid leaders in some of the biggest organizations can get it dramatically wrong. How is it that they can fail to make efficient business decisions when a large group of bees can make a critical decision about their hive in just a few seconds?"', 'n'),
  indent=True)

P(doc, ('According to Miller, "swarm theory" can help managers in three simple steps: discover, test and evaluate. The bees first realize they have a problem. They then fly into the neighborhood to find potential new sites. They come back and perform a "dance" to get other bees to follow them. Eventually, the bees with the best dance attract the most votes – and a decision is made. Miller says. "The bee example tells you that you need to seek out diversity in your team. You need to have a way of gathering up quite different ideas so you can make sure you pick the right one."', 'n'),
  indent=True)

P(doc, ('Ants, in addition, can help businesses organize workflow and people. In an ant colony, there is no leader. Ants are self-organized, and respond to their environment and each other. One ant on its own could not raid (袭击) a kitchen cupboard, but one ant telling the next one that it\'s worth following him to find food ends up creating a food chain. "In an ant colony, you get the right number going in and out searching for food, you get the right number taking care of the babies," Miller says. "As a manager, this can tell you that your hierarchy (等级制度) is getting in the way of getting the work done."', 'n'),
  indent=True)

choice_q(63, 'Miller believes his book differs from other "business thinking" books because ________.',
         [('A', 'it focuses on maximizing profits'), ('B', 'it supports the theory with evidence'),
          ('C', 'it corrects faults in similar books'), ('D', 'it justifies the previous theory')], 'B',
         '细节理解题。定位第1段："Miller believes his book is the first time anyone has explained the science behind management theory."并以其对蜂群、蚁群的观察作为例证，说明本书的特色是"用科学证据支撑管理理论"，故选 B。A 项是 Obliquity 的内容；C、D 项文中无据。')

choice_q(64, 'In the second paragraph, the author indicates that the behavior of bees can show managers how to ________.',
         [('A', 'make up for wrongly made decisions'), ('B', 'justify exactly what the real problem is'),
          ('C', 'draw the correct conclusions quickly'), ('D', 'keep the team safe under great pressure')], 'C',
         '推理判断题。第2段核心对比："managers need to be able to make the right decisions under intense pressure"，而"some of the best-paid leaders... can get it dramatically wrong"，反观"a large group of bees can make a critical decision about their hive in just a few seconds"。作者意在说明蜂群能在数秒内作出关键决定，管理者应学习这种"快速得出正确结论"的能力，故选 C。')

choice_q(65, 'According to the "swarm theory", managers need to ________.',
         [('A', 'regard decision-making as a cooperative process'),
          ('B', 'persuade others to follow your ways of thinking'),
          ('C', 'accept different ideas and keep them balanced'),
          ('D', 'pick out a right person to make the final decision')], 'A',
         '细节理解题。第3段描述蜂群决策："perform a \'dance\' to get other bees to follow them""the bees with the best dance attract the most votes – and a decision is made"，即通过个体间的信息交换与"投票"共同达成决定；Miller 随即总结"you need to seek out diversity in your team... gathering up quite different ideas"，强调决策是协作过程，故选 A。C 项"保持平衡"属过度引申；B 项与"寻求多样性"相反；D 项"选一个人拍板"与蜂群的集体投票相悖。')

choice_q(66, 'Which of the following can be inferred from the last paragraph?',
         [('A', 'Leadership skills can be developed through practical work.'),
          ('B', 'Employees work more efficiently when organized by leaders.'),
          ('C', 'Strengthened hierarchy is the guarantee of work efficiency.'),
          ('D', 'Employees should be allowed to make their own decisions.')], 'D',
         '推理判断题。末段写蚁群"In an ant colony, there is no leader. Ants are self-organized, and respond to their environment and each other"，并借 Miller 之口指出"your hierarchy is getting in the way of getting the work done"——等级制度反而妨碍工作开展。由此可推知，应让员工自主决策、自我组织，故选 D。B、C 项与原文"等级制度妨碍效率"相反；A 项文中未涉及。')

# ---------- Section C 六选四 ----------
P(doc, ('Section C  六选四阅读填空', 'h2'), before=200, after=40)
quick(doc, '67-70: E B A D    [干扰项：C、F]')

P(doc, ('Directions: Complete the following passage by using the sentences given below. Each sentence can be used only once. Note that there are two more sentences than you need.', 'n'), after=40)

P(doc, ('【选项池解析与标注】', 'l20'), before=60, after=40)

P(doc, ('[A] Science has never had much influence on these decisions.    译文：科学对这些决定从来影响甚微。    ', 'r'),
  ('备课精注：对应69空。下文紧接"If it did, we wouldn\'t have lived in a society that allows teenagers to drive before they can buy beer"，if it did 中的 it 正指 A 项所述"科学的影响"，虚拟语气反证"科学其实并未影响这些决定"。', 'g'), after=30)

P(doc, ('[B] There is no single age at which the teenage brain becomes an adult brain.    译文：并不存在某个特定年龄，能让青少年大脑一跃成为成人大脑。    ', 'r'),
  ('备课精注：对应68空。该段小标题为"不同脑区成熟时间表不同"，B 项"没有单一的成年年龄"正是其直接结论，且下文以逻辑思维脑区（16岁）与自控脑区（青年期仍在发育）为例加以印证。', 'g'), after=30)

P(doc, ('[C] However, neuroscience findings prove to be helpful in making a new boundary.    译文：然而，神经科学的发现被证明有助于划定新的界限。    ', 'p19'),
  ('【干扰项：转折关系与第2段开头"Maybe. But it\'s not as simple as it seems"重复冲突；且全文主旨是科学对政治边界影响有限，与本项"有助于划定新界限"相悖】', 'g'), after=30)

P(doc, ('[D] Child growth patterns differ and how cultures understand child growth is so different.    译文：儿童生长模式各不相同，各文化对儿童成长的理解也大相径庭。    ', 'r'),
  ('备课精注：对应70空。该段以荷兰（16岁可饮酒、19岁才能驾车）为例，说明各国年龄界限差异之大，正是 D 项"生长模式与文化理解各异"的具体展开，并自然引出"追究所谓\'正确\'成熟年龄毫无意义"。', 'g'), after=30)

P(doc, ('[E] Some people think this knowledge can help us rethink where we draw legal boundaries between kids and adults.    译文：有些人认为，这一认识有助于我们重新思考在儿童与成人之间划定法律界限的位置。    ', 'r'),
  ('备课精注：对应67空。空前指出"部分脑区要到20岁出头才完全成熟"，E 项承接该发现并引出"法律界限"这一新话题；下一段"Maybe."正是对 E 项中 Some people think 的回应。', 'g'), after=30)

P(doc, ('[F] This discovery may well indicate that neuroscience can help us better understand the interrelationship among different ages.    译文：这一发现很可能表明，神经科学能帮助我们更好地理解不同年龄段之间的相互关系。    ', 'p19'),
  ('【干扰项：内容空泛，未涉及下文反复讨论的"法律界限"核心话题；且"不同年龄段之间的相互关系"与上下文均无呼应】', 'g'), after=60)

P(doc, ('When Does a Teenager Become an Adult?', 'pt'), align=C, before=80, after=40)

P(doc, ('Neuroscientists (神经科学家) now know that brain maturation (成熟) occurs far later than previously thought. Great changes in brain are still taking place during young adulthood, especially in the regions of decision making, reasoning, comparing risk and reward, etc. Indeed, some brain regions do not reach full maturity until the early 20s. 67 ', 'n'),
  ('【E】 Some people think this knowledge can help us rethink where we draw legal boundaries between kids and adults.', 'r'),
  (' （有些人认为，这一认识有助于我们重新思考在儿童与成人之间划定法律界限的位置）  ', 'n'),
  ('【备课衔接：67空位于首段末尾。空前给出"部分脑区20岁出头才成熟"的科学发现，E 项顺势把话题从"脑发育"推进到"法律界限"，为下文"这可行吗"埋下引子。】', 'g'),
  indent=True)

P(doc, ('Maybe. But it\'s not as simple as it seems for two reasons.', 'n'), indent=True)

P(doc, ('1. Different brain regions mature along with different timetables. 68 ', 'n'),
  ('【B】 There is no single age at which the teenage brain becomes an adult brain.', 'r'),
  (' （并不存在某个特定年龄，能让青少年大脑一跃成为成人大脑）  ', 'n'),
  ('【备课衔接：68空紧随小标题"不同脑区成熟时间表不同"，B 项是该标题的直接推论；空后立即以"逻辑思维脑区16岁成熟、自控脑区青年期仍在发育"作具体例证，衔接紧密。】', 'g'),
  (' The part of the brain that handles logical thinking is usually fully developed by 16, but those involved in self-discipline are still developing in young adulthood. This means they may not have the same level of emotional control, which can make them less responsible for their actions.', 'n'),
  indent=True)

P(doc, ('2. 69 ', 'n'),
  ('【A】 Science has never had much influence on these decisions.', 'r'),
  (' （科学对这些决定从来影响甚微）  ', 'n'),
  ('【备课衔接：69空位于第二个分论点开头。空后"If it did, we wouldn\'t have lived in a society that allows teenagers to drive before they can buy beer"以虚拟语气反证，it 即回指 A 项中的 science；紧随其后的"Age boundaries are drawn mainly for political reasons"进一步坐实该判断。】', 'g'),
  (' If it did, we wouldn\'t have lived in a society that allows teenagers to drive before they can buy beer. Age boundaries are drawn mainly for political reasons, not scientific ones. It\'s a pity that neuroscience won\'t have much of an impact on politics although it is always correct.', 'n'),
  indent=True)

P(doc, ('70 ', 'n'),
  ('【D】 Child growth patterns differ and how cultures understand child growth is so different.', 'r'),
  (' （儿童生长模式各不相同，各文化对儿童成长的理解也大相径庭）  ', 'n'),
  ('【备课衔接：70空位于末段段首。空后"It is pointless to try to determine the \'right\' age of maturation"是全文结论，D 项先摆出"差异普遍存在"这一事实，再引出"追究统一年龄无意义"的判断，逻辑上构成由事实到结论的推进；荷兰的例子则是对 D 项的直接例证。】', 'g'),
  (' It is pointless to try to determine the "right" age of maturation. The Dutch, for example, allow children to drink alcohol at the age of 16 but not to drive until they are 19. Even if I firmly believe legal decisions should refer to neuroscience seriously and it\'s a good idea to lower the drinking age and raise the driving age, I recognize that the government might never accept it.', 'n'),
  indent=True)

# ============================================================
# 第 II 卷
# ============================================================
P(doc, ('第II卷', 'h1'), before=240, after=60)

# ---------- IV. Summary Writing ----------
P(doc, ('IV. Summary Writing (71)', 'h2'), before=80, after=40)
quick(doc, '71. 见下方官方参考范文（59 words）')

P(doc, ('Directions: Read the following passage. Summarize in no more than 60 words the main idea of the passage and how it is illustrated. Use your own words as far as possible.', 'n'), after=40)

P(doc, ('Why Children Need to Get Muddy', 'pt'), align=C, before=80, after=40)

P(doc, ('With the rise of urbanism (城市化), and the attraction of video games and social media, contact with nature is much rarer than in the past. For many, there is simply no opportunity to get muddy. Today, many parents may secretly wish their children had the chance to pick up a bit of dirt.', 'n'), indent=True)

P(doc, ('Many of the psychological benefits of outdoor play are already well established. Our brains evolved in natural landscapes. This means that natural scenes provide the perfect level of stimulation, which is thought to help recharge the brain when it is tired and easily unfocused. Supporting this theory, one study from 2009 found that children with attention-deficit hyperactivity disorder (ADHD) (注意力缺陷多动症) were better able to concentrate following a 20-minute walk in the park, compared to a 20-minute walk on the streets of a well-kept urban area. Being close to grass and trees seemed to have had a beneficial effect on their minds. The authors recommended using such "doses of nature" as a safe and accessible way of supporting children with ADHD, alongside other tools.', 'n'), indent=True)

P(doc, ('Outdoor play can also offer valuable learning experiences. For example, the act of shaping and stretching materials like mud or sand can help children develop the way their senses and movement interact, known as sensorimotor (感觉运动) development, according to the scientists at the University of Palermo, Italy. This allows the child to gradually understand his or her bodily signals.', 'n'), indent=True)

P(doc, ('Given the known psychological benefits, many day-care centers and schools are already encouraging greater contact with nature: outdoor lessons, regular nature walks and the construction of mud kitchens that encourage children to play in the dirt.', 'n'), indent=True)

P(doc, ('【官方参考范文】', 'l20'), before=100, after=20)
P(doc, ('Urbanization and technology have made it difficult for children to be close to nature. Actually, outdoor play has many psychological benefits, such as recharging the brain and improving concentration, which is particularly beneficial for children with ADHD. Meanwhile, outdoor play can help children develop their sensorimotor skill through learning experience. Realizing these benefits, many organizations are offering outdoor activities. (59 words)', 'ru'), indent=True, after=40)

P(doc, ('【要点提炼与评分维度解析】', 'l20'), before=60, after=20)
P(doc, ('• 核心论点（Main Idea）：城市化与科技的发展，使儿童与自然接触的机会大幅减少。', 'g'), after=0)
P(doc, ('• 原因或细节（Illustration）：① 户外活动对大脑有多重心理益处——为疲惫、易分心的头脑"充电"，并能显著改善多动症（ADHD）儿童的注意力；② 户外玩耍还能提供学习体验，如玩泥玩沙促进感觉运动（sensorimotor）发展。', 'g'), after=0)
P(doc, ('• 语言重组亮点：用 have made it difficult for children to be close to nature 概括首段三个并列原因（城市化、电子游戏、社交媒体）；用 Actually / Meanwhile 两个连接词分层，避免逐句翻译；用 Realizing these benefits 的分词短语收束末段"机构已在行动"的信息，句数少而信息密度高。', 'g'), after=0)
P(doc, ('• 分值分布：内容要点 5 分（①城市化与科技致接触自然减少 1 分；②户外活动对大脑的益处、含 ADHD 特别益处 2 分；③促进感觉运动技能发展 1 分；④学校等机构提供户外活动 1 分）；语言 5 分（语法、词汇、拼写、连贯性）。字数 59 词，符合"不超过 60 词"要求。', 'g'), after=60)

# ---------- V. Translation ----------
P(doc, ('V. Translation (3+3+4+5=15分)', 'h2'), before=160, after=40)
quick(doc, '72-75 见下方参考译文')

P(doc, ('Directions: Translate the following sentences into English, using the words given in the brackets.', 'n'), after=40)

# 72
P(doc, ('72. 考虑到学生的实际需求，学校餐厅周末向学生开放。(open)', 'b'), before=100, after=20)
P(doc, ('【参考译文】 Considering the actual needs of the students, the school canteen is open to students on weekends. (3分)', 'ru'), after=20)
P(doc, ('【分值采分点与考点精析】', 'l20'), before=20, after=10)
P(doc, ('• 采分点：Considering the actual needs of the students 分词短语作状语 1 分；the school canteen is open to students 主系表结构 1 分；on weekends 时间状语 1 分。', 'g'), after=0)
P(doc, ('• 词汇句法：open 在此为形容词"开放的、营业的"，须用 be open to sb 而非 be opened to sb（opened 是被动"被打开"，语义不同）；considering 已语法化为介词/分词，意为"考虑到"，后直接接名词短语，不加 that。', 'g'), after=40)

# 73
P(doc, ('73. 教练和运动员为决赛做了详细的训练计划，对冠军志在必得。(determine)', 'b'), before=80, after=20)
P(doc, ('【参考译文】 The coach and players have made a detailed training plan for the final and are determined to win the championship. (3分)', 'ru'), after=20)
P(doc, ('【分值采分点与考点精析】', 'l20'), before=20, after=10)
P(doc, ('• 采分点：have made a detailed training plan for the final 1 分；are determined to win 1 分；the championship 1 分。', 'g'), after=0)
P(doc, ('• 词汇句法：be determined to do sth 意为"决心做某事"，determined 为形容词化的过去分词，须与 be 连用，不可直接作谓语（determine to do = decide to do，是动词用法，主语主动决定）；"志在必得"对应 be determined to win / be bent on winning；"冠军"用 the championship（头衔）而非 the champion（人）。', 'g'), after=40)

# 74
P(doc, ('74. 这家饭店对所有客人热情相迎，消费再低也不会被另眼相待。(no matter)', 'b'), before=80, after=20)
P(doc, ('【参考译文】 This restaurant warmly welcomes all the guests, and no matter how little money people spend there, they won\'t be treated differently. (4分)', 'ru'), after=20)
P(doc, ('【参考译文·替换版】 This restaurant gives a warm welcome to all its guests; no matter how small the amount they spend, they will not be treated unequally. (4分)', 'ru'), after=20)
P(doc, ('【分值采分点与考点精析】', 'l20'), before=20, after=10)
P(doc, ('• 采分点：warmly welcomes all the guests 1 分；no matter how little (money) people spend 2 分（引导词 1 分 + 语序与时态 1 分）；won\'t be treated differently 1 分。', 'g'), after=0)
P(doc, ('• 词汇句法：no matter how + 形容词/副词 + 主语 + 谓语，必须用陈述语序，不可写成 no matter how little do people spend；"另眼相待"译为 be treated differently / unequally，用被动语态承接主语 they（客人）；"消费再低"中的"低"指金额少，用 little（修饰不可数）或 small，不用 low。', 'g'), after=40)

# 75
P(doc, ('75. 这个街区缺乏健身设施的问题引起了当地政府高度关注，已筹措资金将一幢废弃的厂房改建成一座老少咸宜的运动中心。(attention)', 'b'), before=80, after=20)
P(doc, ('【参考译文】 The lack of fitness facilities in this community has aroused significant attention of the local government, and funds have been raised to transform an abandoned factory building into a sports center suitable for people of all ages. (5分)', 'ru'), after=20)
P(doc, ('【参考译文·替换版】 The shortage of fitness facilities in this neighborhood has attracted great attention from the local government, which has raised funds to turn an abandoned factory into a sports center for all ages. (5分)', 'ru'), after=20)
P(doc, ('【分值采分点与考点精析】', 'l20'), before=20, after=10)
P(doc, ('• 采分点：The lack of fitness facilities in this community 1 分；has aroused/attracted significant attention (of/from) the local government 1 分；funds have been raised 1 分；transform/turn ... into ... 1 分；suitable for people of all ages 1 分。', 'g'), after=0)
P(doc, ('• 词汇句法：arouse / attract / draw attention 均可，注意介词搭配 attention of sb 或 attention from sb；"筹措资金"用 raise funds，且资金是被筹措的，用被动 funds have been raised 更贴合"已"这一完成含义；transform A into B（= turn A into B）为固定搭配，into 不可换成 to；"老少咸宜"用 suitable for people of all ages 或 for all ages，注意 suitable 后接 for 而非 to；"厂房"用 factory building，避免与 factory（工厂整体）混淆。', 'g'), after=60)

# ============================================================
OUT = '/Users/linquin/WorkBuddy AI/EnglishTeacher-Workspace/2024届高三英语走向成功 周中练习八（备课讲义版）.docx'
doc.save(OUT)
print('saved:', OUT)
