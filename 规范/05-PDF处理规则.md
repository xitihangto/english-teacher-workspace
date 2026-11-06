# 05 · PDF 处理规则

> 适用：用户要把做好的 Word 转成 PDF、把几份 PDF 合成一份、把 PDF 拆成图片、或从 PDF 里取原图。
> 这是**输出形态与素材预处理**，不是第五条生产线——讲义 / 批改 / 识别的规则仍在 01 / 02 / 03，本文只管"换个壳"。
> 本文件与 01–04 同属产物规则，改动需口令。

---

## 1. 触发与路由

| 用户说 | 做什么 | 命令 |
|---|---|---|
| 「转成 PDF」「导个 PDF」 | 成品 docx → PDF | `topdf` |
| 「把这两份合成一个」「合并 PDF」 | 多份 PDF 按给定顺序拼一份 | `merge` |
| 「转成图片」「发群用」「做课件」 | 逐页渲染成 PNG | `toimg` |
| 「把里面的图抽出来」 | 抽内嵌位图（不渲染） | `extract` |
| 「这个 PDF 几页」 | 只报页数与内嵌图数量 | `info` |

**不问格式细节**：DPI 默认 200（够投影和打印），页数默认全部；用户没说就用默认值，别列选项让他挑。
**顺序有歧义才问**：合并时若用户没说先后，按文件名里的卷次 / 日期排；排不出来再问一句。

---

## 2. 依赖策略：默认不装，按需装，大头不代劳

**默认状态是什么都不装。** 首次安装只**探测**、不安装，也不记状态文件——
`import pymupdf` 和 `command -v soffice` 都是毫秒级，每次用时现探，比记状态可靠（不会出现"记着装过、实际被删了"）。

判据一句话：**pip 能装且小于 50 MB 的，自动装；需要外部安装包、brew 或 sudo 的，一律不装，只给指引。**

### 2.1 三件小事（合并 / 转图 / 抽图）→ 自动装

一个 `pymupdf` 全覆盖，纯 pip，不碰外部程序。装法固定在 `工具/py` 里：

```bash
./工具/py 工具/pdf_tools.py merge 生成物/合并.pdf a.pdf b.pdf
```

第一次调用会自建 `.venv`（仓库根或技能包根）、用国内镜像装依赖，约 10 秒，之后直接转发。

三条硬约定：

1. **锁 `pymupdf==1.24.14`**。2.x 会把 `pymupdf_layout`、`pymupdf4llm`、`onnxruntime`（80 MB）、`numpy`（34 MB）、
   `networkx`（18 MB）当硬依赖拖进来，venv 从 81 MB 涨到 284 MB，而这三个 API 一模一样。
2. **镜像顺序：清华 → 阿里 → 腾讯云**，全部失败才报错。三个源都在国内，任一能通即可。
   **不许改全局 `pip.conf`**——命令行带 `-i` 只作用于这一次，不污染机器上别的项目。
3. **不许 sudo、不许 `--break-system-packages`、不许装进系统 Python**。依赖只进 `.venv`，
   卸载就是删目录，永远不脏系统。

### 2.2 Word 转 PDF → 不代装，只给指引

`docx → pdf` 没有纯 Python 方案（`docx2pdf` 只是个壳，macOS 下仍靠 AppleScript 驱动 Word）。唯一可靠的是 LibreOffice：

- 装之前先探 `soffice`：PATH 里找，找不到再找 `/Applications/LibreOffice.app/Contents/MacOS/soffice`。
  两条都试过才判定"没装"——手动拖 dmg 装的和 brew 装的位置不同，只探一个会误判。
- **agent 不许自己下载、不许 `brew install --cask libreoffice`、不许 sudo 装**。原因：
  包 806 MB；brew cask 走官方源实测 0.4 MB/s（清华镜像 23.7 MB/s）；装它还要管理员授权。
- 没装就**停手，给用户两条路**，然后等他说一声再继续：

```
① 最省事：在 Word 里打开该 docx → 文件 → 另存为 → PDF（零安装）
② 装 LibreOffice（806 MB，装一次长期有效）：
   https://mirrors.tuna.tsinghua.edu.cn/libreoffice/libreoffice/stable/
   进版本目录选 mac/aarch64/（Apple 芯片）或 mac/x86-64/（Intel），下 dmg 拖进「应用程序」
```

**不许静默降级**：不能因为没装 LibreOffice 就偷偷截图拼 PDF、或拿 `qlmanage` 缩略图糊弄——
那正是 `AGENTS.md` 第 11 条明令禁止的"渲染核对"路子，出来的东西不能用。

---

## 3. 命令清单（照抄，别自己造轮子）

```bash
./工具/py 工具/pdf_tools.py info     <in.pdf>
./工具/py 工具/pdf_tools.py merge    <out.pdf> <in1.pdf> <in2.pdf> ...
./工具/py 工具/pdf_tools.py toimg    <in.pdf> <outdir> [--dpi 200] [--pages 1-3]
./工具/py 工具/pdf_tools.py extract  <in.pdf> <outdir>
./工具/py 工具/pdf_tools.py topdf    <in.docx> [--out out.pdf]
```

退出码：`0` 成功 / `2` 缺外部程序（附指引）/ `3` 输入有问题 / `4` 处理失败。

**一律走 `./工具/py`，不许裸敲 `python3`**。本机有四个 `python3`，裸敲的那个不一定装了依赖，
装到别的解释器里会出现"pip 说装好了、脚本却 import 失败"。

---

## 4. 产物与命名

| 东西 | 放哪 | 命名 |
|---|---|---|
| 转出的 PDF、合并后的 PDF | `生成物/` | `<原名>.pdf`、`<主卷名>-合并.pdf` |
| 逐页渲染的 PNG | `原料/<任务名>/pdf-中间/` | `<原名>-001.png`（页码三位） |
| 抽出的内嵌图 | `原料/<任务名>/pdf-中间/` | `p001-x<ref>.png`（页号 + 对象号，便于回查） |

中间件不算交付物，用完可删；成品一律进 `生成物/`（`HANDOVER.md` §0.6 目录约定）。

---

## 5. 保真与已知局限

- **docx → PDF 会重排字体**：soffice 用的是系统字库，机器上没装宋体 / Times New Roman 时会被替换，
  行距和断行都会漂。看着像"转换出错"，其实是字体缺失——先查字体，别去改版式。
- **抽图只能抽真内嵌位图**：矢量图、被蒙版或裁切处理的图抽出来会残缺。遇到这种情况退到 `toimg`
  整页渲染再裁，不要在抽图上反复试。
- **加密 PDF 直接报错**，请用户给无密码版本，不尝试破解。
- **中文文件名没问题**，pymupdf 与 soffice 都支持；但 zip 打包仍要用 Python `zipfile`（见 `AGENTS.md` §A.6）。

---

## 6. 自检

PDF 的检查比 docx 简单，**只查两件**：文件头是 `%PDF-`、页数对得上。不渲染成图人工比对——
`AGENTS.md` 第 11 条的自检预算对 PDF 同样有效，一次任务合计 ≤ 3 次。

```bash
./工具/py 工具/pdf_tools.py info 生成物/xxx.pdf    # 页数、内嵌图数量
```
