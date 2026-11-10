# Design Kit · 设计规范与通用图标

这是用于 PPT、图片、拓扑图和视频的设计规范与通用线条素材分享版。收录 **43 枚可编辑 SVG**，使用统一的细线、开放轮廓和局部蓝色强调。

| 查找内容 | 入口 |
|---|---|
| 设备、语音通信、应用、服务器图标 | [图标绘制清单与分组预览](docs/icon-briefs.md) |
| 来电、消息、邮件、摘要等常用图标 | [通用图标预览](docs/icon-preview.png) |
| 线宽、留白、色彩和 SVG 分层 | [图标规范](docs/icon-system.md) |
| 视频编排与交付 | [视频制作规范](docs/workflow.md) |
| 在 Codex 中按名称选取素材 | [设计素材库技能](skills/design-assets/SKILL.md) |

在仓库根目录按名称查找原件：

```sh
python3 scripts/find-design-asset.py "SIP 终端"
python3 scripts/find-design-asset.py "路由器"
```

SVG 原件位于 [assets/icons](assets/icons/)。支持 SVG 的工具可直接使用原件；需要位图时，可按作品尺寸渲染透明 PNG。Mac 上可用 `python3 scripts/render-icon-preview.py` 重建各组预览（需要 Pillow 和系统自带的 sips）。

本仓库公开展示设计规范和素材。复用、修改或再分发请向维护者确认授权。
