# coding: utf-8
"""Refresh the design index when files change; --check verifies freshness."""
from pathlib import Path
import hashlib
import sys
from datetime import datetime
ROOT = Path(__file__).resolve().parent.parent
EXCLUDE = {'.DS_Store', '__pycache__', '.git', 'node_modules', '.venv', 'tree.md'}

def entries(folder):
    return sorted((p for p in folder.iterdir() if p.name not in EXCLUDE and not p.name.startswith('.')), key=lambda p: (not p.is_dir(), p.name.casefold()))

rows = []
fingerprint = hashlib.sha256()
def walk(folder, prefix=''):
    children = entries(folder)
    for index, p in enumerate(children):
        last = index == len(children)-1
        rows.append(prefix + ('└── ' if last else '├── ') + p.name + ((' → ' + str(p.readlink())) if p.is_symlink() else ('/' if p.is_dir() else '')))
        stat = p.lstat()
        fingerprint.update(f'{p.relative_to(ROOT)}:{stat.st_size if not p.is_dir() else 0}:{stat.st_mtime_ns if not p.is_dir() else 0}\n'.encode())
        if p.is_dir() and not p.is_symlink():
            walk(p, prefix + ('    ' if last else '│   '))
walk(ROOT)
marker = '<!-- fingerprint: ' + fingerprint.hexdigest() + ' -->'
out = ROOT/'tree.md'
if out.exists() and marker in out.read_text():
    print('tree.md is current')
    sys.exit(0)
if '--check' in sys.argv:
    print('tree.md needs refresh')
    sys.exit(1)
intro = '''# 设计目录与规范索引

正式素材：`~/design/assets/`。规范：`~/design/docs/`。技能：`~/design/skills/`。项目交付：`~/design/projects/`。历史备份：`~/design/archive/`。

## 设计规范

[目录结构与维护](docs/shared/library-structure.md) · [PPT 规范入口](docs/presentations/README.md)

| 规范 | 内容 |
|---|---|
| [图标规范](docs/shared/icon-system.md) | Wired Outline：中灰空心圆角细线、局部 3CX 蓝、透明背景、SVG 分层；新图标自动入库 |
| [图标绘制清单](docs/shared/icon-briefs.md) | 英文文件名、中文名称、绘制说明，含分组预览 |
| [素材分类与使用](docs/shared/visual-assets.md) | 品牌、线条图标、插画的存放、查找与复用 |
| [CRM 品牌原件](docs/shared/crm-brand-logos.md) | CRM 品牌原件与来源 |
| [拓扑图规范](docs/images/topology-style.md) | 白底、蓝灰四类线路、连接端点、标题与精简标签 |
| [视频制作规范](docs/videos/workflow.md) | 分镜、图标动效、旁白字幕、品牌角标及成片验收 |
| [企业案例技能](skills/case-study/SKILL.md) | 客户与挑战、解决方案、项目成果三页图片 |
| [企业案例设计规则](skills/case-study/references/image-case-style.md) | 精简文字、标题箭头、Logo 比例、四主题说明、照片与留白 |
| [已认可案例标准](skills/case-study/references/approved-three-page-standard.png) | 当前用户认可的三页视觉参考 |
| [素材使用技能](skills/design-assets/SKILL.md) | 查找原件、跨媒介复用及新图标入库流程 |

## 维护

本机登录后每 60 秒检查内容变化并刷新本文件；助手修改后也应立即运行 `python3 ~/design/scripts/update-tree.py`。
校验命令：`python3 ~/design/scripts/update-tree.py --check`。
不展开隐藏目录、缓存、Git、依赖目录；目录结构为自动生成，请勿手工编辑。

## 完整结构

```text
~/design/
'''
out.write_text(intro + '\n'.join(rows) + '\n```\n\n更新时间：' + datetime.now().astimezone().isoformat(timespec='seconds') + '\n' + marker + '\n')
print('Updated ' + str(out))
