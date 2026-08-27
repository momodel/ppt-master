<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- audience: 理工科课堂学习者
- objective: 按确认大纲逐页展开教学讲解
- core_message: 由确认大纲决定
- consumption_mode: balanced

## mode
- mode: instructional

## visual_style
- visual_style: blueprint

## colors
- background: #0D2740
- secondary_bg: #13405E
- primary: #4FC3F7
- accent: #FFB74D
- secondary_accent: #81C784
- body_text: #E0E0E0

## typography
- font_family: "Microsoft YaHei", "Consolas", monospace, sans-serif
- title_family: "Microsoft YaHei", "Segoe UI", sans-serif
- body_family: "Microsoft YaHei", "Consolas", monospace, sans-serif
- annotation_family: "Microsoft YaHei", "Consolas", monospace, sans-serif
- body: 24
- title: 42
- subtitle: 32
- lead: 28
- annotation: 18
- footnote: 16

## icons
- library: phosphor-duotone
- inventory: waveform, wave-sine, math-operations, warning-circle, funnel, brain, check-circle

## page_rhythm
- P01: anchor
- P02: dense
- P03: dense
- P04: breathing
- P05: anchor

## pptx_structure
- mode: flat

## layout
- principles: 60px 外安全边距；蓝图坐标网格背景（#13405E 细线）；左对齐标题位于 60–130px；主体内容区 130–620px；所有线框、标注线、坐标轴使用 #4FC3F7 主色；关键条件/采样点/警告使用 #FFB74D 强调色；正面确认使用 #81C784；正文 #E0E0E0 确保对比度≥4.5:1；无圆角卡片，使用直角蓝图框 + 标注引线
- variation: 封面页使用全幅深蓝底+主色大标题+底部结论色带；内容页使用左文右图/左图右文交替，配蓝图坐标网格背景与标注线；数据页使用居中 hero 元素（公式/数字/图表）+辐射标注线；对比页左右分裂布局，中部用强调色标记关键差异；总结页三列纵向矩阵+底部色带放置收束要点。所有页面共享同一网格与配色体系，页间通过内容密度与构图家族变化保持节奏，无相邻重复。

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters

## page_types
- 封面页：标题与副标题居中的开篇页
- 目录页：逐条列出章节的学习路径页
- 内容页：以要点分条讲解概念的主体页
- 图文页：示意图标与说明文字并重的解释页
- 数据页：以数字、公式或图表为主的证据页
- 对比页：左右或表格式的对照分析页
- 总结页：收束要点与行动建议的结尾页
