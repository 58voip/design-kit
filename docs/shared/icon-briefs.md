# 图标绘制清单

每个图标占一行。第一列是拟用的 SVG 文件名，第二列是中文名称，第三列是绘制要求。新增或修改需求时可以直接编辑第三列。通用线宽、圆角和用色沿用 [Wired Outline 图标规范](icon-system.md)。

绘制进度（2026-11-10）：本清单 62 枚线条图标均已绘制。各组预览包含 144 px、48 px 和 36 px 三种尺寸。SVG 保存在[共用图标目录](../../assets/icons)，品牌文件见[素材索引](visual-assets.md)。预览可用 `python3 scripts/render-icon-preview.py` 在 macOS 上重建，需要 Pillow 和系统自带的 sips。

## 3CX 官方产品与部署组件

[3CX 组件预览](icon-preview-3cx-components.png)

使用[灰色版 3CX Logo](../../assets/brands/3cx/3CX-GRAY.png)，保留原色、比例和完整标记。图标内采用上下结构，设备正面或客户端内容区上方放 Logo，下方放识别符号。小尺寸下优先简化细节，留出线间空隙。

| 图标英文名称（文件名）        | 中文名称              | 图标描述                                                                                                  |
| ----------------------------- | --------------------- | --------------------------------------------------------------------------------------------------------- |
| `3cx-server.svg`              | 3CX 服务器            | 两层机架轮廓，上层居中放 3CX Logo，下层放左侧蓝色状态灯与两条面板线。                                     |
| `3cx-sbc.svg`                 | 3CX SBC               | 小型网关上方放 3CX Logo，下方留两个空心端口，蓝色强调左侧端口。左右各伸出一小段连接线。                   |
| `3cx-windows-softphone.svg`   | 3CX Windows 软电话    | 单层应用窗口，标题栏右侧保留最小化、最大化和关闭图形。内容区上方放 3CX Logo，下方放空心蓝色听筒。         |
| `3cx-mobile-softphone.svg`    | 3CX 手机软电话        | 竖向手机轮廓，屏幕内上方放 3CX Logo，下方放空心蓝色听筒。底部用一条短线表示手势区。                       |
| `3cx-web-softphone.svg`       | 3CX 网页软电话        | 浏览器窗口顶部只保留一条地址栏。内容区上方放 3CX Logo，下方放空心蓝色听筒。                               |
| `3cx-ai-server.svg`           | 3CX AI Server         | 机架上层放 3CX Logo，下层放带 AI 字样的空心芯片和两道蓝色声纹。                                           |
| `3cx-video-phone.svg`         | 接入 3CX 的视频电话机 | 宽屏桌面话机，左侧放实体手柄。屏幕内上方放 3CX Logo，下方放蓝色视频符号，四周留白。                       |
| `3cx-router-phone.svg`        | 3CX 路由电话机        | 以实体话机为主体，小屏内放 3CX Logo。底座一侧加蓝色分支线和两个节点，表示话机内置 SBC。                   |
| `3cx-pms-module.svg`          | 3CX PMS 模块          | 酒店门牌和入住记录卡同高同宽、上下对齐。门牌内放蓝色钥匙，记录卡上方放放大的 3CX Logo，下方留两条记录线。 |
| `3cx-call-center-module.svg`  | 3CX 呼叫中心模块      | 队列面板上方放 3CX Logo，下方用坐席耳麦和三枚分开的节点表示呼叫队列，蓝色点亮队首。                       |
| `3cx-cloud-server.svg`        | 承载 3CX 的云服务器   | 用带底部缺口的云轮廓包住开放式机架托槽。上方放 3CX Logo，下方用蓝色状态灯和短面板线表示服务器。           |
| `3cx-virtual-machine.svg`     | 运行 3CX 的虚拟机     | 用上下两层机架表现服务器。上层放 3CX Logo，下层放蓝色状态灯和面板线。机架下方用两层浅折线表示虚拟化底座。 |
| `3cx-active-server.svg`       | 3CX 主服务器（ACTIVE） | 两层机架，上方放 3CX Logo，下方用蓝色 ACTIVE 字样标识主用角色。                  |
| `3cx-standby-server.svg`      | 3CX 备份服务器（STANDBY） | 沿用主服务器机架，上方放 3CX Logo，下方用蓝色 STANDBY 字样标识备用角色。             |
| `3cx-multi-tenant-server.svg` | 3CX 多租户服务器      | 两层机架，上层放 3CX Logo，下层放三个隔开的租户单元，用一枚蓝色单元强调租户分组。                         |
| `3cx-tenant.svg`              | 3CX 租户              | 单个组织面板，上方放 3CX Logo，下方放一栋办公楼轮廓和一扇蓝色门。                                         |
| `3cx-xapi.svg`                | 3CX XAPI（配置 API）  | 上方放 3CX Logo，下方放 XAPI 字样和蓝色滑杆，表现通过接口配置系统。                                       |
| `3cx-call-control-api.svg`    | 3CX Call Control API  | 上方放 3CX Logo，下方用空心蓝色听筒与一组代码括号表示通话控制接口。                                       |

产品与部署节点参考 [3CX 多租户配置](https://www.3cx.com/docs/multi-tenant-configuration/)、[3CX Call Control API](https://www.3cx.com/docs/call-control-api/)、[3CX 应用列表](https://www.3cx.com/ordering/pricing/features/)、[AI Server](https://www.3cx.com/docs/transcription-engine-server/)、[酒店 PMS](https://www.3cx.com/docs/pms-integration/)、[呼叫中心](https://www.3cx.com/call-center/) 和 [IP 话机与路由电话机](https://www.3cx.com/docs/manual/ip-phones/)。CRM 品牌原件见 [3CX CRM 集成品牌索引](crm-brand-logos.md)。

## VoIP／SIP 设备相关图标

[VoIP／SIP 设备与通话角色预览](icon-preview-voip-sip.png) · [话机品牌素材来源](visual-assets.md#话机品牌原件)

通用设备用中灰空心轮廓和局部蓝色。部署图需要表明话机已接入 3CX 时，可以使用带 3CX Logo 的话机款。主叫和被叫是这组设备图的通话角色配套图标。

| 图标英文名称（文件名）     | 中文名称               | 图标描述                                                                                          |
| -------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------- |
| `sip-desk-phone.svg`       | SIP 桌面话机           | 扁方形桌面底座，左侧放实体听筒，右上角画小屏，右下角用两排小点表示按键。小屏里用一条蓝色状态线。  |
| `3cx-desk-phone.svg`       | 接入 3CX 的 SIP 话机   | 沿用 SIP 桌面话机的结构，在小屏内放完整 3CX Logo，表示它连接到 3CX 系统。                         |
| `sip-dect-base.svg`        | SIP DECT 基站          | 一个短方形基站和一支竖向无线话机。基站顶端加两道小蓝色波纹，话机用细线画屏幕和按键。              |
| `sip-ata.svg`              | 模拟电话适配器（ATA）  | 小型盒体，两侧分别用听筒和网口图形表示模拟电话与网络。用一段蓝色短线表示两侧转换。                |
| `voip-voice-gateway.svg`   | VoIP 语音网关          | 扁平机架，左侧画一组灰色电话端口，右侧用蓝线描出较大的网口。                                      |
| `sip-intercom.svg`         | SIP 门口对讲机         | 竖向面板，顶部是喇叭孔，下方是圆形呼叫按钮。用一圈蓝色细线强调按钮。                              |
| `teams-desk-phone.svg`     | Microsoft Teams 电话机 | 沿用 Cisco 话机的机身、带支架的小屏和两列功能键。屏幕内放 Teams 标记，保留原色和比例。            |
| `sip-sbc.svg`              | 通用 SIP SBC           | 扁平网关，左右各有一个连接点。中间用两段蓝色细线穿过一个小盾牌，表示会话经过边界控制节点。        |
| `sip-conference-phone.svg` | SIP 会议电话机         | 用低矮的三角形或三瓣底座，中央画扬声器网格，三个端点各画一个小麦克风，其中一处用蓝线强调。        |
| `cisco-desk-phone.svg`     | Cisco 电话机           | 用带支架的小屏、侧置实体手柄和两列短功能键表现桌面话机。屏幕内放 Cisco 官方字标，保留原色和比例。 |
| `avaya-desk-phone.svg`     | Avaya 电话机           | 沿用 Cisco 话机的机身、带支架的小屏和两列功能键。屏幕内放 Avaya 字标，保留原色和比例。            |
| `mitel-desk-phone.svg`     | Mitel 电话机           | 沿用 Cisco 话机的机身、带支架的小屏和两列功能键。屏幕内只显示 Mitel 字标，保留原色和比例。        |
| `caller.svg`               | 主叫                   | 一个人、一个空心电话手柄和一支蓝箭头。人物与手柄组成一组，箭头从这组元素指向外侧，表示拨出。      |
| `callee.svg`               | 被叫                   | 与主叫使用相同的人物和手柄轮廓。蓝色箭头从外侧指向人物与手柄这一组，表示接收来电。                |
| `fxo-gateway.svg`          | FXO 网关               | 沿用横向语音网关机壳，面板上部留清楚的 FXO 字样，下部排两个接口，蓝色描网口。                     |
| `fxs-gateway.svg`          | FXS 网关               | 与 FXO 网关同形，面板上部留清楚的 FXS 字样，下部排两个接口，蓝色描网口。                          |
| `e1-gateway.svg`           | E1 网关                | 沿用同组网关机壳，面板上部留清楚的 E1 字样，下部放线路口与蓝色网口。                              |

三款网关沿用同一机壳，分别保留 FXO、FXS、E1 字样。

## 网络设备相关图标

[网络设备预览](icon-preview-network.png)

设备轮廓和内部结构用中灰线，蓝色只标出最能区分用途的细节。

| 图标英文名称（文件名）       | 中文名称               | 图标描述                                                                                                              |
| ---------------------------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `network-firewall.svg`       | 防火墙                 | 用横向设备盒体，面板中央叠一个空心盾牌，左右留出连接点。盾牌用蓝色轮廓。                                              |
| `fiber-ont.svg`              | 光猫（ONT）            | 扁平圆角盒体，左侧接一根带蓝色接头的细光纤，右侧画一个网口。面板用两颗小状态灯补充细节。                              |
| `network-router.svg`         | 路由器                 | 横向机壳内，中部并排放两个灰色网口，右侧放蓝色双向交换箭头。                                               |
| `network-switch.svg`         | 交换机                 | 横向机架面板，一排等距的小网口。选一两个端口加蓝色状态灯，保留端口阵列的辨识度。                                      |

## 语音通信系统与网络

[语音通信系统与网络预览](icon-preview-telephony.png)

交换平台、运营商、中继和公共电话网络在本组，终端与硬件网关归入 VoIP／SIP 设备组。

| 图标英文名称（文件名）     | 中文名称             | 图标描述                                                                |
| -------------------------- | -------------------- | ----------------------------------------------------------------------- |
| `pabx.svg`                 | PABX 电话交换机      | 横向机架，面板内用一条蓝色来线分向三枚分机端点，表现内部电话交换。      |
| `telecom-carrier.svg`      | 电信运营商           | 用通信塔与两道蓝色信号弧表示运营商节点。                                |
| `avaya-pabx.svg`           | Avaya 电话交换机     | 沿用 PABX 机架，上层放 Avaya 原色字标，下层放交换分支。                 |
| `cisco-cucm.svg`           | Cisco CUCM           | 采用呼叫管理机架，上层放 Cisco 原色标记，下层用一个控制节点连两支听筒。 |
| `mitel-pabx.svg`           | Mitel 电话交换机     | 沿用 PABX 机架，上层只显示 Mitel 原色字标，下层放交换分支。             |
| `sip-trunk.svg`            | SIP 中继             | 左右端点之间用两道平行细线连接，蓝色强调中间链路。                      |
| `sip-server.svg`           | SIP 服务器           | 两层通用机架，上层显示 SIP 字样，下层放一条面板线和蓝色状态灯。         |
| `pstn-network.svg`         | PSTN 网络            | 用开放云轮廓与内部三个相连的节点表现公共电话网络，保留 PSTN 字样。      |
| `teams-direct-routing.svg` | Teams Direct Routing | 用 Teams 标记、小型 SBC 和蓝色连接线表达语音接入路径，沿横向排开。      |

名称与构图参考 [Cisco Unified Communications Manager](https://www.cisco.com/c/en/us/products/unified-communications/unified-communications-manager-callmanager/index.html) 和 [Microsoft Teams Direct Routing](https://learn.microsoft.com/en-us/microsoftteams/direct-routing-connect-the-sbc)。

## 软件应用与功能

[软件应用与功能预览](icon-preview-applications.png)

通用呼叫队列与 PMS 使用独立编号，分别对应跨平台功能与酒店系统。

| 图标英文名称（文件名） | 中文名称      | 图标描述                                                       |
| ---------------------- | ------------- | -------------------------------------------------------------- |
| `call-queue.svg`       | 呼叫队列      | 三个等距呼叫节点向坐席耳麦排开，用蓝色强调队首。               |
| `sms.svg`              | 短信息（SMS） | 用单个消息气泡和 SMS 字样标识短信，下面保留一条蓝色短线。      |
| `video-meeting.svg`    | 视频会议      | 一面会议窗口内放两枚与会者头像，右下角用蓝色视频符号标识会议。 |
| `knowledge-base.svg`   | 知识库        | 用打开的索引手册表现可查阅资料，蓝色突出书签。                 |
| `call-recording.svg`   | 通话录音      | 用音频波形和蓝色圆形录音指示组成简洁录音符号。                 |
| `pms-system.svg`       | 酒店 PMS 系统 | 等高的房门牌与入住记录卡并列，用蓝色钥匙突出酒店管理。         |
| `developer-sdk.svg`    | 开发 SDK    | 开放轮廓的代码窗口，上方用蓝色代码括号，下方保留 SDK 字样。    |

## 服务器与基础服务

[服务器与基础服务预览](icon-preview-server-services.png)

使用同一套机架轮廓，通过服务标记、操作系统标记或传输符号区分。

| 图标英文名称（文件名）   | 中文名称       | 图标描述                                                            |
| ------------------------ | -------------- | ------------------------------------------------------------------- |
| `application-server.svg` | 应用服务器     | 上下两层机架，上层留三枚应用方块，下层用蓝色状态线表示运行。        |
| `samba-server.svg`       | Samba 文件服务 | 用共享文件夹和两条连接线表现文件共享，蓝色强调共享分支。            |
| `dns-server.svg`         | DNS 服务器     | 用机架和清楚的 DNS 字样标识解析服务，蓝色强调查询节点。             |
| `web-server.svg`         | Web 服务器     | 机架上方放简化的浏览器地址栏，下方放面板线与蓝色状态灯。            |
| `linux-server.svg`       | Linux 服务器   | 复用通用机架外形，上层放 Linux 企鹅识别标记，下层保留蓝色状态灯。   |
| `windows-server.svg`     | Windows 服务器 | 复用通用机架外形，上层放 Windows 窗格识别标记，下层保留蓝色状态灯。 |
| `ftp-server.svg`         | FTP 服务器     | 机架上层放 FTP 字样，下层用蓝色上下箭头表现文件传输。               |

## 案例新增组合图标（2026-11-11）

| 图标英文名称（文件名） | 中文名称 | 图标描述 |
|---|---|---|
| `employee-phone.svg` | 员工电话协作 | 中灰圆角细线与局部蓝色，用于小红书案例对应主题；原件为独立 SVG。 |
| `review-checklist.svg` | 审查清单 | 中灰圆角细线与局部蓝色，用于小红书案例对应主题；原件为独立 SVG。 |
| `database-readonly-review.svg` | 数据库只读审查 | 中灰圆角细线与局部蓝色，用于小红书案例对应主题；原件为独立 SVG。 |
