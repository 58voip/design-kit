#!/usr/bin/env python3
"""Render the icon library previews using macOS sips and Pillow.

Usage: python3 scripts/render-icon-preview.py
Reads canonical SVGs and rebuilds the preview sheets in docs.
"""
from pathlib import Path
import re
import subprocess
import tempfile
import xml.etree.ElementTree as ET

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
SVG_NS = "http://www.w3.org/2000/svg"
XLINK = "http://www.w3.org/1999/xlink"
ET.register_namespace("", SVG_NS)
ET.register_namespace("xlink", XLINK)


def entries(text, heading):
    group = text.split(f"## {heading}\n", 1)[1].split("\n## ", 1)[0]
    group = group.split("\n### 待绘制\n", 1)[0]
    return re.findall(r"\|\s*`([^`]+\.svg)`\s*\|\s*([^|]+?)\s*\|", group)


def render(path, size, temp):
    tree = ET.parse(path)
    tree.getroot().set("width", str(size))
    tree.getroot().set("height", str(size))
    src = temp / f"{path.stem}-{size}.svg"
    dest = src.with_suffix(".png")
    tree.write(src, encoding="unicode")
    subprocess.run(["sips", "-s", "format", "png", str(src), "--out", str(dest)],
                   check=True, capture_output=True, timeout=20)
    image = Image.open(dest).convert("RGBA")
    assert image.size == (size, size), (path.name, image.size)
    bounds = image.getchannel("A").getbbox()
    assert bounds and bounds[0] > 0 and bounds[1] > 0 and bounds[2] < size and bounds[3] < size, (path.name, size, bounds)
    return image


def check_svg(path):
    svg = ET.parse(path).getroot()
    assert svg.get("viewBox") == "0 0 24 24", path.name
    assert float(svg.get("stroke-width", "0")) == 0.56, path.name
    assert svg.get("fill") == "none", path.name
    layers = {node.get("data-part"): node for node in svg if node.get("data-part")}
    assert {"body", "accent"} <= layers.keys(), path.name
    assert layers["body"].get("stroke", "").upper() == "#68737C", path.name
    assert layers["accent"].get("stroke", "").upper() == "#0596D4", path.name
    assert "brand" not in layers, path.name
    for node in svg.iter():
        width = node.get("stroke-width")
        if width:
            assert float(width) in (0.56, 0.46), (path.name, width)


def font(size):
    return ImageFont.truetype("/System/Library/Fonts/STHeiti Light.ttc", size)


def render_board(icons, heading, columns, filename):
    rows = (len(icons) + columns - 1) // columns
    board = Image.new("RGB", (56 + 306 * columns, 172 + 326 * rows), "#F6F8FA")
    draw = ImageDraw.Draw(board)
    draw.text((40, 32), heading, font=font(34), fill="#33434D")
    draw.text((40, 82), f"Wired Outline  /  {len(icons)} icons  /  24 × 24", font=font(17), fill="#68737C")
    with tempfile.TemporaryDirectory(prefix="3cx-icon-preview-") as folder:
        temp = Path(folder)
        for index, (svg_name, title) in enumerate(icons):
            path = ROOT / "assets/icons" / svg_name
            check_svg(path)
            row_count = min(columns, len(icons) - (index // columns) * columns)
            x = 40 + (index % columns) * 306 + (columns - row_count) * 153
            y = 132 + (index // columns) * 326
            draw.rounded_rectangle((x, y, x + 282, y + 302), radius=16, fill="white", outline="#E1E7EB")
            for size, xx, yy in ((144, x + 69, y + 18), (48, x + 71, y + 245), (36, x + 176, y + 251)):
                icon = render(path, size, temp)
                board.paste(icon, (xx, yy), icon)
            draw.text((x + 141, y + 181), title, font=font(18), fill="#33434D", anchor="mt")
            draw.text((x + 141, y + 210), svg_name, font=font(12), fill="#68737C", anchor="mt")
            draw.text((x + 56, y + 264), "48", font=font(11), fill="#89959D", anchor="rm")
            draw.text((x + 161, y + 264), "36", font=font(11), fill="#89959D", anchor="rm")
            print(f"OK {svg_name}: 144/48/36 px")
    output = ROOT / "docs" / filename
    board.save(output)
    print(output)


def main():
    standard = (ROOT / "docs/icon-system.md").read_text()
    general = [(f"{name}.svg", title.strip()) for name, title in
               re.findall(r"^\| `([^`]+)` \| ([^|]+) \|", standard, flags=re.M)]
    briefs = (ROOT / "docs/icon-briefs.md").read_text()
    boards = [
        (entries(briefs, "VoIP／SIP 设备相关图标"), "VoIP／SIP 设备与通话角色", 4, "icon-preview-voip-sip.png"),
        (entries(briefs, "网络设备相关图标"), "网络设备", 4, "icon-preview-network.png"),
        (entries(briefs, "语音通信系统与网络"), "语音通信系统与网络", 3, "icon-preview-telephony.png"),
        (entries(briefs, "软件应用与功能"), "软件应用与功能", 3, "icon-preview-applications.png"),
        (entries(briefs, "服务器与基础服务"), "服务器与基础服务", 4, "icon-preview-server-services.png"),
        (general, "通用线条图标", 3, "icon-preview.png"),
    ]
    indexed = [name for icons, _, _, _ in boards for name, _ in icons]
    assert len(set(indexed)) == len(indexed), "Duplicate icon filename in indexes"
    assert set(indexed) == {path.name for path in (ROOT / "assets/icons").glob("*.svg")}
    for icons, heading, columns, filename in boards:
        render_board(icons, heading, columns, filename)


if __name__ == "__main__":
    main()
