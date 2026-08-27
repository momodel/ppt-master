<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock: Business Report Dark Professional

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- audience: 汇报对象（管理层、评审者或客户）
- objective: 结构化呈现分析结论与决策建议
- core_message: 由确认大纲决定
- consumption_mode: balanced

## mode
- mode: pyramid

## visual_style
- visual_style: data-journalism

## colors
- background: #1A1A2E
- secondary_bg: #16213E
- primary: #E94560
- accent: #F5C518
- secondary_accent: #53C2C6
- body_text: #D4D4D8

## typography
- font_family: "Segoe UI", "Microsoft YaHei", sans-serif
- title_family: "Segoe UI", "Microsoft YaHei", sans-serif
- body_family: "Segoe UI", "Microsoft YaHei", sans-serif
- annotation_family: "Consolas", "Segoe UI", monospace
- body: 22
- title: 40
- subtitle: 30
- lead: 26
- annotation: 16
- footnote: 14

## icons
- library: phosphor-duotone
- inventory: chart-bar, trend-up, target, magic-wand, warning, check-circle

## page_rhythm
- P01: anchor
- P02: dense
- P03: dense
- P04: breathing
- P05: anchor

## pptx_structure
- mode: flat

## layout
### principles
- 48px 外安全边距；深色底不使用网格线；底部 24px 处放置页码与章节标签色带（primary 色 3px 横线 + 文本）；标题左对齐位于 48–110px，primary 色 4px 竖线前缀；主体内容区 110–650px；数据面板使用 secondary_bg 圆角矩形（8px）；KPI 数字使用 accent 色加大至 48px；正文 #D4D4D8 确保深底可读；图表轴线和标签使用 #D4D4D8。
### variation
- 封面页全幅 primary 色渐变（#E94560 -> #1A1A2E）背景，白色大标题居中，底部一条 4px 金色横线；数据页使用 2×2 或 1×3 KPI 面板矩阵，每个面板 secondary_bg 底圆角矩形，数字 48px accent 色标签 18px 灰色；对比页左右分裂布局，中间 2px 分隔线，两侧各一个观点标题+证据列表；结论页三列卡片，顶部 primary 色编号大字，卡片 secondary_bg 圆角底。

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters

## page_types
- 封面页：深色渐变底大标题开篇页
- 目录页：编号列表式汇报路线图
- 内容页：要点分条的结构化分析页
- 数据页：KPI 面板或数据矩阵的证据页
- 对比页：左右分裂的方案或状态对比页
- 结论页：行动建议与决策收束页
