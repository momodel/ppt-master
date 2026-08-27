<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock: Product Launch Deep Space

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- audience: 成果展示的观众（评审、同行或公众）
- objective: 展示成果亮点与价值
- core_message: 由确认大纲决定
- consumption_mode: balanced

## mode
- mode: showcase

## visual_style
- visual_style: dark-tech

## colors
- background: #0A0A1A
- secondary_bg: #12122A
- primary: #7B68EE
- accent: #00D9FF
- secondary_accent: #FF6B9D
- body_text: #E8E8F0

## typography
- font_family: "Segoe UI", "Microsoft YaHei", sans-serif
- title_family: "Segoe UI", "Microsoft YaHei", sans-serif
- body_family: "Segoe UI", "Microsoft YaHei", sans-serif
- annotation_family: "Consolas", "Segoe UI", monospace
- body: 24
- title: 44
- subtitle: 32
- lead: 28
- annotation: 16

## icons
- library: phosphor-duotone
- inventory: rocket-launch, star, sparkle, thumbs-up

## page_rhythm
- P01: anchor
- P02: breathing
- P03: dense
- P04: breathing
- P05: anchor

## pptx_structure
- mode: flat

## layout
### principles
- 60px 外安全边距；深空黑底；标题左对齐，primary→accent 渐变色文字（SVG linearGradient）；特性卡片 secondary_bg 底圆角 12px 配 1px accent 边框；对比面板左右分裂配 accent 分隔线；正文 #E8E8F0 深底可读。
### variation
- 封面页全幅深空底+渐变大标题+底部品牌色横线；展示页居中 hero 元素配辐射光效装饰；特性页 2×2 或 1×3 卡片矩阵+accent 边框；对比页左右分裂+accent 分隔线+两侧观点+证据列表；结尾页三列亮点卡片+底部 CTA 色带。

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters

## page_types
- 封面页：深空底渐变标题的展示开篇页
- 目录页：编号列表的发布路线页
- 展示页：居中 hero 元素的聚焦展示页
- 特性页：卡片矩阵的亮点陈列页
- 对比页：左右分裂的方案对比页
- 结尾页：亮点卡片与 CTA 收束页
