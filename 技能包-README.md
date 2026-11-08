# 高三英语文档线（技能包）

发考卷 + 答案出讲义、发作文出批改稿、发试卷图出转录 Word、发一条链接自动取卷并去水印；
也能把成品转 PDF、把几份 PDF 合并、拆成图片、抽里面的图。
版式写死在 `references/` 的规范里，用的时候不用交代格式要求。

## 安装

把整个目录放到 `~/.workbuddy-ai/skills/gaosan-english/`（Windows：`%USERPROFILE%\.workbuddy-ai\skills\gaosan-english\`），
保留 `references/`、`scripts/` 的相对结构。卸载就是删掉这个目录（连带 `.venv` 一起删，不会留下任何东西）。

装完先看 `SKILL.md` 的《首次安装》：探测 `python-docx` / `pymupdf` / `soffice` / node / chromium，缺什么补什么。

**依赖默认一个都不装。** 第一次跑 `./scripts/py ...` 时它才自建 `.venv`（本目录下，81 MB，走国内镜像，约 10 秒），
之后一直复用；依赖坏了会自动重建。**不碰系统 Python，不用 sudo，不改全局 `pip.conf`。**

## 结构

```
SKILL.md        # 入口：硬规矩、规则路由、首次安装、按需安装、自检
references/     # 六份规范（01–05 + 技术要点）+ 三份版式参照 docx
scripts/        # py 依赖执行器 / check.py 体检 / pdf_tools.py PDF 四件事 / 去水印 / 渲染层 / 截包
```

## PDF 能力（按需）

- 合并 / 转图片 / 抽内嵌图：一个 `pymupdf` 搞定，`scripts/py` 自动装，不用手动 pip。
- **Word 转 PDF 需要 LibreOffice，本包不代装**（806 MB）。没装时会给出国内镜像地址，
  或者直接在 Word 里「另存为 PDF」，零安装。

## 边界

- 包内规则是**只读快照**，要改规则回仓库改、改完重新导出，别在技能目录里直接改。
- 模板 docx 只是版式参照，**不含真实题目**，缺素材得自己给。
- 导出依据与版本见 `SKILL.md` 顶部那行注释。
