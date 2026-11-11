# 设计素材分类

2026-11-09 用户确认分三类管理。

[全部图标总览](icon-preview-all.png)汇总线条图标和品牌标记，可用 macOS「预览」放大查看。

PPT、图片和视频共用这里的源文件。跨媒介查找与取用见[设计素材库技能](../../skills/design-assets/SKILL.md)。

| 类别 | 目录 | 选用原则 |
|---|---|---|
| 品牌图标库 | [assets/brands/](../../assets/brands) | 留存品牌官方原件，保留原色、字标和比例。彩色官方图标可直接使用。3CX 视频默认用用户指定的灰色 Logo。 |
| 线条图标库 | [assets/icons/](../../assets/icons) | 用于人物、操作和流程节点。按[Wired Outline 图标规范](icon-system.md)使用中灰空心描边与局部 3CX 蓝。 |
| 插画库 | [assets/illustrations/](../../assets/illustrations) | 用于整幅功能或情境画面。通用风格待定，当前[无文字来电摘要插画](../../assets/illustrations/3cx-call-popup-summary.png)是用户认可的方向样例。 |

## 品牌来源

- [3CX 灰色 Logo](../../assets/brands/3cx/3CX-GRAY.png)为用户提供的标准文件。素材库同时留存先前的白色版。
- [Zoho](../../assets/brands/zoho.svg)留存[官方 SVG](https://www.zohowebstatic.com/sites/zweb/images/commonroot/zoho-logo-web.svg)，按[官方品牌规范](https://www.zoho.com/branding/visual-guidelines.html)保持比例和颜色。

- 千问保留[官网项目中的彩色原件](../../assets/brands/qwen/qwen-official.png)。[灰色显示版](../../assets/brands/qwen/qwen-gray-display.png)在排版时对同一标记做去饱和处理，供浅色拓扑图使用。来源为[千问官方站点仓库](https://github.com/QwenLM/qwenlm.github.io/blob/main/static/img/logo.png)。

- [3CX CRM 集成品牌索引](crm-brand-logos.md)列出可复用的 CRM 和客服品牌 Logo。

插画示意可以在分镜里另作说明。来电摘要插画用于表达功能概念，不能作为客户端实测画面。

## 话机品牌原件

设备 SVG 的品牌层按比例嵌入标记。Teams 和 Cisco 使用原 SVG 渲染为 PNG 后嵌入，Avaya 和 Mitel 直接嵌入原 PNG。Mitel 话机通过 SVG 视口只显示 Mitel 字标，素材库保留完整原件。

| 标记 | 本地原件 | 来源 | 品牌使用说明 |
|---|---|---|---|
| Microsoft Teams | [SVG](../../assets/brands/phones/teams.svg) | [Microsoft 365 标记的存档](https://commons.wikimedia.org/wiki/File:Microsoft_Office_Teams_(2025%E2%80%93present).svg) | [Microsoft 品牌规范](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks) |
| Cisco | [SVG](../../assets/brands/phones/cisco.svg) | [Cisco 品牌素材](https://brand-assets.security.cisco.com/) | [Cisco 企业 Logo 指南](https://www.cisco.com/c/en/us/about/brand-center/logo-usage-guidelines/corporate-logo.html) |
| Avaya | [PNG](../../assets/brands/phones/avaya.png) | [Avaya 媒体图库红色字标](https://news.avaya.com/press-portal-image-gallery) | [Avaya 商标及使用条款](https://www.avaya.com/en/legal/termsofuse/) |
| Mitel | [PNG](../../assets/brands/phones/mitel.png) | [Zoom 的 Mitel 合作伙伴页面](https://partner.zoom.com/solutions/mitel/) | [Mitel 商标说明](https://www.mitel.com/legal/trademarks) |

## 软件品牌原件

[查看七款品牌标记](icon-preview-software-brands.png)。素材保留下载版本的原色和比例，文件存放于 `assets/brands/software/`。

| 标记 | 本地原件 | 来源与品牌使用说明 |
|---|---|---|
| Microsoft SharePoint | [SVG](../../assets/brands/software/sharepoint.svg) | [2025 版微软标记存档](https://commons.wikimedia.org/wiki/File:Microsoft_Office_SharePoint_(2025%E2%80%93present).svg) · [Microsoft 品牌规范](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks) |
| Microsoft 365 | [SVG](../../assets/brands/software/microsoft-365.svg) | [2022 版套件标记存档](https://commons.wikimedia.org/wiki/File:Microsoft_365_(2022).svg) · [Microsoft 品牌规范](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks) |
| WhatsApp | [SVG](../../assets/brands/software/whatsapp.svg) | [WhatsApp 官网标记的矢量存档](https://commons.wikimedia.org/wiki/File:WhatsApp.svg) · [WhatsApp 品牌规范](https://www.meta.com/brand/resources/whatsapp/whatsapp-brand/) |
| WordPress | [PNG](../../assets/brands/software/wordpress.png) | [WordPress 官方图形资源](https://wordpress.org/about/logos/)，使用透明底 W 标记 |
| MySQL | [PNG](../../assets/brands/software/mysql.png) | [MySQL 官网原色标记及使用条件](https://www.mysql.com/about/legal/logos.html) |
| PostgreSQL | [SVG](../../assets/brands/software/postgresql.svg) | [PostgreSQL 官方三色标记](https://wiki.postgresql.org/wiki/Logo) · [视觉规范](https://wiki.postgresql.org/wiki/Identity_Guidelines) |
| Microsoft SQL Server | [SVG](../../assets/brands/software/sql-server.svg) | [SQL Server 2025 标记存档](https://commons.wikimedia.org/wiki/File:Microsoft_SQL_Server_2025_icon.svg) · [Microsoft 品牌规范](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks) |

## 生成图标必须入库

凡使用 `~/design` 制作内容时产生的新图标元素，均须单独保存到正式图标库，覆盖图片、PPT、拓扑图、视频等用途。不能只保留整页生成图；整页中的新图形需要单独重建为可复用图标并验收。线条图标存入 `assets/icons/`，品牌原件存入 `assets/brands/`；同步清单、预览、来源及使用说明，具体按[图标自动入库规则](icon-system.md)执行。

## 宁波诺丁汉大学

[官网 Logo 原件](../../assets/brands/unnc/unnc-logo.jpg) · [来源与使用说明](../../assets/brands/unnc/sources.md)。品牌原件保留原色及比例；校名“宁波诺丁汉大学”单独排版，不把品牌结构讲解图当 Logo。

## 小红书

[品牌图标原件](../../assets/brands/xiaohongshu/logo.png) · [来源](../../assets/brands/xiaohongshu/sources.md)。红色方形品牌标记保留比例，不作为自绘线条图标管理。
