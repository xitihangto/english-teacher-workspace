# -*- coding: utf-8 -*-
"""周末练习六 备课讲义生成脚本（依据 规范/01 v1.15）。"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from jy_builder import Book

OUT = os.path.join(ROOT, '生成物', '高三英语周末练习六（备课讲义版）.docx')

b = Book()

# ---------- 便捷片段 ----------
def N(t):  return (t, 'n')
def B(t):  return (t, 'b')
def R(t):  return (t, 'r')      # 正确答案（红/粗/下划线）
def RU(t): return (t, 'ru')     # 正确答案（红/粗）
def P(t):  return (t, 'p')      # 干扰项（紫）
def G(t):  return (t, 'g')      # 解析（绿）
def GB(t): return (t, 'gb')     # 出处标注（绿粗）
def T(t):  return (t, 't333')   # 灰字

def para(parts, indent=False):
    return b.rich(parts, indent=indent)

def gr(parts):
    return b.rich(parts, kind='g')

def opt(correct, *items):
    """构造选项行：correct 为正确字母；items = [(字母, 英文, 中文), ...]"""
    out = []
    for i, (ch, en, cn) in enumerate(items):
        seg = f'{ch}. {en} ({cn})'
        if ch == correct:
            seg += ' ★'
        out.append((('  ' if i else '') + seg, 'ru' if ch == correct else 'p'))
    return out

def cloze(num, letter, word, cn_map, note):
    """完形一个空：含空原文句 → 选项 → 精析。cn_map = [(字母,中文),...]"""
    pass

# =========================================================
# 卷头
# =========================================================
b.title('高三英语周末练习六（备课讲义版）')

# =========================================================
# II. Grammar and Vocabulary
# =========================================================
b.h1('II. Grammar and Vocabulary (20分)')

# ---- Section A 语法填空 ----
b.h2('Section A (10分) 语法填空')
b.quick('【本节答案速查】 21. was launched    22. although    23. employing    24. (being) done    25. had spent    26. may/might    27. who    28. in/on    29. more advanced    30. to create')
b.dir('Directions: After reading the passage below, fill in the blanks to make the passage coherent and grammatically correct. For the blanks with a given word, fill in each blank with the proper form of the given word; for the other blanks, use one word that best fits each blank.')
b.pt('OpenAI Announces ChatGPT Successor GPT-4')

para([N('OpenAI has released GPT-4, the latest version of its hugely popular artificial intelligence chatbot ChatGPT.')], indent=True)

para([
    N('The new model can respond to images by providing recipe suggestions from photos of ingredients as well as writing captions and descriptions. It can also process up to 25,000 words, about eight times as many as ChatGPT. Millions of people have used ChatGPT since it '),
    R('21. was launched'),
    G(' (launch) 【一般过去时被动语态：it 指代 ChatGPT，与 launch 为被动关系，且有明确过去时间状语 in November 2022，故填 was launched】'),
    N(' in November 2022. Popular requests for it include writing songs, poems, marketing copy, computer code, and helping with homework, '),
    R('22. although'),
    G(' 【让步状语从句：前句讲 ChatGPT 广受欢迎，后句讲老师认为学生不该用，前后为让步关系，填 although/though】'),
    N(' teachers say students shouldn’t use it. ChatGPT answers questions '),
    R('23. employing'),
    G(' (employ) 【现在分词作方式状语：employ 与主语 ChatGPT 为主动关系，表“采用、使用”某种语言，用 employing】'),
    N(' natural human-like language, and it can also imitate other writing styles such as songwriters and authors, using the Internet as its knowledge database.'),
], indent=True)

para([
    N('There are concerns that it could one day take over many jobs currently '),
    R('24. (being) done'),
    G(' (do) 【过去分词作后置定语：jobs 与 do 为被动关系，currently 表进行，故可用 (being) done 修饰 jobs，意为“目前由人类承担的”】'),
    N(' by humans. OpenAI said it '),
    R('25. had spent'),
    G(' (spend) 【过去完成时：said 为过去时，“投入六个月”发生在 said 之前，属“过去的过去”，用 had spent】'),
    N(' six months on safety features for GPT-4, and on human feedback. However, it warned that it '),
    R('26. may/might'),
    G(' 【情态动词：warned that 后接可能性的委婉表述，用 may/might 表“可能”，与 warned 的时态一致用 might 亦可】'),
    N(' still be subject to sharing disinformation.'),
], indent=True)

para([
    N('GPT-4 will initially be available to ChatGPT Plus subscribers, '),
    R('27. who'),
    G(' 【非限制性定语从句：先行词 subscribers 指人，从句缺主语，用关系代词 who 引导】'),
    N(' pay $20 per month for easy access to the service. It’s already powering Microsoft’s Bing search engine platform. The tech giant has invested $10b '),
    R('28. in/on'),
    G(' 【介词搭配：invest (money) in/on sth. 意为“把钱投资于……”，$10b 后接投资对象 OpenAI，填 in 或 on】'),
    N(' OpenAI.'),
], indent=True)

para([
    N('GPT-4 has “'),
    R('29. more advanced'),
    G(' (advanced) 【形容词比较级：后有 than ChatGPT，构成比较结构，advanced 为多音节形容词，比较级加 more】'),
    N(' reasoning skills” than ChatGPT, OpenAI said. The model can, for example, find available meeting times for three schedules.'),
], indent=True)

para([
    N('OpenAI also announced new partnerships with language learning app Duolingo and Be My Eyes, an application for the visually impaired, '),
    R('30. to create'),
    G(' (create) 【不定式作目的状语：宣布合作的目的是“开发”能帮助用户的聊天机器人，表目的用 to create】'),
    N(' AI Chatbots which can assist their users using natural language.'),
], indent=True)

para([N('However, like its predecessors (被替代的事物), OpenAI has warned that GPT-4 is still not fully reliable and it may invent facts or make reasoning errors.')], indent=True)

# ---- Section B 选词填空 ----
b.h2('Section B (10分) 选词填空')
b.quick('【本节答案速查】 31-35: I G F B K    36-40: A H C D E    [多余项：J. seeks]')
b.dir('Directions: Complete the following passage by using the words in the box. Each word can only be used once. Note that there is one word more than you need.')
b.rich([B('【原始备选词汇框】')], kind='label')
b.rich([T('A. breakthroughs 突破    B. core 核心的    C. driver 驱动因素    D. empower 赋能/使能够    E. fully 充分地    F. increasingly 日益')], kind='t333')
b.rich([T('G. mounting 越来越多的    H. potential 潜力/潜在的    I. promoting 促进    J. seeks 寻求    K. serves 服务')], kind='t333')
b.pt('Companies Help Integrate (整合) Digital Real Economies')

para([
    N('Chinese platform companies are doubling down on the most advanced digital technologies to seek new drivers in revenue (财政收入) growth, as the country puts greater emphasis on '),
    R('31. I. promoting'),
    G('（促进）'),
    N(' the in-depth integration of the digital and real economies, experts and company executives said.'),
], indent=True)

para([
    N('Despite the depressing global outlook and '),
    R('32. G. mounting'),
    G('（越来越多的/加剧的）'),
    N(' uncertainties, China’s platform economy is playing a(n) '),
    R('33. F. increasingly'),
    G('（日益）'),
    N(' vital role in boosting technological innovation and high-quality development.'),
], indent=True)

b.rich([('【就近选项参考池】 [I] promoting (促进) — 对应31空：on promoting the in-depth integration 促进深度融合；[G] mounting (越来越多的) — 对应32空：mounting uncertainties 越来越多的不确定性；[F] increasingly (日益) — 对应33空：increasingly vital role 日益重要的作用', 'label')], kind='label')

para([
    N('During an earnings conference with investors on Thursday, Zhang Yong, chairman and CEO of Alibaba Group, said that cloud computing is one of the company’s '),
    R('34. B. core'),
    G('（核心的）'),
    N(' strategies for the future, and Alibaba Cloud is also the foundation through which the company '),
    R('35. K. serves'),
    G('（服务）'),
    N(' the real economy and drives the integration of the digital and real economies.'),
], indent=True)

b.rich([('【就近选项参考池】 [B] core (核心的) — 对应34空：core strategies 核心战略；[K] serves (服务) — 对应35空：serves the real economy 服务实体经济', 'label')], kind='label')

para([
    N('Noting that this is a critical period for technological '),
    R('36. A. breakthroughs'),
    G('（突破）'),
    N(' and development in cloud computing and AI, Zhang said he believed in the vast '),
    R('37. H. potential'),
    G('（潜力）'),
    N(' of industrial digitalization and the role of cloud computing as the focus of the digital economy.'),
], indent=True)

para([
    N('Revenue in the cloud business, Alibaba’s main growth '),
    R('38. C. driver'),
    G('（驱动因素）'),
    N(' besides e-commerce, reached 20.18 billion yuan during the October-December period, an increase of 3% year-on-year, mainly driven by public cloud growth.'),
], indent=True)

b.rich([('【就近选项参考池】 [A] breakthroughs (突破) — 对应36空：technological breakthroughs 技术突破；[H] potential (潜力) — 对应37空：vast potential 巨大潜力；[C] driver (驱动因素) — 对应38空：main growth driver 主要增长驱动', 'label')], kind='label')

para([
    N('The company is making efforts to make use of digital technologies to help small and medium-sized enterprises and speed up industrial transformation (工业转型) in an effort to '),
    R('39. D. empower'),
    G('（赋能）'),
    N(' the real economy.'),
], indent=True)

para([
    N('The tone-setting Central Economic Work Conference in mid-December said that platform companies will be supported to “'),
    R('40. E. fully'),
    G('（充分地）'),
    N(' display their capabilities” in encouraging economic growth, job creation and international competition. The conference also emphasized the need to energetically develop the digital economy.'),
], indent=True)

b.rich([('【就近选项参考池】 [D] empower (赋能) — 对应39空：empower the real economy 赋能实体经济；[E] fully (充分地) — 对应40空：fully display their capabilities 充分展示能力；[J] seeks (寻求) 多余未选干扰项', 'label')], kind='label')

# =========================================================
# III. Reading Comprehension
# =========================================================
b.h1('III. Reading Comprehension (45分)')

# ---- Section A 完形填空 ----
b.h2('Section A (15分) 完形填空')
b.quick('【本节答案速查】 41-45: B D A B D    46-50: C A C B A    51-55: D B B D C')
b.dir('Directions: For each blank in the following passage there are four words or phrases marked A, B, C and D. Fill in each blank with the word or phrase that best fits the context.')

def clz(sent_parts, num, opts_items, correct, note):
    """句子级一空一组：含空句 → 【第N题】选项 → 思路精析"""
    para(sent_parts, indent=True)
    line = [(f'【第 {num} 题】', 'b')]
    line += opt(correct, *opts_items)
    b.rich(line)
    gr([G('思路精析：' + note)])

# 段1
para([N('It is Nobel Prize week, the one week every year when people from all corners of the globe celebrate science, read about ribosomes (核糖体), and give their best shot at trying to understand particle physics. It is also the one week when science is guaranteed some prime headline space on mainstream news outlets.')], indent=True)
clz([N('And yet the science Nobels (in medicine, physics, and chemistry) present a(n) '), R('41 B. outdated'), N(' view of science.')],
    41, [('A','strange','奇怪的'), ('B','outdated','过时的'), ('C','all-round','全面的'), ('D','advanced','先进的')], 'B',
    '首段先铺垫“诺奖周全民关注科学”，随后 And yet 转折，指出诺贝尔科学奖呈现的是一种“过时（outdated）”的科学观——后文论证现代科学是集体协作，而诺奖只表彰三人，正是“过时”的体现。A strange（奇怪的）、C all-round（全面的）、D advanced（先进的）均与转折方向不符。')

# 段2
clz([N('The problem starts with the '), R('42 D. figure'), N(' of prize-winners selected every year.')],
    42, [('A','quality','质量'), ('B','diversity','多样性'), ('C','discipline','学科'), ('D','figure','人数/数字')], 'D',
    '本段讲“问题始于每年获奖者的______”。后句“规则把每个奖项限制在三人以内”正是对空的解释——被限制的是“人数（figure）”。A quality、B diversity、C discipline 都无法与“三人”这一数量限制对应。')
clz([N('The rules governing the Nobel Prize '), R('43 A. restrict'), N(' it to just three winners in each category.')],
    43, [('A','restrict','限制'), ('B','extend','扩展'), ('C','relate','关联'), ('D','apply','应用')], 'A',
    '主语是 rules governing the Nobel Prize（诺奖规则），宾语 it 后接 to just three winners，构成 restrict ... to ...（把……限制在……）的固定搭配。B extend、C relate、D apply 均不与“it to just three”搭配。')
clz([N('This means that for every discovery that is awarded a Nobel, the majority of contributing scientists end up being '), R('44 B. ignored'), N('.')],
    44, [('A','employed','受雇'), ('B','ignored','被忽视'), ('C','respected','受尊重'), ('D','nominated','被提名')], 'B',
    '因为每项发现最多只表彰三人，“大多数有贡献的科学家最终______”。与“获奖”相对的是“被忽视（ignored）”。A employed、C respected、D nominated 都不合“落选”语境。')

# 段3
clz([N('As a matter of fact, science has never been a(n) '), R('45 D. individual'), N(' effort.')],
    45, [('A','terrific','极好的'), ('B','constant','持续的'), ('C','intellectual','智力的'), ('D','individual','个人的')], 'D',
    'As a matter of fact 引出本段主旨——科学从来不是“个人的（individual）”努力。后文牛顿“站在巨人肩上”、阿姆斯特朗登月靠数十万工程师，都是反证。A terrific、B constant、C intellectual 均不与“集体协作”构成对立。')
para([N('Isaac Newton stood on the “shoulders of giants”; Neil Armstrong’s “one small step” was a dream realized by hundreds of thousands of engineers and scientists.')], indent=True)
clz([N('Science is, and always has been, and repetitive process where individuals draw on discoveries made by others to '), R('46 C. gradually'), N(' advance the boundaries of human knowledge.')],
    46, [('A','naturally','自然地'), ('B','rapidly','快速地'), ('C','gradually','逐渐地'), ('D','personally','个人地')], 'C',
    'individuals draw on discoveries made by others to ______ advance the boundaries（借鉴他人发现来______推进认知边界）。科学进步是代际累积的“逐步（gradually）”过程。A naturally、B rapidly、D personally 不合“累积”语义。')
clz([N('Yes, Albert Einstein famously won the Nobel Prize all by himself for a paper he alone authored, but he could not have made his discoveries without '), R('47 A. previous'), N(' work by Max Planck, James Maxwell, and several others.')],
    47, [('A','previous','先前的'), ('B','subsequent','后续的'), ('C','physical','物理的'), ('D','commercial','商业的')], 'A',
    '爱因斯坦的发现离不开普朗克、麦克斯韦等人的______工作。这些成果在爱因斯坦之前，故用 previous（先前的）。B subsequent 时间相反；C physical、D commercial 与上下文无关。')

# 段4
clz([N('To make matters worse, typical of the Nobel Prizes, none of the '), R('48 C. awardees'), N(' was a first author on any of the publications cited by the prize announcements.')],
    48, [('A','employees','雇员'), ('B','addressees','收件人'), ('C','awardees','获奖者'), ('D','refugees','难民')], 'C',
    '本句说“______中没有一人是授奖公告所引论文的第一作者”。指代“获奖者”用 awardees。A employees、B addressees、D refugees 均不指获奖人。')
para([N('The first author of a scientific paper is typically the person who did the hands-on laboratory work, usually a graduate student or young post-doctoral researcher.')], indent=True)
clz([N('It is precisely these '), R('49 B. early-career'), N(' researchers who are in greater need of the Nobel Prize money than their generally tenured (终身的) supervisors.')],
    49, [('A','chief-position','首席职位'), ('B','early-career','职业早期'), ('C','senior-management','高级管理'), ('D','academic-world','学术界')], 'B',
    '前句说明第一作者通常是做实验的研究生或年轻博士后，即“职业早期（early-career）”研究者。A chief-position、C senior-management 与“年轻”矛盾，D academic-world 不能修饰 researchers。')

# 段5
clz([N('More basically, awarding the prizes to only three scientists spreads a vision of science as an individual enterprise. By ensuring that graduate students are not given '), R('50 A. due'), N(' recognition, the prizes reinforce (加强) the mistaken image of a scientist as an old white man in a lab coat.')],
    50, [('A','due','应有的'), ('B','immediate','立即的'), ('C','literary','文学的'), ('D','governmental','政府的')], 'A',
    'not given ______ recognition（没有得到______认可）。固定搭配 due recognition（应有的认可）。B immediate、C literary、D governmental 均不搭配。')
clz([N('This can only '), R('51 D. step up'), N(' gender and racial inequalities in science, especially further along in an academic career.')],
    51, [('A','turn down','拒绝/调低'), ('B','level off','趋平'), ('C','take away','消除'), ('D','step up','加剧/提升')], 'D',
    'This can only ______ gender and racial inequalities（这只会______性别与种族不平等）。step up 有“加剧、提升”之意，符合“强化错误印象→加剧不平等”。A turn down、B level off、C take away 方向相反。')

# 段6
clz([N('Any one of these reasons is sufficient to '), R('52 B. reform'), N(' the Nobel Prizes.')],
    52, [('A','claim','声称'), ('B','reform','改革'), ('C','present','呈现'), ('D','announce','宣布')], 'B',
    'Any one of these reasons is sufficient to ______ the Nobel Prizes（上述任一理由都足以______诺贝尔奖）。后句 Here is one idea 提出改制方案，故为 reform（改革）。A claim、C present、D announce 都不引出下文的改制建议。')
clz([N('Here is one idea: Award the Nobel Prizes not to '), R('53 B. researchers'), N(' but for discoveries; donate the prize money to an international science fund to promote further exploration in each year’s prize-winning field of research.')],
    53, [('A','organizers','组织者'), ('B','researchers','研究者'), ('C','sponsors','赞助商'), ('D','supervisors','导师')], 'B',
    'Award the Nobel Prizes not to ______ but for discoveries（把奖颁给“发现”而不是“______”）。全文批判“奖给人”，故为 researchers（研究者）。A organizers、C sponsors、D supervisors 都偏离“科学家”这一核心。')

# 段7
clz([N('A science-oriented Nobel, rather than a scientist-oriented one, would educate the public in the most important scientific developments and, '), R('54 D. in turn'), N(', stimulate new scientific progress by using the prize money to fund the next generation of researchers.')],
    54, [('A','in fact','事实上'), ('B','in comparison','相比之下'), ('C','in theory','理论上'), ('D','in turn','继而/反过来')], 'D',
    '空前“教育公众了解最重要科学进展”，空后“用奖金资助下一代研究者以刺激新进展”，前后为连锁递进关系，用 in turn（继而、反过来）。A in fact、B in comparison、C in theory 都不表连锁。')
clz([N('Science works best when the '), R('55 C. achievements'), N(' of one generation of scientists are paid forward to drive the next to even greater heights.')],
    55, [('A','legends','传奇'), ('B','spirits','精神'), ('C','achievements','成就'), ('D','mysteries','奥秘')], 'C',
    'the ______ of one generation are paid forward to drive the next（一代科学家的______被传递下去推动下一代）。“成就（achievements）”最合语境。A legends、B spirits、D mysteries 都不能与“推动下一代到更高处”搭配。')
para([N('That is to say, scientists of different generations work with joint efforts to support future scientific advancements for the betterment of society as a whole.')], indent=True)

# ---- Section B 阅读理解 ----
b.h2('Section B (30分) 阅读理解')
b.quick('【本节答案速查】 56-59: A C C B    60-62: C D C    63-66: B B D C')
b.dir('Directions: Read the following three passages. Each passage is followed by several questions or unfinished statements. For each of them there are four choices marked A, B, C and D. Choose the one that fits best according to the information given in the passage you have just read.')

# (A)
b.pt('(A)')
para([
    N('On the track for the 400-meter dash at the 1958 British Empire and Commonwealth Games, Mikha Singh shot from the start as fast as possible, but then, in a second, sensed Malcolm Spence of South Africa over his shoulder. At the line, with six inches between them, Singh won the gold.'),
    GB(' [56A 出处：六英寸之差＝险胜]'),
    N(' The audience broke into applause. To them, however, he was just a village boy who ran with his arms gracefully waving. They did not know that, for him, running was not a sport. It was everything, his religion, his beloved, and his life.'),
], indent=True)
para([
    N('As a child, Singh ran to get an education outside his home village. The school was ten kilometers away.'),
    GB(' [57 排序依据③ school education]'),
    N(' But at the age of 18, Singh ran to save his very life. In 1947, the village was being split between India and Pakistan. Crowds of Muslim outsiders suddenly arrived in his village, ordering his family to convert to Islam or die. His father, dying, shouted, “Run, Milkha, run!” He raced for the forest, crying.'),
], indent=True)
para([
    N('There followed a time when Singh hopped trains as a refugee, shoeless and starving. Eventually the army took him on. There he discovered running of a new kind, with coaching, races over set lengths, and prizes. The first race he won rewarded him with a daily glass of milk.'),
    GB(' [57 排序依据① milk as a prize]'),
], indent=True)
para([
    N('As a result, Singh began the hard, necessary work, six hours a day. He pushed his body to the limit out of pride—and for India. His iron discipline finally paid off.'),
    GB(' [58C 出处：six hours a day / pushed his body to the limit ＝ constant effort]'),
    N(' In 1960, he was invited to compete against Pakistan’s champion runner. At first, Singh refused to go since his childhood home was there and now he was still covered in his mind with the blood of his family. However, the moment Singh crossed the border, to his surprise, he was welcomed with flags and flowers. When he won his race, the then Pakistani prime minister said, “Pakistan bestows on (授予) you the title of The Flying Sikh. ” Despite everything that had happened, Singh had two countries.'),
    GB(' [57 排序依据④ the title of The Flying Sikh；59 主旨依据：跑步贯穿一生]'),
], indent=True)

b.rich([B('56. Milkha Singh _________ at the 1958 British Empire and Commonwealth Games.')])
b.rich(opt('A', ('A','narrowly won the 400-meter dash','险胜400米'), ('B','broke the world record for the 400 meters','打破400米世界纪录'), ('C','was already a household name before the 400-meter dash','赛前已家喻户晓'), ('D','had little confidence in himself before the 400-meter dash','赛前缺乏自信')))
gr([G('【解析定位】 细节题。定位首段 “At the line, with six inches between them, Singh won the gold.” 六英寸之差即“险胜（narrowly won）”。B 世界纪录无依据；C 与 “to them, he was just a village boy” 相反；D 缺乏自信未提及。故选 A。')])

b.rich([B('57. Put the following things in the time order of their appearance in Singh’s life.')])
b.rich([N('① milk as a prize    ② gold medal    ③ school education    ④ the title of The Flying Sikh')])
b.rich(opt('C', ('A','①②③④','牛奶—金牌—上学—称号'), ('B','①③②④','牛奶—上学—金牌—称号'), ('C','③①②④','上学—牛奶—金牌—称号'), ('D','③①④②','上学—牛奶—称号—金牌')))
gr([G('【解析定位】 排序题。时间线：童年每天跑十公里上学（③）→ 参军后首次夺冠奖励一杯牛奶（①）→ 1958 年夺金（②）→ 1960 年访巴获“飞行锡克教徒”称号（④）。故 ③①②④。故选 C。')])

b.rich([B('58. Singh’s success as an athlete lies in his _______________.')])
b.rich(opt('C', ('A','good luck','好运'), ('B','rare talent','罕见天赋'), ('C','constant effort','持续的努力'), ('D','patient coaches','耐心的教练')))
gr([G('【解析定位】 推断题。定位末段 “began the hard, necessary work, six hours a day… pushed his body to the limit”，说明成功源于持续努力（constant effort）。A 好运、B 天赋、D 耐心教练均未提及。故选 C。')])

b.rich([B('59. What is the best title of the passage?')])
b.rich(opt('B', ('A','War and Peace','战争与和平'), ('B','Lifelong Running','终身奔跑'), ('C','A Fierce Competition','一场激烈的比赛'), ('D','Running for Education','为教育而跑')))
gr([G('【解析定位】 主旨题。全文从童年为求学而跑、为逃命而跑，到参军发现跑步、为国争光，跑步贯穿其一生，故 “Lifelong Running” 最贴切。A 偏离主题；C 仅涉一场比赛；D 只覆盖童年。故选 B。')])

# (B)
b.pt('(B)')
para([
    N('If you have an investment portfolio (投资组合) of $500,000 or more, get...'),
    GB(' [62 出处：以资产门槛招揽客户 ＝ 寻找潜在客户]'),
], indent=True)
para([N('______________________________________________________________________________')])
para([N('About Fisher Investments')])
para([
    N('Fisher Investments is a money management enterprise serving over 85,000 clients as well as large institutional investors. * We have been managing portfolios through bull and bear markets for over 40 years. Fisher Investments has managed over $169 billion in client investments. *'),
    GB(' [61D 出处：enterprise ＝ a company]'),
], indent=True)
para([N('_______________________________________________________________________________')])

b.rich([B('60. If Mike is considering developing a tax-efficient retirement strategy, which tip can he turn to for reference?')])
b.rich(opt('C', ('A','Tip #10.','第10条'), ('B','Tip #23.','第23条'), ('C','Tip #40.','第40条'), ('D','Tip #85.','第85条')))
gr([G('【解析定位】 细节题（广告信息提取）。题干问“制定节税退休策略”可参阅哪条提示，对应原文指南中的 Tip #40。属广告类文本的定点信息定位。故选 C。')])

b.rich([B('61. What is “Fisher Investments”?')])
b.rich(opt('D', ('A','An app.','一个应用'), ('B','A book.','一本书'), ('C','A website.','一个网站'), ('D','A company.','一家公司')))
gr([G('【解析定位】 事实题。定位 “About Fisher Investments” 段首句 “Fisher Investments is a money management enterprise…”，enterprise 与 company 同义，故为“一家公司”。故选 D。')])

b.rich([B('62. What is the main purpose of this passage?')])
b.rich(opt('C', ('A','To give investment advice to anyone planning to retire.','给所有计划退休者投资建议'), ('B','To provide a free guide on retirement planning to everyone.','向所有人提供免费指南'), ('C','To seek potential customers who are interested in retirement planning.','寻找有意退休规划的潜在客户'), ('D','To offer a special bonus report on maximizing Social Security benefits for retirement.','提供社保福利特别报告')))
gr([G('【解析定位】 写作目的题。全文以 “If you have an investment portfolio of $500,000 or more, get…” 设资产门槛招揽高净值客户，并引导索取免费指南，目的是寻找潜在客户。A、B 称面向所有人，与 $500,000 门槛矛盾；D 仅为诱饵细节。故选 C。')])
gr([G('【原材料提示】 本篇为广告类文本，原卷扫描排版有缺字（首句不完整、部分选项缺字母标记），题目按原卷与答案原样转录。')])

# (C)
b.pt('(C)')
para([N('A baby born today will be thirty-something in 2050. If all goes well, that baby will still be around in 2100, and might even be an active citizen of the 22nd century. What should we teach that baby to help them survive and flourish in the world of 2050 and beyond? What kind of skills will they need in order to get a job, understand what is happening around them, and navigate their tough life?')], indent=True)
para([N('At present, too many schools across the world focus on providing pupils with a set of predetermined skills, such as writing computer code in C++ and conversing in Chinese. Yet since we have no idea how the world and the job market will look in 2050, we don’t really know what particular skills people will need. We might invest a lot of effort in teaching kids how to write in C++ or to speak Chinese, only to discover sooner or later that AI will have been able to code software far better than humans, and that a new translation app will have enabled you to conduct a conversation in almost flawless Mandarin, Cantonese or Hakka, even though you only know how to say ni hao.')], indent=True)
para([
    N('So what should we be teaching? Many experts argue that schools should '),
    B('downplay'),
    N(' technical skills and emphasize general-purpose life skills: the ability to deal with change, to learn new things, and to preserve your mental balance in unfamiliar situations. In order to keep up with the world of 2050, you will above all need to reinvent yourself again and again.'),
    GB(' [63B 出处：downplay 与 emphasize 反义并列；64B 出处：deal with change / learn new things ＝ adaptability]'),
], indent=True)
para([
    N('To succeed in such a demanding task, you will need to work very hard on getting to know your operating system better—to know what you are and what you want from life. This is, of course, the oldest advice in the book: know thyself. This advice was never more urgent than in the mid-21st century, because unlike in the days of Laozi or Socrates, now you have serious competition. Coca-Cola, Amazon and Facebook are all racing to hack you.'),
    GB(' [65D 出处：know your operating system 为后文 outrun algorithms 张本]'),
], indent=True)
para([N('Right now, the algorithms (算法) are watching where you go, what you buy, and who you meet. Soon they will monitor all your steps, breaths and heartbeats. They are relying on big data and machine learning to get to know you better and better. And once these algorithms know you better than you know yourself, they could control and manipulate (操纵) you. In the end, authority will shift to them.')], indent=True)
para([
    N('Of course, you might be perfectly happy giving up all authority to the algorithms and trusting them to make decisions for you and for the rest of the world. If, however, you want to maintain some control over your personal existence and over the future of life in general, you have to run faster than the algorithms. To run fast, don’t take much luggage with you. Leave all your illusions (幻想) behind. They are very heavy.'),
    GB(' [65D 出处：run faster than the algorithms / maintain some control]'),
], indent=True)

b.rich([B('63. What does the underlined word “downplay” in paragraph 3 most probably mean?')])
b.rich(opt('B', ('A','Give too much emphasis on something.','过分强调'), ('B','Make people think that something is less important.','使显得不那么重要/轻视'), ('C','Offer your reasons why something is right or wrong.','给出对错的理由'), ('D','Decide something in advance so that it does not happen.','预先决定以免发生')))
gr([G('【解析定位】 词义猜测题。定位第三段 “schools should downplay technical skills and emphasize general-purpose life skills”，downplay 与 emphasize（强调）由 and 反义并列，故为“贬低、轻视（使显得不那么重要）”。故选 B。')])

b.rich([B('64. According to the article, ___________ plays a vital role in children’s bright future.')])
b.rich(opt('B', ('A','imagination','想象力'), ('B','adaptability','适应力'), ('C','self-discipline','自律'), ('D','a good sense of balance','良好的平衡感')))
gr([G('【解析定位】 细节题。定位第三段 “emphasize general-purpose life skills: the ability to deal with change, to learn new things…”，即“适应力（adaptability）”。A 想象力、C 自律未提及；D 混淆 mental balance（心理平衡）与“平衡感”。故选 B。')])

b.rich([B('65. It’s important to know our operating system because ___________.')])
b.rich(opt('D', ('A','if we don’t, algorithms will hack all our devices.','否则算法会入侵所有设备'), ('B','it is an essential skill for us to succeed in the world of 2050.','是2050年成功的必备技能'), ('C','we need to learn how algorithms work and make full use of them.','需要学会利用算法'), ('D','we need to outrun algorithms to keep some control over our personal life.','需跑赢算法以保住对个人生活的掌控')))
gr([G('【解析定位】 细节/因果题。定位末段 “If you want to maintain some control over your personal existence… you have to run faster than the algorithms”，说明“了解自己的操作系统”是为了跑赢算法、保住个人生活的掌控权。A 过于具体；B 未点明与算法的关系；C 与文意相反。故选 D。')])

b.rich([B('66. The article mainly talks about _________.')])
b.rich(opt('C', ('A','the importance of knowing yourself','认识自己的重要性'), ('B','the threats and dangers of technology','技术的威胁与危险'), ('C','what kind of skills we might need in the future','未来可能需要什么样的技能'), ('D','some potential benefits algorithms would bring to humankind','算法可能给人类带来的好处')))
gr([G('【解析定位】 主旨题。全文以 2050 年的婴儿开篇，围绕“该教什么技能”展开：先否定预设技能（C++、中文），再提出通用生活技能与认识自我，核心是“未来可能需要什么样的技能”。A、B 仅为部分论据；D 与文意相反。故选 C。')])

# ---- Section C 六选四 ----
b.h2('Section C (8分) 六选四')
b.quick('【本节答案速查】 67-70: B E F A    [干扰项：C、D]')
b.dir('Directions: Read the following passage. Fill in each blank with a proper sentence given in the box. Each sentence can be used only once. Note that there are two more sentences than you need.')

b.rich([('【选项池解析与标注】', 'label')])
b.rich([RU('A. Tailor Vitamin C intake to your weight. (根据体重调整维C摄入量)  '), G('译文：按体重定制你的维C摄入量。'), G(' 备课精注：对应70空，为该段主题句。')])
b.rich([RU('B. The subjects who couldn’t perform this had a higher risk of death. (无法做到的受试者死亡风险更高)  '), G('译文：无法完成这一动作的受试者死亡风险更高。'), G(' 备课精注：对应67空，是研究的“结论”。')])
b.rich([P('C. Vitamin C supplements are always safe and effective for everyone. (维C补充剂对所有人总是安全有效的)  '), G('译文：维C补充剂对所有人总是安全有效的。'), G(' 【干扰项：与末段“按体重摄入”及 F 项的安全警告矛盾】')])
b.rich([P('D. Regular exercise can improve your balance and reduce the risk of falls. (规律运动可改善平衡、降低跌倒风险)  '), G('译文：规律运动能改善平衡并降低跌倒风险。'), G(' 【干扰项：虽与平衡话题相关，但首段结论句已由 B 占据，无处可填】')])
b.rich([RU('E. Both are harmless and don’t require treatment unless their appearance is an issue. (两者均无害，除非影响外观否则无需治疗)  '), G('译文：两者都无害，除非外观成问题否则不需要治疗。'), G(' 备课精注：对应68空，承上“两类斑点”，启下“不必自行去除”。')])
b.rich([RU('F. But these products can contain a large amount of salicylic acid (水杨酸) and could leave you with permanent scars. (但这些产品可能含水杨酸并留下永久疤痕)  '), G('译文：但这些产品可能含有大量水杨酸，并可能留下永久疤痕。'), G(' 备课精注：对应69空，解释 FDA 警告的原因。')])

b.pt('News From The World of Medicine')
b.rich([B('The balance challenge')])
para([
    N('Can you stand on one leg for ten seconds? This question could help doctors assess the overall health of their middle-aged and older patients, argues a Brazilian-led study published in the British Journal of Sports Medicine. '),
    R('【67 B】 The subjects who couldn’t perform this had a higher risk of death. (无法完成这一动作的受试者死亡风险更高)'),
    G(' 【备课衔接：空前提出“单腿站立十秒”的评估方法，空后说“七年随访后得出上述结论”，故空处应是结论本身；B 中 this 指代站立动作，承上启下。】'),
    N(' During a follow-up period of seven years, the researchers drew the above conclusion after accounting for basic factors like age and sex.'),
], indent=True)
para([N('Besides causing falls, poor balance can also signal underlying medical issues, such as declining eyesight or nerve damage caused by diabetes (糖尿病). Much like grasp strength and walking speed, balancing ability doesn’t tell the whole story of your health, but it’s a useful clue.')], indent=True)
b.rich([B('Don’t remove skin tags and moles yourself.')])
para([
    N('Two of the most common types of skin spots among adults are dark spots known as moles and the growths known as skin tags. '),
    R('【68 E】 Both are harmless and don’t require treatment unless their appearance is an issue. (两者均无害，除非外观成问题否则无需治疗)'),
    G(' 【备课衔接：空前介绍痣与皮赘是最常见的两类皮肤斑点，E 中 Both 正好回指这两类，并引出后文“不必自行去除”。】'),
], indent=True)
para([
    N('In some places, mole- and skin-tag removal kits are sold for home use. '),
    R('【69 F】 But these products can contain a large amount of salicylic acid (水杨酸) and could leave you with permanent scars. (但这些产品可能含水杨酸并留下永久疤痕)'),
    G(' 【备课衔接：空前说有家用去除套装售卖，空后说 FDA 收到受伤报告并发出警告；F 以 But 转折，说明套装的危险成分，正是警告的原因。】'),
    N(' US FDA recently issued a warning about these kits after receiving reports about consumers who had injured themselves. You’re better off visiting a dermatologist, who are experts in treating skin diseases. Plus, they can perform the all-important screening for skin cancer.'),
], indent=True)
para([
    R('【70 A】 Tailor Vitamin C intake to your weight. (根据体重调整维C摄入量)'),
    G(' 【备课衔接：空后整段讲新西兰研究者按体重给出维C摄入量（60公斤110毫克，90公斤140毫克），A 正是对该段的概括，作主题句。】'),
], indent=True)
para([N('Researchers from New Zealand recommend a 60-kilogram person consume 110 milligrams of vitamin C per day through a balanced diet, while someone weighing 90 kilograms needs 140 milligrams. That is to say, when taking vitamin C, it’s best to take your weight into account. Eating foods like oranges—which contain on average 70 milligrams of vitamin C each—can really help.')], indent=True)

# =========================================================
# IV. Summary Writing
# =========================================================
b.h1('IV. Summary Writing (10分)')
b.rich([B('71.')])
b.pt('A Montessori Education')
para([N('There are now at least 60,000 schools across the world using the Montessori method. There are different kinds of Montessori schools, but certain fundamental principles have remained the same.')], indent=True)
para([N('One is the idea of teachers encouraging the children to complete the activities with as little adult involvement as possible. Take the Ecoscuola Montessori on the Italian island of Sicily. At the school, there is a subject called “Practical Life”. It involves real-life practical tasks, such as serving drinks to their classmates. For safety, teachers would take charge of boiling the water, but the children would play active roles in cleaning the work surface and then presenting the drinks to others. “During breakfast and lunch, they are also self-directed, taking it in turns to lay the table and serve their classmates,” says Miriam Ferro, the headteacher of Ecoscuola.')], indent=True)
para([N('The method encourages not only independence, but also cooperation. Children of different ages are taught in the same classroom, so that the six-year-olds, for example, can help the three-year-olds. In addition, each session is three hours long so as to allow the children to bury themselves in what they are doing. The learning materials are also designed for being handled and explored with all their senses. For example, letters and numbers are made of sandpaper, which the child can trace with their finger.')], indent=True)
para([N('This concept may sound sensible. But does it bring about any tangible (实际的) benefits, beyond those seen in a typical classroom?')], indent=True)
para([N('Angeline Lillard, a professor of psychology, found some benefits for children’s development while looking at a Montessori school in Milwaukee, in the United States. Analyzing their progress at age five, she found that the children tended to have better literacy, numeracy, executive function and social skills, compared to those who had attended the other schools. And at age 12, they showed better story-telling abilities.')], indent=True)

b.rich([('【官方参考范文】', 'label')])
para([
    N('Despite the difference between schools using Montessori education method, fundamental principles are the same. Children are encouraged to finish tasks with little or no help of adults. It cultivates their independence and cooperation. Besides, children can learn to stay focused on their task with all their senses. Beyond typical classrooms, children are also found to have developed their abilities. (59 words)'),
])
b.rich([('【参考范文·替换版】', 'label')])
para([
    N('According to the basic principles of Montessori schools, children are encouraged to finish tasks with little or no help of adults. It cultivates not only their independence but also cooperation ability. Besides, children can learn to stay focused on their task with all their senses. Children can also develop their abilities in reading, writing, calculating and interactive skills.'),
])
b.rich([('【要点提炼与评分维度解析】', 'label')])
gr([G('• 核心论点：蒙特梭利学校形式各异，但基本原则一致——鼓励儿童在成人极少介入的情况下独立完成活动（Despite the difference… fundamental principles are the same）。')])
gr([G('• 原因或细节：① 培养独立性，也培养合作能力（混龄教学、三小时长课时、砂纸字母等多感官教具）；② 实证研究表明，蒙特梭利儿童在读写、计算、执行功能与社交技能上更优，12 岁时叙事能力更强。')])
gr([G('• 语言重组亮点：用 Despite the difference… 概括“形式不同、原则相同”；用 cultivate their independence and cooperation 一个动宾结构浓缩原文两大目标；用 Beyond typical classrooms 引出附加收益，避免罗列原文细节。全文 59 词，符合 60 词左右的篇幅要求。')])

# =========================================================
# V. Translation
# =========================================================
b.h1('V. Translation (15分)')
b.dir('Directions: Translate the following sentences into English, using the words given in the brackets.')
b.quick('【本节分值】 72. 3分    73. 3分    74. 4分    75. 5分')

b.rich([B('72. 你要学会用具体的例子来更清晰地阐述你的观点。(quote)')])
b.rich([('【参考译文】', 'label'), RU(' You should learn to quote some specific examples to illustrate your points more clearly. (3分)')])
b.rich([('【参考译文·替换版】', 'label'), R(' You should learn to illustrate your points more clearly by quoting some specific examples.')])
gr([G('• 采分点：quote（引用）；illustrate / elaborate your points（阐述观点）；more clearly（更清晰地）。')])
gr([G('• 词汇句法：learn to do sth. 学会做某事；by quoting… 作方式状语。易错：illustrate 拼写；quote（引用原话）与 cite（引证）的区分。')])

b.rich([B('73. 这部新片取材于老百姓的日常生活，很受欢迎。(anchor)')])
b.rich([('【参考译文】', 'label'), RU(' The newly-released film is anchored in ordinary people’s daily life, so / and it is warmly welcomed. (3分)')])
gr([G('• 采分点：be anchored in（以……为根基 / 取材于）；ordinary people’s daily life（老百姓的日常生活）；be warmly welcomed（深受欢迎）。')])
gr([G('• 词汇句法：anchor 本义“抛锚”，此处引申为“扎根于、取材于”，需接介词 in；so / and 连接结果分句。易错：newly-released 复合形容词的构成。')])

b.rich([B('74. 帮助孩子学会解决传统习俗和现代技术之间的冲突是有挑战性的，但这是一项孩子必须掌握的技能。(grasp)')])
b.rich([('【参考译文】', 'label'), RU(' Helping children learn how to deal with the conflict between traditional customs and modern technology is challenging, but it is a skill that they must have a good grasp of / grasp. (4分)')])
gr([G('• 采分点：deal with / handle the conflict between… and…（解决……与……之间的冲突）；traditional customs vs modern technology；challenging（有挑战性的）；have a good grasp of（掌握）。')])
gr([G('• 词汇句法：动名词短语 Helping children learn… 作主语，谓语用单数 is；that 引导定语从句修饰 a skill。易错：grasp 此处为名词，需用 have a good grasp of 搭配。')])

b.rich([B('75. 成功人士都有一个共同点：尽管历经可怕的挫折，他们依然对生活抱以积极的态度，并凭着顽强的意志力实现自己的理想。(What)')])
b.rich([('【参考译文】', 'label'), RU(' What successful people have in common is that despite terrible setbacks, they still have a positive attitude towards life and realize their dreams with a strong will. (5分)')])
b.rich([('【参考译文·替换版】', 'label'), R(' What successful people have in common is that despite the fact that they have suffered terrible setbacks, they still have a positive attitude towards life and realize their dreams with a strong will.')])
gr([G('• 采分点：What… have in common is that…（主语从句 + 表语从句）；despite terrible setbacks（尽管历经挫折）；have a positive attitude towards life（对生活抱积极态度）；realize their dreams with a strong will（凭顽强意志实现理想）。')])
gr([G('• 词汇句法：What 引导主语从句时谓语用单数 is；despite 为介词，后接名词短语（不可接句子，若用句子须加 the fact that）。易错：realize one’s dream 的固定搭配；will 作“意志”时为不可数名词。')])

# =========================================================
b.save(OUT)
print('saved:', OUT)
