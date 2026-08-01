#!/bin/bash
# 动物世界 - 启动脚本
# 使用方法: ./start.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INDEX_FILE="$SCRIPT_DIR/index.html"

if [ -f "$INDEX_FILE" ]; then
    echo "🦁 正在启动动物世界小程序..."

    # 尝试在不同平台上打开 HTML 文件
    if command -v xdg-open &> /dev/null; then
        # Linux
        xdg-open "$INDEX_FILE"
    elif command -v open &> /dev/null; then
        # macOS
        open "$INDEX_FILE"
    else
        # Windows (在Git Bash中)
        start "$INDEX_FILE" 2>/dev/null || echo "请手动打开 $INDEX_FILE"
    fi

    echo "✓ 请在浏览器中查看！"
else
    echo "❌ 错误：找不到 index 文件！"
    echo "   请确保脚本与 index.html 在同一目录"
    exit 1
fi
