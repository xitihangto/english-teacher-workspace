#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 变更日志.md 抽出版本条目，生成 GitHub Release 的标题与正文。

用法：
    python3 工具/release_notes.py v1.15            # 打印 release 正文（Markdown）
    python3 工具/release_notes.py v1.15 --title    # 只打印标题，如「v1.15 自检预算硬规矩 + ...」
    python3 工具/release_notes.py --latest         # 用最新 tag 之外的最近一条版本条目（按 §2 顺序）

找不到对应版本条目时退出码 1，并往 stderr 打一行原因。
不依赖网络，只读本地 变更日志.md。
"""
import re
import sys
import pathlib

CHANGELOG = pathlib.Path(__file__).resolve().parent.parent / "变更日志.md"

FOOTER = """---

**本包不含** `生成物/`（交付成品）与 `原料/`（用户原料、下载原文件、OCR 中间件）——这两类由 `.gitignore` 排除，需要的话从本地取。

**上手**

1. 解压后把会话工作目录指向仓库根目录
2. 先读 `AGENTS.md` 和 `索引.md`
3. 按规则路由只读对应那一份 `规范/`：讲义 01 / 批改 02 / 识别 03 / 链接下载 04
4. 成品写 `生成物/`，原料放 `原料/<任务名>/`，根目录只放规则与脚本

**改规则请回仓库改**，不要在这个解压副本上改；以 `变更日志.md` 与仓库 tag 为准。
"""


def load_section(tag: str):
    """返回 (标题行, 正文)；找不到返回 (None, None)。"""
    text = CHANGELOG.read_text(encoding="utf-8")
    # 条目形如：### v1.15 · 2026-11-03 17:19 · 自检预算硬规矩 + 保留原则放宽为可移位可加注
    pat = re.compile(r"^### (" + re.escape(tag) + r"[^\n]*)\n(.*?)(?=^### |\Z)", re.S | re.M)
    m = pat.search(text)
    if not m:
        return None, None
    heading = m.group(1).strip()
    body = m.group(2).strip()
    return heading, body


def make_title(heading: str, tag: str) -> str:
    """v1.15 · 日期 · 一句话  →  v1.15 一句话"""
    parts = [p.strip() for p in heading.split("·")]
    if len(parts) >= 3:
        return f"{parts[0]} {parts[-1]}"
    return heading


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    title_only = "--title" in sys.argv

    if not args:
        print("用法：release_notes.py <tag> [--title]", file=sys.stderr)
        return 2

    tag = args[0]
    heading, body = load_section(tag)
    if heading is None:
        print(f"变更日志.md 里没有 {tag} 的版本条目", file=sys.stderr)
        return 1

    if title_only:
        print(make_title(heading, tag))
        return 0

    print(f"## {heading}\n")
    print(body)
    print()
    print(FOOTER, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
