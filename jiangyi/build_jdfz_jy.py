# -*- coding: utf-8 -*-
"""生成《交大附中2026-2027学年高三上第一次调研测试英语（备课讲义版）》。"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from jy_builder import Book

b = Book()

# ============ 卷头 ============
b.title('交大附中2026-2027学年高三上第一次调研测试英语（备课讲义版）')
b.rich([('【卷面说明】 ', 'label'),
        ('原材料（公众号图文）从 “II. Grammar and Vocabulary 的 Section B” 开始，Section A 未出现在原材料中，故本讲义自 Section B 起编。', 'g')],
       kind='label')

# ============ II. Grammar and Vocabulary ============
b.h1('II. Grammar and Vocabulary (20分)')
b.h2('Section B (20分) 选词填空')
b.quick('【本节答案速查】 1-10: H I F B A K D C E J    11-20: K B G A J C H D E I    [多余项：(A) G. overwhelmed；(B) F. cutting-edge]')
b.dir('Directions: Fill in each blank with the correct word from the box. Each word can be used only once. Note that there are two more words than you need.')

b.rich([('(A)', 'pt')], align='center', kind='pt')
b.label('【原始备选词汇框】')
b.rich([('A. carries    B. experienced    C. implies    D. involved    E. integrating    F. longing', 't333')], after=0)
b.rich([('G. overwhelmed    H. perspective    I. release    J. touching    K. throwing', 't333')])
b.pt('A recipe for peace')

b.rich([('French filmmaker Francois Truffaut once claimed most war films glorify violence. To break this paradox, Chinese director Wen Muye presents a unique anti-war ', 'n'),
        ('H. perspective 观点/视角', 'r'),
        (' 【名词作宾语。a unique anti-war perspective 意为“独特的反战视角”，与后文 through ordinary food and humanity（借日常饮食与人性）呼应；perspective 常与 present/offer 搭配。】', 'g'),
        (' through ordinary food and humanity in his new blockbuster Once Upon a Time in the Middle East.', 'n')], indent=True)

b.rich([('Starring famous actor Shen Teng, the film has achieved remarkable success since its ', 'n'),
        ('I. release 上映/发行', 'r'),
        (' 【名词。since its release 意为“自上映以来”，与后半句 has grossed… / has dominated… 的现在完成时呼应。】', 'g'),
        (' It has grossed over 1.6 billion yuan and dominated China’s daily box office for 14 straight days, earning an impressive 8.6 rating on Douban. Audiences speak highly of its nuanced description of human nature in wars and profound reflection on people’s ', 'n'),
        ('F. longing 渴望', 'r'),
        (' 【名词。people’s longing for peace 意为“人们对和平的渴望”，longing for 为固定搭配，与 profound reflection（深刻反思）并列，说明影片的思想深度。】', 'g'),
        (' for peace.', 'n')], indent=True)

b.rich([('【就近选项参考池】 ', 'label'),
        ('[H] perspective (观点/视角) — 对应1空：a unique anti-war perspective 独特的反战视角    |    [I] release (上映/发行) — 对应2空：since its release 自上映以来    |    [F] longing (渴望) — 对应3空：people’s longing for peace 人们对和平的渴望', 't333')], kind='label')

b.rich([('Different from traditional domestic war works, the film creatively combines overseas warfare with Chinese cuisine. It centers on Xu Fu, a(n) ', 'n'),
        ('B. experienced 经验丰富的', 'r'),
        (' 【形容词作前置定语。an experienced chef 意为“一位经验丰富的厨师”，修饰主人公徐福；后文 who works in a Middle East restaurant to pay off debts 交代其身份背景。】', 'g'),
        (' chef who works in a Middle East restaurant to pay off debts. For Chinese people, food is never merely to relieve hunger. It ', 'n'),
        ('A. carries 承载', 'r'),
        (' 【动词第三人称单数。It carries family memories… 意为“它承载着家庭记忆、文化传统与真挚祝福”，主语 It 指 food，carry 在此表“承载、包含”。】', 'g'),
        (' family memories, cultural traditions and sincere blessings, symbols deeply rooted in Chinese culture.', 'n')], indent=True)

b.rich([('Peaceful daily life soon collapses as war breaks out, ', 'n'),
        ('K. throwing 使……陷入', 'r'),
        (' 【现在分词作结果状语。throw… into… 意为“使……陷入（混乱）”，与前半句“战火爆发、平静生活崩塌”构成因果。】', 'g'),
        (' the country into chaos. Trapped in gunfire and ruins, Xu and his friend get ', 'n'),
        ('D. involved 卷入的', 'r'),
        (' 【形容词。get involved in 意为“卷入、陷入”，与 in dangerous crises 搭配，与后半句 bond with war orphans 并列，交代主人公处境。】', 'g'),
        (' in dangerous crises and bond with war orphans suffering from extremist forces’ brainwashing.', 'n')], indent=True)

b.rich([('【就近选项参考池】 ', 'label'),
        ('[B] experienced (经验丰富的) — 对应4空：an experienced chef 经验丰富的厨师    |    [A] carries (承载) — 对应5空：It carries family memories 它承载着家庭记忆    |    [K] throwing (使……陷入) — 对应6空：throwing the country into chaos 使国家陷入混乱    |    [D] involved (卷入的) — 对应7空：get involved in dangerous crises 陷入危险危机', 't333')], kind='label')

b.rich([('Throughout the chaotic war scenes, food always serves as a symbol of reunion, harmony and connection. The director explains that Chinese dining culture ', 'n'),
        ('C. implies 意味着/暗示', 'r'),
        (' 【动词第三人称单数。imply doing sth 后接动名词，implies stopping conflicts and embracing peace 意为“意味着止息冲突、拥抱和平”，与并列的 embracing 形式一致。】', 'g'),
        (' stopping conflicts and embracing peace. The warm custom of sharing meals reflects ordinary people’s humble wish for safety and reunion amid turbulence.', 'n')], indent=True)

b.rich([('Devoted to authentic creation, the crew made great efforts in scene setting and food design. By ', 'n'),
        ('E. integrating 融合', 'r'),
        (' 【介词 By 后接动名词。integrate A with B 意为“把 A 与 B 融合”，与后文 the film vividly shows cultural integration 直接呼应，是本段的“题眼”。】', 'g'),
        (' northeastern Chinese cooking skills with local foreign styles, the film vividly shows cultural integration. Ultimately, it conveys a(n) ', 'n'),
        ('J. touching 动人的', 'r'),
        (' 【形容词作定语。a touching core message 意为“一条动人的核心信息”，与后文 the deepest love and sincere hope 的情感基调一致。】', 'g'),
        (' core message: in chaotic times, the simple wish of “eating well” represents the deepest love and sincere hope for surviving hardships and returning home safely.', 'n')], indent=True)

b.rich([('【就近选项参考池】 ', 'label'),
        ('[C] implies (意味着) — 对应8空：implies stopping conflicts 意味着止息冲突    |    [E] integrating (融合) — 对应9空：By integrating… with… 通过把……与……融合    |    [J] touching (动人的) — 对应10空：a touching core message 一条动人的核心信息    |    多余未选干扰项：G. overwhelmed (不知所措的)', 't333')], kind='label')

# ---------- (B) ----------
b.rich([('(B)', 'pt')], align='center', kind='pt')
b.label('【原始备选词汇框】')
b.rich([('A. appreciation    B. boast    C. bridge    D. creativity    E. crosses    F. cutting-edge', 't333')], after=0)
b.rich([('G. exposing    H. houses    I. knowledge-focused    J. updated    K. waking', 't333')])
b.pt('Night reveals beauty of Longmen Grottoes')

b.rich([('As darkness descends over the Yi River, the stone carvings of the Longmen Grottoes, a UNESCO World Heritage Site in Luoyang, Henan province, begin glowing softly in hidden-lamp light, as if ', 'n'),
        ('K. waking 苏醒', 'r'),
        (' 【现在分词。as if waking to life 意为“仿佛苏醒过来”，as if 后接分词短语，主语 the stone carvings 与 wake 构成主动关系，写出夜灯下石窟“活起来”的效果。】', 'g'),
        (' to life.', 'n')], indent=True)

b.rich([('Among its numerous wonders, Fengxian Temple stands out, with nine giant Buddhist-deity statues dominating a cliff face. The carvings ', 'n'),
        ('B. boast 拥有（引以为傲的特点）', 'r'),
        (' 【动词第三人称单数。boast 作动词表“拥有（值得骄傲的事物）”，boast staggering scale and strikingly lifelike facial expressions 意为“拥有惊人的规模与栩栩如生的面部表情”。】', 'g'),
        (' staggering scale and strikingly lifelike facial expressions. UNESCO states that the extraordinary stone carvings perfectly reflect the high cultural level and sophisticated society of Tang-Dynasty China. The grand Vairocana Buddha gazes across the river, having endured nearly 1,300 years of wind, rain and historical changes.', 'n')], indent=True)

b.rich([('For night-tour visitors, the route resembles a slowly unfurling scroll painting. Niches (壁龛) carved 1,500 years ago receive subtle lighting, ', 'n'),
        ('G. exposing 使显露', 'r'),
        (' 【现在分词作结果状语。exposing delicate ancient chisel marks 意为“使精美的古代凿痕显露出来”，与 receive subtle lighting（受柔光照射）构成因果。】', 'g'),
        (' delicate ancient chisel (凿刻) marks. A tour guide comments that night-time sightseeing brings visitors spiritual resonance for people of all nationalities share a common ', 'n'),
        ('A. appreciation 欣赏/鉴赏', 'r'),
        (' 【名词。a common appreciation for such timeless beauty 意为“对这般永恒之美的共同欣赏”，appreciation for 为固定搭配，与 share 连用表“共有”。】', 'g'),
        (' for such timeless beauty.', 'n')], indent=True)

b.rich([('【就近选项参考池】 ', 'label'),
        ('[K] waking (苏醒) — 对应11空：as if waking to life 仿佛苏醒过来    |    [B] boast (拥有) — 对应12空：The carvings boast staggering scale 这些造像拥有惊人的规模    |    [G] exposing (使显露) — 对应13空：exposing delicate ancient chisel marks 使精美的古代凿痕显露    |    [A] appreciation (欣赏) — 对应14空：a common appreciation for such timeless beauty 对这般永恒之美的共同欣赏', 't333')], kind='label')

b.rich([('Longmen Grottoes launched night tours in 2007 and has repeatedly ', 'n'),
        ('J. updated 更新', 'r'),
        (' 【过去分词。has repeatedly updated facilities 意为“多次更新设施”，与 has repeatedly 构成现在完成时；update 的过去分词为规则变化 updated。】', 'g'),
        (' facilities. China’s 240-hour visa-free transit policy brought a sharp rise in overseas tourists, turning Luoyang into an unmistakable travel destination. To ', 'n'),
        ('C. bridge 弥合', 'r'),
        (' 【动词原形（To 后接不定式表目的）。bridge cultural gaps 意为“弥合文化差异”，bridge 作动词表“弥合、架桥连接”，为高频搭配。】', 'g'),
        (' cultural gaps, the site has built a professional multilingual-guide team, and night tours have become its major attraction.', 'n')], indent=True)

b.rich([('Spanning 400 years of creation, Longmen Grottoes ', 'n'),
        ('H. houses 容纳/收藏', 'r'),
        (' 【动词第三人称单数。house 作动词表“收藏、容纳”，houses over 100,000 Buddhist statues 意为“容纳十万余尊佛像”，主语把石窟群视为一个整体，故用单数谓语。】', 'g'),
        (' over 100,000 Buddhist statues within 2,345 caves and niches. UNESCO regards these sculptures as an outstanding manifestation of human artistic ', 'n'),
        ('D. creativity 创造力', 'r'),
        (' 【名词。human artistic creativity 意为“人类的艺术创造力”，与 outstanding manifestation（杰出体现）搭配，artistic creativity 为常见搭配。】', 'g'),
        (', showing the perfection of a mature art form that greatly influenced Asian cultural evolution. Its sculptural charm ', 'n'),
        ('E. crosses 跨越', 'r'),
        (' 【动词第三人称单数。cross borders 意为“跨越国界”，与 strikes a chord with audiences from diverse cultural backgrounds 并列，说明其艺术感染力。】', 'g'),
        (' borders and strikes a chord with audiences from diverse cultural backgrounds.', 'n')], indent=True)

b.rich([('On global social-media platforms, overseas creators share videos of the hand-carved grottoes. Many tourists arrange full-experience trips: viewing relics in daylight before enjoying night scenes; some wear hanfu to immerse themselves in Tang-style atmospheres. Nowadays, more visitors favour ', 'n'),
        ('I. knowledge-focused 以知识为核心的', 'r'),
        (' 【形容词作定语。knowledge-focused immersive cultural travel 意为“以知识为核心的沉浸式文化旅游”，与 rather than simple photo-taking（而非单纯拍照）形成对比。】', 'g'),
        (' immersive cultural travel rather than simple photo-taking. When night falls, lit stone figures keep their silent vigil, with the Yi River reflecting flickering lights.', 'n')], indent=True)

b.rich([('【就近选项参考池】 ', 'label'),
        ('[J] updated (更新) — 对应15空：has repeatedly updated facilities 多次更新设施    |    [C] bridge (弥合) — 对应16空：To bridge cultural gaps 为弥合文化差异    |    [H] houses (容纳) — 对应17空：houses over 100,000 Buddhist statues 容纳十万余尊佛像    |    [D] creativity (创造力) — 对应18空：human artistic creativity 人类艺术创造力    |    [E] crosses (跨越) — 对应19空：crosses borders 跨越国界    |    [I] knowledge-focused (以知识为核心的) — 对应20空：knowledge-focused immersive cultural travel 以知识为核心的沉浸式文化旅游    |    多余未选干扰项：F. cutting-edge (尖端的)', 't333')], kind='label')

# ============ III. Reading Comprehension ============
b.h1('III. Reading Comprehension (45分)')
b.h2('Section A (15分) 完形填空')
b.quick('【本节答案速查】 21-25: D C B A A    26-30: C D D B A    31-35: C B C B D')
b.dir('Directions: For each blank in the following passage there are four words or phrases marked A, B, C and D. Fill in each blank with the word or phrase that best fits the context.')
b.pt('Why Saying “Late Bloomer” Is Wrong')


def kun(parts, num, opts, ana, indent=False):
    b.rich(parts, indent=indent, kind='n')
    runs = [('【第 %d 题】 ' % num, 'b')]
    for i, (letter, word, gloss, ok) in enumerate(opts):
        if i:
            runs.append(('    ', 'b'))
        runs.append(('%s. %s (%s)%s' % (letter, word, gloss, ' ★' if ok else ''), 'ru' if ok else 'p'))
    b.rich(runs, kind='b')
    b.green('思路精析：' + ana)


b.rich([('Doree Shafrir considers herself to be a late bloomer. She got married at 38, had her first child at 41, and generally sees herself as having been late “to finding the kind of work I ', 'n'),
        ('21 D. truly', 'r'),
        (' like to do.”', 'n')], indent=True, kind='n')
b.rich([('【第 21 题】 ', 'b'), ('A. mainly (主要地)', 'p'), ('    ', 'b'), ('B. broadly (大体上/广泛地)', 'p'),
        ('    ', 'b'), ('C. roughly (粗略地)', 'p'), ('    ', 'b'), ('D. truly (真正地) ★', 'ru')], kind='b')
b.green('思路精析：引号内为 the kind of work I truly like to do（我真正想做的那类工作），truly 修饰 like，强调内心真正的意愿；mainly / broadly / roughly 都偏向“范围、程度”的估计，与 like 的语义不搭。')

b.rich([('While the road has not always been smooth, the Los Angeles-based author, 44, now feels gratitude for her journey, along with a new outlook on the ', 'n'),
        ('22 C. milestones', 'r'),
        (' that she once felt she was missing.', 'n')], kind='n')
b.rich([('【第 22 题】 ', 'b'), ('A. expectations (期望)', 'p'), ('    ', 'b'), ('B. rewards (回报)', 'p'),
        ('    ', 'b'), ('C. milestones (里程碑) ★', 'ru'), ('    ', 'b'), ('D. possessions (财产)', 'p')], kind='b')
b.green('思路精析：紧接的 “These goals are relatively arbitrary and culturally prescribed” 中的 These goals 正指此空；下文又两次出现 milestones（hit these milestones “late”、a rigid timeline of professional and personal milestones），属原词复现，故选 C。')

b.rich([('“These goals are relatively arbitrary (武断的) and culturally prescribed,” Shafrir says. “I now see that the things I saw as ‘mistakes’ were just another part of my story.”', 'n')], kind='n')
b.rich([('Shafrir views her memoir, Thanks for Waiting: The Joy (& Weirdness) of Being a Late Bloomer, as a “gentle corrective to the idea that we’re supposed to do things on a schedule.” Yet it is a notion that is ', 'n'),
        ('23 B. deep-rooted', 'r'),
        ('.', 'n')], indent=True, kind='n')
b.rich([('【第 23 题】 ', 'b'), ('A. cold-blooded (冷血的)', 'p'), ('    ', 'b'), ('B. deep-rooted (根深蒂固的) ★', 'ru'),
        ('    ', 'b'), ('C. far-sighted (有远见的)', 'p'), ('    ', 'b'), ('D. single-minded (一心一意的)', 'p')], kind='b')
b.green('思路精析：Yet 表转折——她的书只是对这一观念“温和的纠正”，反衬该观念“根深蒂固”；后文 a societal tendency、Many of us feel… that our paths should… 也都在说明这种想法普遍而牢固。')

b.rich([('Many of us feel—consciously or otherwise—that our paths should ', 'n'),
        ('24 A. fit into', 'r'),
        (' a rigid timeline of professional and personal milestones.', 'n')], kind='n')
b.rich([('【第 24 题】 ', 'b'), ('A. fit into (符合/嵌入) ★', 'ru'), ('    ', 'b'), ('B. break into (强行进入)', 'p'),
        ('    ', 'b'), ('C. account for (解释/占比)', 'p'), ('    ', 'b'), ('D. make for (走向/有助于)', 'p')], kind='b')
b.green('思路精析：空格宾语是 a rigid timeline（僵化的时间表），“我们觉得自己的人生路径应当套进这张时间表”，fit into 意为“符合、嵌入”，与 rigid 的“刻板、不可变通”呼应。')

b.rich([('We may judge ourselves negatively if we hit these milestones “late,” in part because of a societal tendency to ', 'n'),
        ('25 A. admire', 'r'),
        (' youthful achievement.', 'n')], kind='n')
b.rich([('【第 25 题】 ', 'b'), ('A. admire (仰慕/推崇) ★', 'ru'), ('    ', 'b'), ('B. doubt (怀疑)', 'p'),
        ('    ', 'b'), ('C. envy (羡慕)', 'p'), ('    ', 'b'), ('D. strike (打动/撞击)', 'p')], kind='b')
b.green('思路精析：社会“推崇”年少成名，我们才会把“晚”当作失败。envy 侧重羡慕他人“拥有的东西”，与抽象的 youthful achievement 搭配不如 admire 自然；doubt 与句意相反；strike 不搭配。')

b.rich([('Yet plenty of people find professional fulfillment, financial prosperity, or rewarding relationships within their own time frames. In fact, research shows that people today are increasingly likely to ', 'n'),
        ('26 C. accomplish', 'r'),
        (' major life events at a later age than previous generations.', 'n')], indent=True, kind='n')
b.rich([('【第 26 题】 ', 'b'), ('A. encounter (遭遇)', 'p'), ('    ', 'b'), ('B. expect (期待)', 'p'),
        ('    ', 'b'), ('C. accomplish (完成/实现) ★', 'ru'), ('    ', 'b'), ('D. undertake (承担)', 'p')], kind='b')
b.green('思路精析：宾语是 major life events（结婚、生子等重大人生事件），与 at a later age 搭配表“实现这些人生大事的年龄推迟”。encounter 侧重偶然“遇到”，undertake 侧重“着手、承担”，均不合语境。')

b.rich([('Given that we are living longer, switching ', 'n'),
        ('27 D. careers', 'r'),
        (' more often, and seeking more meaning in our work, it makes sense for more people to “bloom” later in life.', 'n')], indent=True, kind='n')
b.rich([('【第 27 题】 ', 'b'), ('A. routines (日常惯例)', 'p'), ('    ', 'b'), ('B. locations (地点)', 'p'),
        ('    ', 'b'), ('C. identities (身份)', 'p'), ('    ', 'b'), ('D. careers (职业) ★', 'ru')], kind='b')
b.green('思路精析：与 living longer、seeking more meaning in our work 并列，谈的是人生节奏的变化；switch careers（转行）为常见搭配，且与 work 同属一个语义场。')

b.rich([('And as they do, the stigma (污名) of succeeding at an older age—including the idea that it is more surprising than doing so young—has become an outdated view of age and achievement. The concept of late bloomers can also be toxic to those who do succeed later in life. Such people may ', 'n'),
        ('28 D. struggle', 'r'),
        (' with feelings of failure, negative self-comparison to others, and even the sense that they have been forgotten.', 'n')], kind='n')
b.rich([('【第 28 题】 ', 'b'), ('A. interfere (干涉)', 'p'), ('    ', 'b'), ('B. correspond (通信/相符)', 'p'),
        ('    ', 'b'), ('C. cope (应对)', 'p'), ('    ', 'b'), ('D. struggle (挣扎/苦于) ★', 'ru')], kind='b')
b.green('思路精析：struggle with 意为“与……苦苦纠缠”，与 feelings of failure、negative self-comparison、have been forgotten 三处负面情绪一致。cope with 虽也译“应对”，但隐含“成功应对”，与 toxic（有害）的语境不合。')

b.rich([('Removing the pressure to succeed within a given timeline is good for our mental health. It can also enable the people we currently label “late bloomers” to ', 'n'),
        ('29 B. enjoy', 'r'),
        (' the distinct successes that come with the achievements that are made later in life.', 'n')], indent=True, kind='n')
b.rich([('【第 29 题】 ', 'b'), ('A. obtain (获得)', 'p'), ('    ', 'b'), ('B. enjoy (享受/享有) ★', 'ru'),
        ('    ', 'b'), ('C. secure (确保/取得)', 'p'), ('    ', 'b'), ('D. witness (目睹)', 'p')], kind='b')
b.green('思路精析：enable sb to enjoy the distinct successes 意为“使某人得以享有这些独特的成功”。witness 的主语应为人“目睹（事件）”，obtain/secure 侧重“取得”具体之物，均不如 enjoy 贴合“享受成果”之意。')

b.rich([('Many of these strengths and skills are a direct result of spending more time on self-discovery, learning and even failure. “Late bloomers may have faced ', 'n'),
        ('30 A. additional', 'r'),
        (' challenges on their pathway to achievement, leading them then to develop more resilience (适应力),” says Chia-Jun Tsay, an associate professor at University College London.', 'n')], kind='n')
b.rich([('【第 30 题】 ', 'b'), ('A. additional (额外的) ★', 'ru'), ('    ', 'b'), ('B. emotional (情感的)', 'p'),
        ('    ', 'b'), ('C. intentional (有意的)', 'p'), ('    ', 'b'), ('D. optional (可选的)', 'p')], kind='b')
b.green('思路精析：与 leading them then to develop more resilience 构成因果——正因为多经历了“额外的”挑战，才练就更强的韧性；下句 difficult circumstances 亦与之呼应。')

b.rich([('“Such people may be more ', 'n'),
        ('31 C. prepared', 'r'),
        (' to adapt to difficult circumstances.”', 'n')], kind='n')
b.rich([('【第 31 题】 ', 'b'), ('A. entitled (有资格的)', 'p'), ('    ', 'b'), ('B. tempted (想要/受诱惑的)', 'p'),
        ('    ', 'b'), ('C. prepared (有准备的/乐于的) ★', 'ru'), ('    ', 'b'), ('D. qualified (合格的)', 'p')], kind='b')
b.green('思路精析：be prepared to do sth 意为“准备好做某事/乐于做某事”，与 adapt to difficult circumstances 搭配自然。be qualified to 后多接职位类动词，entitled to 侧重“有权”，tempted to 侧重“受诱惑”，均不合。')

b.rich([('Beyond increased ', 'n'),
        ('32 B. flexibility', 'r'),
        (', a longer road to success also brings opportunities to discover and cultivate meaningful values and passions that are personally resonant (引起共鸣的), rather than what society pushes us towards.', 'n')], kind='n')
b.rich([('【第 32 题】 ', 'b'), ('A. accessibility (可及性)', 'p'), ('    ', 'b'), ('B. flexibility (灵活性) ★', 'ru'),
        ('    ', 'b'), ('C. productivity (生产力)', 'p'), ('    ', 'b'), ('D. sensibility (感受力)', 'p')], kind='b')
b.green('思路精析：Beyond increased flexibility 承接上句“更善于适应困境”，adapt 的核心即“灵活变通”；且与本段后文“发现自己真正认同的价值与热爱”的“可变、可塑”语义一致。')

b.rich([('Clearly, we are ', 'n'),
        ('33 C. due', 'r'),
        (' for a shift in how we view achievements in terms of age. We simply can’t afford to maintain a bias that leads to ', 'n'),
        ('34 B. overlooking', 'r'),
        (' a whole band of the population’s untapped (未开发的) potential.', 'n')], indent=True, kind='n')
b.rich([('【第 33 题】 ', 'b'), ('A. grateful (感激的)', 'p'), ('    ', 'b'), ('B. renowned (著名的)', 'p'),
        ('    ', 'b'), ('C. due (应得的/到期的) ★', 'ru'), ('    ', 'b'), ('D. answerable (有责任的)', 'p')], kind='b')
b.green('思路精析：be due for sth 意为“该有、理应得到”，we are due for a shift 意为“我们理应转变看法”；下句 We simply can’t afford to maintain a bias 进一步说明这种转变的必要性。')
b.rich([('【第 34 题】 ', 'b'), ('A. comprising (由……组成)', 'p'), ('    ', 'b'), ('B. overlooking (忽视/漏看) ★', 'ru'),
        ('    ', 'b'), ('C. realizing (实现/意识到)', 'p'), ('    ', 'b'), ('D. sacrificing (牺牲)', 'p')], kind='b')
b.green('思路精析：a bias that leads to overlooking… potential 意为“一种导致忽视整整一群人未被开发潜能的偏见”。overlook 与 untapped potential 搭配，强调“看不见”而非“牺牲”；comprising 与句意无关。')

b.rich([('Shafrir learned this lesson in her own time. However, she hopes that future generations will be ', 'n'),
        ('35 D. spared', 'r'),
        (' from the age-related achievement pressure she faced—particularly as a woman.', 'n')], kind='n')
b.rich([('【第 35 题】 ', 'b'), ('A. benefited (受益)', 'p'), ('    ', 'b'), ('B. drawn (被吸引)', 'p'),
        ('    ', 'b'), ('C. received (收到)', 'p'), ('    ', 'b'), ('D. spared (免于/免受) ★', 'ru')], kind='b')
b.green('思路精析：spare sb from sth 意为“使某人免于某事”，此处为被动语态 be spared from the… pressure，意为“希望后代不必再承受这种与年龄相关的成就压力”，与上文 Removing the pressure to succeed 呼应。')

# ---------- Section B ----------
b.h2('Section B (30分) 阅读理解')
b.quick('【本节答案速查】 Passage (A): 36-39 B A B D    Passage (B): 40-42 B C A    Passage (C): 43-46 B C D A')
b.dir('Directions: Read the following passages. Each passage is followed by several questions or unfinished statements. For each of them there are four choices marked A, B, C and D. Choose the one that fits best according to the information given in the passage.')

# (A)
b.rich([('(A)', 'pt')], align='center', kind='pt')
b.pt('Rest in the Present')

b.rich([('Last summer, I was suffering from too much stress. I had just graduated from a challenging doctoral program and was exhausted from the years of research. My wife and I took a vacation after graduation to celebrate, but ', 'n'),
        ('the academic intensity had become a habit and my brain couldn’t seem to shut off.', 'b'),
        (' [36B 学业强度已成习惯，大脑关不掉]', 'gb')], indent=True)
b.rich([('We vacationed on Mackinac Island in Michigan, where the pace of life slows considerably. Ordinarily, the clip-clop (咔哒声) of horses, the lack of cars and the old shops would have relaxed me, but I could not slow down—I was too tired, and distracted.', 'n')], indent=True)
b.rich([('We took a day away from the crowds and sat on the beautiful back lawn of our hotel. I had my phone with me to look at e-mails and then put it down. I needed to relax, but why couldn’t I? My lovely wife sat next to me on a sofa. I had a cool glass of lemonade to enjoy. A breeze stirred up whitecaps (白浪) on the lake. Yet my shoulders were tense, raised up to my ears, and I could not put them down.', 'n')], indent=True)
b.rich([('A dragonfly buzzed around us. Those creatures are special to me because they are a symbol of living in the present: they live most of their lives underwater as larvae (幼虫) and emerge with only months ahead to enjoy a colorful adulthood. ', 'n'),
        ('This one’s brightly colored wings reminded me of the dragonfly tattooed on my wife’s right ankle.', 'b'),
        (' [37A 彩色翅膀→妻子脚踝的蜻蜓纹身]', 'gb'),
        (' Then, the dragonfly came to rest on a piece of grass in front of me.', 'n')], indent=True)
b.rich([('I needed to slow down, I thought, to take inspiration from the persistent wind of life and just relax, if only for a short while. I looked out over the bridge, gazed at the clouds and took a deep breath. Maybe I could slow down. I turned to my wife to tell her about my realization when I felt a touch on my leg. I looked down and saw colorful wings—the dragonfly stopped on my right ankle in the exact position of my wife’s tattoo.', 'n')], indent=True)
b.rich([('I could have sworn that dragonfly looked at me and communicated. “It’s not a matter of relaxing,” it seemed to say. “It’s a matter of appreciating the now. ', 'n'),
        ('Life is so fleeting.', 'b'),
        (' [38B fleeting = 短暂的]', 'gb'),
        (' Be here in the moment and let the future take care of itself.”', 'n')], indent=True)
b.rich([('Suddenly, I could appreciate what was here now and let that appreciation guide me into a sense of peace, and I felt my shoulders descend to their normal place. The dragonfly seemed satisfied that its message had been delivered so it sprang off my ankle and flew away. I decided not to tell my wife about the experience because I needed to let it sit for a while so it could sink in.', 'n')], indent=True)
b.rich([('Months later, I finally told my wife about it and added that I wanted to get my first and only tattoo—a dragonfly on my right ankle. I have it now, and every time I see it, I take a breath and smile. ', 'n'),
        ('It says, “Just live in the present.”', 'b'),
        (' [39D 主旨：珍惜当下，而非忧虑未来]', 'gb')], indent=True)


def read_q(num, stem, opts, ana):
    b.rich([('%d. %s' % (num, stem), 'b')], kind='b')
    ok = [o for o in opts if o[2]]
    bad = [o for o in opts if not o[2]]
    for letter, text, _ in ok:
        b.rich([('%s. %s' % (letter, text), 'ru'), ('  [正确答案]', 'ru')], kind='b')
    for letter, text, _ in bad:
        b.rich([('%s. %s' % (letter, text), 'p')], kind='p')
    b.green('【解析定位】 ' + ana)


read_q(36, 'Why couldn’t the author relax during the vacation on Mackinac Island?', [
    ('A', 'The noisy clip-clop of horses and old shops disturbed his rest.', False),
    ('B', 'He was still used to the stress of academic research.', True),
    ('C', 'He kept checking e-mails on his phone throughout the trip.', False),
    ('D', 'The strong lake breeze made his shoulders physically tense.', False)],
    '细节理解题。定位第1段末句 “the academic intensity had become a habit and my brain couldn’t seem to shut off”——博士阶段的学术强度已经变成习惯，大脑关不掉。A 与原文相反（马啼声、老店原本会让他放松）；C 原文只说“把手机拿起来看了一眼又放下”，并非全程刷邮件；D 张冠李戴，肩膀紧绷是压力所致，不是湖风造成。故选 B。')

read_q(37, 'What did the author notice about the dragonfly before it landed on him?', [
    ('A', 'Its bright wings looked like his wife’s ankle tattoo.', True),
    ('B', 'It buzzed among the crowds of tourists on the hotel lawn.', False),
    ('C', 'It had spent most of its life living underwater as larvae.', False),
    ('D', 'It rested on the lake-side grass to escape the strong lake wind.', False)],
    '细节理解题。定位第4段 “This one’s brightly colored wings reminded me of the dragonfly tattooed on my wife’s right ankle.”——蜻蜓落在他身上之前，他先注意到它鲜艳的翅膀，并由此想到妻子脚踝上的蜻蜓纹身。B 原文是“远离人群”（took a day away from the crowds）；C 是蜻蜓的生物学常识，不是“落在身上之前注意到的特征”；D 原文只说它停在他面前的草地上，未提“躲风”。故选 A。')

read_q(38, 'What does the underlined word “fleeting” in Paragraph 6 most probably mean?', [
    ('A', 'Meaningful and truly unforgettable forever.', False),
    ('B', 'Lasting for a very short period of time.', True),
    ('C', 'Boring and extremely tiring to experience.', False),
    ('D', 'Colorful and visually attractive to the eyes.', False)],
    '词义猜测题。定位第6段 “Life is so fleeting. Be here in the moment and let the future take care of itself.”——正因生命“转瞬即逝”，才要活在当下、让未来自己照顾自己。上下文（蜻蜓成虫只余数月、appreciating the now）均指向“短暂”。故选 B。')

read_q(39, 'What is the main message the author wants to convey through this story?', [
    ('A', 'Hard-working scholars need to escape academic pressure via island vacations.', False),
    ('B', 'Dragonflies are the perfect symbol for people suffering long-term mental stress.', False),
    ('C', 'Tattoos serve as the best reminder for people’s important life-changing experiences.', False),
    ('D', 'We ought to value the present moment rather than worry about the future.', True)],
    '主旨大意题。蜻蜓的话 “It’s a matter of appreciating the now… Be here in the moment and let the future take care of itself.” 与结尾 “Just live in the present.” 两次点题，是全文主旨。A、B、C 都只抓住文中某个局部细节（海岛度假、蜻蜓象征、纹身），属于以偏概全。故选 D。')

# (B)
b.rich([('(B)', 'pt')], align='center', kind='pt')
b.pt('AquaExplorer X1: Your Personal Underwater Drone')
b.rich([('Price: 99    Cable length: 18 ft (5.5m) or 8.5 ft (2.6m)    Quantity: 1', 'n'),
        (' [42A 三项可选参数＝电商下单页]', 'gb')], kind='n')
b.rich([('Description', 'b')], kind='b')
b.rich([('Explore the depths, effortlessly. The AquaExplorer X1 provides a fully immersive underwater viewing experience for both hobbyists and professionals. Unlike traditional diving gear, this compact drone allows for versatile exploration, including ship hull inspections, underwater photography, and marine life observation.', 'n')], indent=True)
b.rich([('Monitor your dive duration with the app and receive real-time alerts when the battery level is low. Wireless connectivity enables live streaming and seamless integration with your smartphone. AquaExplorer X1 offers the best companion for underwater adventures.', 'n')], indent=True)
b.rich([('Durable ABS or aluminum alloy cable options are available. See “Choosing Location” for insight on what environment works best for your underwater mission.', 'n'),
        (' [41C 线缆材质可选，按使用环境选]', 'gb')], indent=True)
b.rich([('Features', 'b')], kind='b')
for line in ['Up to 4K Ultra HD camera with 150°wide-angle lens',
             'Built-in 1000-lumen LED lights for dark environments',
             'Up to 2 hours of continuous operation on a single charge',
             'Maximum diving depth of 100 meters',
             'Compatible with both iOS and Android devices',
             'Two powerful motors for stable movement in strong currents',
             'Wireless range of up to 50 meters (line of sight)',
             'Sleek orange or navy blue finish',
             'Built-in GPS for surface positioning']:
    b.rich([('• ' + line, 'n')], kind='n')
b.rich([('Choosing Location', 'b')], kind='b')
b.rich([('Deploy AquaExplorer X1 in a location that allows clear visibility and calm currents.', 'n')], indent=True)
b.rich([('• Orange finish: Recommended for freshwater lakes and swimming pools.', 'n')], kind='n')
b.rich([('• Navy blue finish: Recommended for deep-sea exploration and marine environments.', 'n')], kind='n')
b.rich([('Installation Guidance', 'b')], kind='b')
b.rich([('AquaExplorer X1 must be paired with its dedicated app by a registered user. Visit our official support page to download the manual. If needed, detailed video tutorials are available online.', 'n')], indent=True)

read_q(40, 'Which of the following is NOT a feature of the AquaExplorer X1?', [
    ('A', 'It has 50-meter line-of-sight wireless range and supports Android.', False),
    ('B', 'It has motors for strong currents and GPS for underwater positioning.', True),
    ('C', 'It provides 2-hour runtime and a 4K Ultra-HD wide-angle camera.', False),
    ('D', 'It is iOS-compatible and equipped with built-in LED lights.', False)],
    '细节理解题（否定型）。逐条比对 Features 列表：A 对应 “Wireless range of up to 50 meters (line of sight)” 与 “Compatible with both iOS and Android devices”；C 对应 “Up to 2 hours” 与 “4K Ultra HD camera with 150°wide-angle lens”；D 对应 “Compatible with both iOS…” 与 “Built-in 1000-lumen LED lights”。唯有 B 中 GPS 的功能被偷换——原文是 “Built-in GPS for surface positioning（水面定位）”，而非水下定位。故选 B。')

read_q(41, 'What can we learn from the passage?', [
    ('A', 'Its two powerful motors guarantee stable movement at its maximum diving depth.', False),
    ('B', 'The orange model is made for deep-sea exploration and marine environments.', False),
    ('C', 'Buyers may choose ABS or aluminum alloy cables for their diving location.', True),
    ('D', 'The dedicated app must be installed and paired before watching tutorials.', False)],
    '细节理解题。定位 “Durable ABS or aluminum alloy cable options are available. See ‘Choosing Location’ for insight on what environment works best for your underwater mission.”——线缆有 ABS 与铝合金两种可选，具体按使用环境定，C 正确。A 过度推断，原文只说电机“在强水流中保持稳定”，未承诺在最大潜深仍稳定；B 张冠李戴，橙色款用于淡水湖泊与泳池，深海军蓝款才用于深海；D 因果倒置，原文是先配对 App，教程是“如有需要可在线观看”，并非配对后才能看。故选 C。')

read_q(42, 'Where can you most probably find this page?', [
    ('A', 'On an e-commerce site where buyers select cable length and quantity.', True),
    ('B', 'In a printed user manual placed inside the retail box of the AquaExplorer X1.', False),
    ('C', 'On the official website of the drone manufacturer’s support section.', False),
    ('D', 'In a consumer tech magazine reviewing the latest underwater drones.', False)],
    '推理判断题（出处判断）。页面首行给出 “Price: 99 / Cable length: … or … / Quantity: 1”，这三项正是下单时买家需要勾选的规格与数量，属于电商商品页的典型要素；再结合 “See ‘Choosing Location’”“Visit our official support page” 这类导购式指引，可判定为电商页面。B 说明书不会标价与购买数量；C 支持页面不会有“Price/Quantity”；D 杂志评测不会出现“Quantity: 1”这种下单字段。故选 A。')

# (C)
b.rich([('(C)', 'pt')], align='center', kind='pt')
b.rich([('It’s fashionable to talk about ideas as if they were diseases. Some pop songs are infectious, and some products are contagious. To that end, advertisers and song producers have developed a theory of “viral” marketing, which assumes that ', 'n'),
        ('a great idea is self-distributing, and word of mouth can take a little thing and turn it into a phenomenon.', 'b'),
        (' [43B 病毒式传播＝网民自发转发的“小东西”]', 'gb'),
        (' But do ideas and products really go viral?', 'n')], indent=True)
b.rich([('Not really. A few years ago, several researchers studied the spread of millions of messages on a social media app. More than 90 percent of the messages didn’t spread at all. A tiny percentage, about 1 percent, was shared more than seven times. But nothing really went fully viral—not even the most popular shared messages. Around 95 percent of the news that people see on the social media app comes directly from its original source.', 'n')], indent=True)
b.rich([('In other words, popularity on the Internet is mostly driven, not by a million one-to-one shares, but rather by a handful of one-to-one-million outputs. These are what I call “dark broadcasters”: ', 'n'),
        ('critical, but often hidden, outputs inside the information chain which are responsible for broadcasting a piece of content to many people at once', 'b'),
        (', a fraction of whom might pass it on. [44C 暗广播者决定什么内容成为爆款]', 'gb')], indent=True)
b.rich([('The information chain leads to a more reasonable definition of the word “viral.” Popularity is still driven by broadcasts—by publishers, celebrities, and other broadcasters who can reach thousands or even millions of people at once.', 'n')], indent=True)
b.rich([('Seeing beyond the viral myth has important implications for media literacy at a time when people are concerned about fake news. As confidence in traditional news outlets has declined, people have moved their trust to peers and social networks. But they must be careful not to mistake popularity for truth. ', 'n'),
        ('That which would seem to go viral due to its inherent truth or interestingness is typically pushed by broadcasters with hidden motives', 'b'),
        (', because such content seems uplifting. [45D 热门≠真实或有趣]', 'gb')], indent=True)
b.rich([('It promises small-time writers, photographers, and videographers that a moment’s inspiration can transform into sudden fame. It holds up the Internet as a perfect democracy, where anybody can become a star at a moment’s notice if they make something good enough. But in the end, ', 'n'),
        ('the viral myth is a dragon-gate-leap tale (a Chinese legend of ordinary people gaining instant fame) hiding the fact that the Internet is still run by powerful giants.', 'b'),
        (' [46A 病毒神话给人“一夜成名”的虚假希望]', 'gb')], indent=True)

read_q(43, 'Which of the following statements demonstrates the phenomenon of going viral according to the “viral” marketing theory?', [
    ('A', 'A product recommended by a celebrity becomes known to everyone.', False),
    ('B', 'A funny video is shared a million times among common netizens.', True),
    ('C', 'A new theory of marketing impresses and is adopted by a big firm.', False),
    ('D', 'A groundbreaking idea is well received at an academic conference.', False)],
    '细节理解题（概念判断）。题干限定“根据 viral marketing 理论”，该理论的核心是 “a great idea is self-distributing, and word of mouth can take a little thing and turn it into a phenomenon”——靠普通人口口相传把小东西变成现象，B（一段搞笑视频被普通网民转发百万次）正合此义。A 是名人推荐，属“广播式”传播，恰是作者在第三段要反驳的对象；C、D 都发生在小范围专业场合，谈不上“自传播”。故选 B。')

read_q(44, 'Which of the following statements about “dark broadcasters” is true?', [
    ('A', 'They are critical of and responsible for the content they broadcast.', False),
    ('B', 'They are able to convince content receivers to pass on information.', False),
    ('C', 'They play a vital role in determining what becomes a hit.', True),
    ('D', 'They compete with traditional broadcasters for online shares.', False)],
    '细节理解题。定位第3段对 dark broadcasters 的定义：critical, but often hidden, outputs… responsible for broadcasting a piece of content to many people at once——他们是“关键却常被隐藏的”传播节点，负责把内容一次性推给大量受众，因而对“什么内容会火”起决定作用，C 正确。A 曲解 critical（此处意为“关键的”，不是“批评的”）；B 原文只说其中一小部分人会转发（a fraction of whom might pass it on），并未说他们“能说服受众转发”；D 文中无此对比。故选 C。')

read_q(45, 'What does the author mean by saying “be careful not to mistake popularity for truth” in paragraph 5?', [
    ('A', 'People should only trust news released by authoritative traditional media.', False),
    ('B', 'People must not confuse selfish motives with the pursuit of truth.', False),
    ('C', 'People must be able to tell traditional media from social networks.', False),
    ('D', 'People must be aware what is popular may not be true or interesting.', True)],
    '句意理解题。定位第5段紧接其后的解释：“That which would seem to go viral due to its inherent truth or interestingness is typically pushed by broadcasters with hidden motives”——那些看起来因“真实或有趣”而走红的内容，往往是背后有隐藏动机的传播者推出来的。可见作者提醒的是：热不等于真，也不等于真有趣，D 正确。A 过于绝对，作者只说人们对传统媒体的信任下降，并未主张“只信传统媒体”；B 偷换概念，selfish motives 是“传播者的动机”，不是读者要区分的东西；C 只是文中提及的现象，不是该句含义。故选 D。')

read_q(46, 'Why is the viral myth difficult to cope with?', [
    ('A', 'Because it gives people false hope of sudden success.', True),
    ('B', 'Because it helps make the Internet a democratic place.', False),
    ('C', 'Because it promises the creation of inspirational works.', False),
    ('D', 'Because it reveals the dominant force on the Internet.', False)],
    '推理判断题。定位末段：病毒神话向小写手、摄影师、视频作者许诺 “a moment’s inspiration can transform into sudden fame”，把互联网描绘成人人可一夜成名的“完美民主”，而 “hiding the fact that the Internet is still run by powerful giants”——正因为它许下“一夜成名”的虚假希望、又掩盖了平台巨头垄断的现实，才难以破除，A 正确。B、C 都是神话“宣称”的内容，不是“难以应对”的原因；D 与原文相反，神话恰恰是“掩盖”而非“揭示”巨头的主导地位。故选 A。')

# ---------- Section C ----------
b.h2('Section C (10分) 六选四阅读填空')
b.quick('【本节答案速查】 47-50: C A D F    [干扰项：B、E]')
b.dir('Directions: Complete the following passage by using the sentences given below. Each sentence can be used only once. Note that there are two more sentences than you need.')
b.label('【选项池解析与标注】')
opt_c = [
    ('A', 'Yet a summer storm can undo weeks of clear test results.', '然而一场夏季暴雨就能让数周清澈的检测结果前功尽弃。', True, '对应48空。Yet 转折，与上段“巴黎、伦敦投入巨资治污、河水看似可游”形成反差；a summer storm 引出下段“暴雨后 24–72 小时不宜下水”。'),
    ('B', 'Designated swimming areas are often the safest choice.', '划定的游泳区域通常是最安全的选择。', False, '【干扰项】属于“给游泳者的建议”，与本段“河流治污投入”话题不衔接，且下文并未展开“划定区域”。'),
    ('C', 'But health authorities regularly issue warnings about pollution in lakes and rivers.', '但卫生主管部门经常就湖泊与河流的污染发布警告。', True, '对应47空。But 转折承接上句“接触自然水体有益心理健康”；同时 warnings 是下段 “Despite these warnings” 的直接照应。'),
    ('D', 'They are at higher risk than adults because they swallow more water while swimming.', '他们的风险高于成年人，因为游泳时会吞下更多的水。', True, '对应49空。空格前一句已出现 children facing the greatest danger，They 指代 children；because 从句解释“为何风险更高”。'),
    ('E', 'Mental benefits outweigh physical risks for some swimmers.', '对部分游泳者而言，心理益处大于身体风险。', False, '【干扰项】与第1段“心理益处”重复，但本段已转向“风险与疾病”，放回原处会造成语义回环。'),
    ('F', 'The reality is more complicated, especially for rivers.', '现实情况要复杂得多，河流尤其如此。', True, '对应50空。承接上句“泳客以为官方检测能覆盖大部分风险”，下文随即说明现行监测只适合“长期趋势、稳定海岸”，故现实“更复杂”。'),
]
for L, en, zh, ok, note in opt_c:
    b.rich([('[%s] %s' % (L, en), 'ru' if ok else 'p'),
            ('     译文：' + zh, 't333'),
            ('     备课精注：' + note, 'g')], kind='n')

b.pt('Open water swimming is booming, but is it bad for your health?')
b.rich([('Open-water swimming, also known as wild swimming, has boomed in countries from the UK and the US to Australia in the past decade, fuelled by social media and urban “blue space” campaigns. Studies suggest that spending time in natural water is associated with better mental health. ', 'n'),
        ('47 【C】 But health authorities regularly issue warnings about pollution in lakes and rivers. （但卫生主管部门经常就湖泊与河流的污染发布警告）', 'r'),
        ('  【备课衔接：47空位于第1段段末。前句讲“自然水体有益心理健康”，本句用 But 转出“污染警告”，下段开头 Despite these warnings 直接回指，环环相扣。】', 'g')], indent=True)
b.rich([('Despite these warnings, rivers, once treated as open sewers, are now increasingly seen as ‘clean and swimmable’. Paris has invested about €1.4bn in cleaning up the Seine, building a vast underground basin at Austerlitz that can hold about 50,000 cubic metres of stormwater. London’s Tideway “super sewer” can store around 1.6 million cubic metres of combined sewage and rainwater before sending it for treatment. ', 'n'),
        ('48 【A】 Yet a summer storm can undo weeks of clear test results. （然而一场夏季暴雨就能让数周清澈的检测结果前功尽弃）', 'r'),
        ('  【备课衔接：48空位于第2段段末。前面用巴黎、伦敦的巨额投入说明“河水变清”，Yet 一转，指出暴雨会毁掉一切，正好引出第3段“暴雨后 24–72 小时不宜游泳”。】', 'g')], indent=True)
b.rich([('Studies on wild swimming show a consistent pattern: the more contact people have with the water, the higher the risk of gastrointestinal illness, with children facing the greatest danger. ', 'n'),
        ('49 【D】 They are at higher risk than adults because they swallow more water while swimming. （他们的风险高于成年人，因为游泳时会吞下更多的水）', 'r'),
        ('  【备课衔接：49空紧随“with children facing the greatest danger”，They 只能指 children；because 从句解释“为何风险更高”，后句另起 Leptospirosis（钩端螺旋体病）补充另一种风险，层次清楚。】', 'g')], indent=True)
b.rich([('Many swimmers assume that official tests will capture most of these risks. ', 'n'),
        ('50 【F】 The reality is more complicated, especially for rivers. （现实情况要复杂得多，河流尤其如此）', 'r'),
        ('  The current approach to monitoring is designed to track longer-term trends, and works best at stable coastal sites. It’s less useful for on-the-spot decisions, because short pollution events can be missed by routine sampling.  【备课衔接：50空后紧接“现行监测面向长期趋势、适合稳定的海岸站点”，正是在解释“为什么现实更复杂、河流尤其如此”，F 与下文构成“总—分”关系。】', 'g')], indent=True)
b.rich([('In short, alerts help, but they don’t replace making a personal judgement. The pleasures of wild swimming are best preserved when enthusiasm is matched by caution, timing and local knowledge.', 'n')], indent=True)

# ============ 第II卷 ============
b.h1('第II卷')
b.h2('IV. Grammar (10分) 语法填空')
b.quick('【本节答案速查】 51. when    52. to    53. is favored    54. the reason    55. have adopted    56. demanding    57. making    58. until    59. incorporated    60. What')
b.dir('Directions: After reading the passage below, fill in the blanks to make the passage coherent and grammatically correct. For the blanks with a given word, fill in each blank with the proper form of the given word; for the other blanks, use one word that best fits each blank.')
b.pt('Standing Out and Fitting In')

b.rich([('I have always thought that if you can survive high school, you can survive anything. It is the time in a young person’s life ', 'n'),
        ('(51) when', 'r'),
        (' 【定语从句。先行词 the time 表时间，从句 they not only are faced with… but also have to deal with… 结构完整，缺时间状语，故用关系副词 when（＝in which）。】', 'g'),
        (' they not only are faced with the mounting pressures of school, but also have to deal with their own physical and mental development as they navigate the rocky paths of personal self-discovery.', 'n')], indent=True)
b.rich([('It is a difficult time when they want to stand out and show their stuff while hoping to be able to find a place where they can fit in, ', 'n'),
        ('(52) to', 'r'),
        (' 【不定式作同位说明。to fit in with both their peers and society 是对前文 a place where they can fit in 的具体化，用不定式表“即……”，与 fit in with 构成固定搭配。】', 'g'),
        (' fit in with both their peers and society.', 'n')], indent=True)
b.rich([('This problem of “standing out” and “fitting in” can be especially difficult in China which is, as sociologists call it, a “high-context” society. In a nutshell, a high-context society is one in which the group ', 'n'),
        ('(53) is favored (favor)', 'r'),
        (' 【被动语态＋主谓一致。the group 与 favor 之间是被动关系（群体被优先于个体），主语 the group 视为单数，故用 is favored；over the individual 提示 favor A over B 的被动式。】', 'g'),
        (' over the individual as a result of a great many unwritten social rules and understandings. It is a kind of code that people learn to adopt as they grow up in that culture. A “low-context” society, on the other hand, prioritizes the individual over the group, which encourages people to be specific in their social interactions. This is probably ', 'n'),
        ('(54) the reason', 'r'),
        (' 【名词短语。This is probably the reason why… 意为“这大概就是……的原因”，why 引导定语从句修饰 the reason；用定冠词 the 特指上文所述原因。】', 'g'),
        (' why Western societies, most of which are multi-cultural, are known for being plain-spoken.', 'n')], indent=True)
b.rich([('Does this mean that Chinese society is too conformist? I don’t think so. Western societies ', 'n'),
        ('(55) have adopted (adopt)', 'r'),
        (' 【现在完成时。句意“西方社会已把 diversity 一词奉为座右铭”，adopt 的动作已完成并对现在产生影响，主语为复数，故用 have adopted。】', 'g'),
        (' the word “diversity” as their motto. This has led to certain individuals and small groups within these respective societies ', 'n'),
        ('(56) demanding (demand)', 'r'),
        (' 【现在分词作宾语补足语。lead sb to do 的被动/变体结构 lead to sb doing sth 中，sb 与 demand 为主动关系，故用现在分词 demanding；后接 that 从句用虚拟语气 be conferred。】', 'g'),
        (' that special rights and social status be conferred upon them, which has gone on to create a significant amount of social chaos. China’s high-context society, however, provides a solid basis wherein individuals can express their personalities while still ', 'n'),
        ('(57) making (make)', 'r'),
        (' 【现在分词。while still 后接分词作伴随状语，主语 individuals 与 make 为主动关系；与前文 can express their personalities 并列，保持形式一致。】', 'g'),
        (' positive contributions to society.', 'n')], indent=True)
b.rich([('The Eight Eccentrics were Chinese artists who, in the middle of the Qing dynasty, altered the traditions of ink brush painting through their broad brush strokes and use of bright colours. They were “eccentric” because they were not trained artists who painted in the traditional way. For instance, Jin Nong, one of the most famous painters in the group, was so poor during his childhood that he did not start painting ', 'n'),
        ('(58) until', 'r'),
        (' 【固定结构。not… until… 意为“直到……才……”，与前面的 so poor 呼应：因为太穷，直到五十多岁才开始作画。】', 'g'),
        (' he was more than fifty years old. Eccentric though they may have been, Jin and the other seven artists would over time become ', 'n'),
        ('(59) incorporated (incorporate)', 'r'),
        (' 【过去分词作表语。become incorporated into 意为“被并入、融入”，主语 Jin and the other seven artists 与 incorporate 是被动关系，故用过去分词。】', 'g'),
        (' into Chinese culture and would go on to have significant influence over more modern painters such as Qi Baishi.', 'n')], indent=True)
b.rich([('Being a little different and “standing out” — whether it’s you or someone else — is not necessarily a bad thing. ', 'n'),
        ('(60) What', 'r'),
        (' 【主语从句。What is important is that… 中 What 引导主语从句并在从句中作主语，指“重要的（事情）”，不能用 That（that 只起连接作用，不充当成分）。】', 'g'),
        (' is important is that we tolerate these differences and remember that, in this big country and big world, we all belong and we all “fit in.”', 'n')], indent=True)

# ---------- V. Summary ----------
b.h2('V. Summary Writing (10分) 概要写作')
b.quick('【本节答案速查】 61. 见下方官方参考范文（约 51 词）')
b.rich([('61. Directions: Read the following passage. Summarize the main idea and the main point(s) of the passage in no more than 60 words. Use your own words as far as possible.', 'b')], kind='b')
b.pt('A Wise Way to Make Families Rules')
b.rich([('All groups, of whatever size or nature, need standard operating procedures. Without them, groups may very well fall into confusion, chaos and conflict. The functions that rules can serve are indispensable. When it comes to parenting, making rules can make a big difference in our family as well. Actually, the issue is not whether our families need rules. We do need them. The real issue is how to motivate all family members to comply with (遵守) them.', 'n')], indent=True)
b.rich([('At some time in our lives we all have felt unmotivated to comply with some rule or policy that we had no voice in making. Denied the opportunity to participate in establishing a rule, most people feel imposed upon and resentful of the new rule. But when people actively participate in setting a rule or making a decision that will affect them, they are more highly motivated to comply with it. We call this the Principle of Participation, and it has proven its effectiveness in families as well.', 'n')], indent=True)
b.rich([('When children are given the opportunity to participate in setting rules or making decisions that will affect them, several good things happen. Children feel better about themselves — having more self-esteem (自尊心) and self-confidence. Such a good effect is due to their feeling that they have gained more “fate control” over their own lives. They also feel they are equal members of the family with an equal voice in making decisions and establishing rules — they’re part of a team, not second-class citizens. This means that families that function collaboratively and democratically will have closer and warmer relationships than those in which the adults act as bosses or authorities expecting the children to obey the rules made for them.', 'n')], indent=True)
b.rich([('Another important reason for encouraging the full participation of family members in decision making is that it often produces higher-quality solutions to problems. Two heads (or three, or four) are better than one. Shared decisions will be based not only on the knowledge and experience of the adults but also on those of the children. The admonition (告诫) that father knows best should be challenged now.', 'n')], indent=True)
b.label('【官方参考范文】')
b.rich([('The passage emphasizes the importance of establishing family rules through active participation of all family members, which fosters a sense of self-esteem, self-confidence, and equality among them, leading to a more collaborative and democratic family environment. It also highlights the benefits of collective decision-making in generating higher-quality solutions to family problems.', 'r0')], kind='b')
b.label('【要点提炼与评分维度解析】')
b.green('• 核心论点（Main Idea）：家庭规则本身不可或缺，真正的难题在于如何让全体成员愿意遵守——关键在于“共同参与”。')
b.green('• 支撑细节一（Principle of Participation）：人对自己没参与制定的规则容易抵触；一旦参与制定，遵守的意愿显著提高。')
b.green('• 支撑细节二（对孩子的双重收益）：参与让孩子更有自尊与自信，产生“命运掌控感”，并感到自己是家庭中平等的一员，家庭关系更亲密、更民主。')
b.green('• 支撑细节三（决策质量）：集思广益能得出更高质量的解决方案，“父亲最懂”的告诫应当被质疑。')
b.green('• 语言重组亮点：用 which 引导的非限制性定语从句把“参与—自尊—平等—民主氛围”串成一条因果链（fosters…, leading to…），再用 It also highlights… 另起一层，避免逐句翻译；主动词换成 emphasizes / fosters / highlights，与原句重复度低。')

# ---------- VI. Translation ----------
b.h2('VI. Translation (15分) 翻译')
b.quick('【本节答案速查】 62-65 见下方参考译文')
b.dir('Directions: Translate the following sentences into English, using the words given in the brackets.')

trans = [
    ('62. 无论机器人是在工厂、农田、医院还是家庭中工作，这一原则都同样适用。(apply)(汉译英)',
     'Whether robots work in factories, farmlands, hospitals or homes, this principle applies equally.',
     None,
     '• 采分点：“无论……还是……”用 whether… or… 引导让步状语从句置于句首（1分）；主句 this principle applies equally 主语与谓语搭配正确（1分）；规定词 apply 用作谓语且与单数主语一致，写 applies（1分）。',
     '• 词汇句法：apply 在此为不及物动词，意为“适用”，常用 apply to sb/sth；equally（同样地）位置灵活，置于句末最自然。易错点：①误用 no matter 后接名词（no matter robots… 不成立，no matter 后须接 wh- 从句）；②主语 this principle 为单数，apply 漏加 -s。'),
    ('63. 每逢周末晚间，居民们在公园南角的湖畔休息区内品茗叙旧，闲话家常。(gather) (汉译英)',
     'Every weekend evening, residents gather in the lakeside rest area at the southern corner of the park to drink tea, reminisce about old times and chat about daily life.',
     None,
     '• 采分点：“每逢周末晚间”译为时间状语 Every weekend evening（1分）；规定词 gather 作谓语，与主语 residents 一致（1分）；地点状语 in the lakeside rest area at the southern corner of the park 层次清楚（1分）；三个并列动作 drink tea / reminisce about old times / chat about daily life 用 to 引导的不定式并列（1分）。',
     '• 词汇句法：reminisce about old times（叙旧）、chat about daily life（闲话家常）为地道搭配；地点状语按“由小到大”顺序排列更符合英语习惯。易错点：①“品茗叙旧，闲话家常”若逐字直译成 drink tea and talk 会丢分；②gather 为不及物动词，不要写成 gather residents。'),
    ('64. 酷热的山地寸草不生，而种满葡萄的山谷却绿意盎然，形成“火”与“绿”交相辉映的独特风貌。(where)(汉译英)',
     'The scorching mountains are totally barren where not even a blade of grass grows, while the valleys planted with grapes are lush with green, forming a unique landscape where “fire” and “green” set each other off beautifully.',
     None,
     '• 采分点：前半句用 where 引导的定语从句 where not even a blade of grass grows 修饰 barren（1分）；while 表对比连接两个分句（1分）；过去分词短语 planted with grapes 作后置定语（1分）；现在分词短语 forming a unique landscape 作结果状语，并再套一个 where 从句（1分）。',
     '• 词汇句法：scorching（酷热的）、barren（贫瘠的/寸草不生的）、lush with green（绿意盎然）、set each other off（交相辉映）为本句得分亮点；not even a blade of grass grows 用否定强化“寸草不生”。易错点：题干规定词 where 需用两次，只写一次会扣分；while 不能换成 when（此处为对比，非时间）。'),
    ('65. 回望王虹一路走来的求学征途，我们终将明白，普娃与天才的终极差距，与其说在于先天智商的高低，不如说在于后天勇气的深浅、坚守的长短和前行的笃定。(so much...as)(汉译英)',
     'Looking back on Wang Hong’s learning journey along the way, we will finally understand that the ultimate gap between ordinary students and geniuses lies not so much in the level of innate IQ as in the depth of acquired courage, the length of perseverance and the determination to move forward.',
     'Looking back on the academic journey Wang Hong has travelled, we will eventually come to see that the ultimate gap between ordinary students and geniuses lies not so much in how high their innate IQ is as in how deep their acquired courage, how long their perseverance and how firm their determination to move forward.',
     '• 采分点：现在分词短语 Looking back on… 作状语（1分）；宾语从句 that the ultimate gap… lies…（1分）；规定结构 not so much in A as in B 使用正确、前后介词一致（1分）；三个并列名词短语 the depth of acquired courage / the length of perseverance / the determination to move forward（1分）。',
     '• 词汇句法：not so much A as B（与其说 A，不如说 B）是本句唯一硬性考点，A、B 须为对称成分；innate IQ（先天智商）对 acquired courage（后天勇气）；perseverance（坚守）、determination（笃定）。易错点：①漏掉 as 后的 in，造成结构失衡；②把“普娃”直译为 poor children（语义错误，应为 ordinary students / average students）。'),
]
for q, ans, alt, pts, wd in trans:
    b.rich([(q, 'b')], kind='b')
    b.rich([('【参考译文】 ', 'ru'), (ans, 'ru')], kind='b')
    if alt:
        b.rich([('【参考译文·替换版】 ', 'ru'), (alt, 'ru')], kind='b')
    b.label('【分值采分点与考点精析】')
    b.green(pts)
    b.green(wd)

# ---------- VII. Guided Writing ----------
b.h2('VII. Guided Writing (25分) 指导写作')
b.rich([('66. Directions: Write an English composition in 120-150 words according to the instructions given below in Chinese.', 'b')], kind='b')
b.label('【原题要求】')
b.rich([('假设你是明启中学高三学生李华。你的英国笔友 Mike 在最近的一封信中向你抱怨他的室友经常不征得他的同意就把他放在冰箱里的食物吃掉。请回一封信，内容包括：1）你对如何处理这个问题的建议；2）你的理由。', 'n')], indent=True)
b.label('【高分参考范文】')
b.rich([('Dear Mike,', 'b')], kind='b')
b.rich([('I’m sorry to hear that your roommate often eats your food kept in the fridge without asking for your permission. It must be really annoying, so I’m writing to offer some practical suggestions.', 'n')], indent=True)
b.rich([('First, I suggest you have a sincere and gentle talk with him. Many people do such things just out of carelessness instead of bad intentions. If you calmly tell him how uncomfortable this makes you feel, he will probably stop doing it. Second, you can label your food with your name and store it in a closed container. The clear mark will remind him to respect your belongings. If he still ignores your words, you can ask your dorm manager for help to solve the conflict properly.', 'n')], indent=True)
b.rich([('Good roommate relationships rely on mutual respect. I hope my advice will help you deal with the problem smoothly.', 'n')], indent=True)
b.rich([('Yours,', 'n')], align='right', kind='n')
b.rich([('Li Hua', 'n')], align='right', kind='n')
b.label('【写作架构与亮点表达赏析】')
b.green('1. 审题立意与行文结构：书信体，三段式。首段“共情＋点明写作目的”——先承认对方处境令人恼火（It must be really annoying），再自然过渡到“我来给几条实用建议”，符合英文书信“先情后理”的惯例；中段按“先软后硬”排列两条建议：先沟通（have a sincere and gentle talk），再设防（label your food / closed container），最后加一层兜底（ask your dorm manager），逻辑层层递进；末段一句点出“室友关系靠相互尊重”收束全文，并附祝愿，格式完整（Dear Mike / Yours, Li Hua）。全文约 139 词，落在 120–150 区间。')
b.green('2. 高分地道词汇与短语：• without asking for your permission（未经你同意）• out of carelessness instead of bad intentions（出于疏忽而非恶意，instead of 对比结构很地道）• label your food with your name（在食物上贴名字标签）• respect your belongings（尊重你的物品）• solve the conflict properly（妥善解决冲突）• rely on mutual respect（依靠相互尊重）')
b.green('3. 句式多样性：① 首段用 so 引导的并列句承接因果（It must be really annoying, so I’m writing to…）；② 中段用 if 引导的条件状语从句两次（If you calmly tell him… / If he still ignores your words…），构成“先礼后兵”的双层假设；③ 用 rather than / instead of 的对比结构替代简单的 but；④ 建议句使用 I suggest you (should) do 的虚拟语气，语气委婉而得体。')

out = '/Users/linquin/WorkBuddy AI/EnglishTeacher-Workspace/生成物/交大附中2026-2027学年高三上第一次调研测试英语（备课讲义版）.docx'
b.save(out)
print('saved:', out)
