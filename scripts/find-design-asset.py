#!/usr/bin/env python3
"""Find the canonical local asset by display name, filename, or common alias."""

import argparse
from pathlib import Path
import re
import sys
import unicodedata


ROOT = Path(__file__).resolve().parents[1]
KINDS = {"icon": "icons"}
FORMATS = {".svg", ".png", ".webp", ".jpg", ".jpeg"}
ALIASES = {
    "icons/sip-desk-phone.svg": ("SIP 终端", "SIP 话机"),
    "icons/3cx-desk-phone.svg": ("3CX SIP 终端", "接入 3CX 的 SIP 终端"),
    "icons/network-router.svg": ("网络路由器",),
    "icons/teams-direct-routing.svg": ("Direct Routing", "Teams 直连"),
    "icons/pms-system.svg": ("通用 PMS", "酒店 PMS"),
}


def normalize(value):
    return "".join(char for char in unicodedata.normalize("NFKC", value).casefold() if char.isalnum())


def indexed_names():
    labels = {}
    for doc in ("icon-briefs.md", "icon-system.md"):
        source = (ROOT / "docs" / doc).read_text()
        for name, title in re.findall(r"^\|\s*`([^`]+)`\s*\|\s*([^|\n]+)\|", source, re.M):
            filename = name if name.endswith(".svg") else f"{name}.svg"
            labels[f"icons/{filename}"] = title.strip()
    return labels


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="*", help="中文名称、英文名称或文件名")
    parser.add_argument("--kind", choices=KINDS, help="限定素材类型")
    args = parser.parse_args()
    query = normalize(" ".join(args.query))
    if args.query and not query:
        parser.error("请输入名称或文件名")
    labels = indexed_names()
    matches = []
    for kind, directory in KINDS.items():
        if args.kind and kind != args.kind:
            continue
        for path in (ROOT / "assets" / directory).rglob("*"):
            if not path.is_file() or path.suffix.lower() not in FORMATS:
                continue
            relative = path.relative_to(ROOT / "assets").as_posix()
            label = labels.get(relative, path.stem.replace("-", " "))
            keys = [normalize(value) for value in (label, path.stem, path.name, *ALIASES.get(relative, ()))]
            if not query or query in keys:
                rank = 0
            elif any(query in key for key in keys):
                rank = 1
            else:
                continue
            matches.append((rank, kind, label, path))
    if not matches:
        print("未找到匹配素材。可尝试更短的名称，或省略 --kind 查看全部分类。", file=sys.stderr)
        return 1
    for _, kind, label, path in sorted(matches):
        print(f"{kind}\t{label}\t{path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
