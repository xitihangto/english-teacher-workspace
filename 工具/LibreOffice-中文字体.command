#!/bin/sh
# 双击本文件 = 带中文字体启动 LibreOffice 图形界面。
# 原因：LibreOffice 自带的 fontconfig 把配置目录写死在 /usr/local/etc/fonts，
# 这个目录在 macOS 上不存在，于是它读不到任何系统字体（宋体、黑体、苹方全没有）。
# 本脚本只是把 FONTCONFIG_FILE 指到仓库里的 fonts.conf，不改任何系统设置。
DIR=$(cd "$(dirname "$0")" && pwd)
SOFFICE=/Applications/LibreOffice.app/Contents/MacOS/soffice
[ -x "$SOFFICE" ] || { echo "没找到 $SOFFICE"; exit 2; }
FONTCONFIG_FILE="$DIR/fonts.conf" exec "$SOFFICE" "$@"
