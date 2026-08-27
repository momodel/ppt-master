<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock: Academic Clean

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- audience: 学术评审者或课程学习者
- objective: 按确认大纲逐页展开讲解
- core_message: 由确认大纲决定
- consumption_mode: balanced

## mode
- mode: pyramid

## visual_style
- visual_style: swiss-minimal

## colors
- background: #FFFFFF
- secondary_bg: #F0F4F8
- primary: #1E3A5F
- accent: #C0392B
- secondary_accent: #27674A
- body_text: #2C3E50

## typography
- font_family: "Microsoft YaHei", "Segoe UI", sans-serif
- title_family: "Microsoft YaHei", "Segoe UI", sans-serif
- body_family: "Microsoft YaHei", "Segoe UI", sans-serif
- annotation_family: "Microsoft YaHei", "Segoe UI", sans-serif
- body: 24
- title: 40
- subtitle: 30
- lead: 26
- annotation: 16
- footnote: 14

## icons
- library: phosphor-duotone
- inventory: file-text, magnifying-glass, graduation-cap, magic-wand

## page_rhythm
- P01: anchor
- P02: dense
- P03: breathing
- P04: dense
- P05: anchor

## pptx_structure
- mode: flat

## layout
### principles
- 64px 外安全边距；白底不用网格线；标题左对齐位于 64–128px，primary 色 3px 底线装饰；主体内容区 128–620px；数据面板用 secondary_bg 浅灰底圆角矩形；引文使用左侧 primary 色竖线+斜体；正文 #2C3E50 白底可读。
### variation
- 封面页白底+大标题居中+底部学校/院系标注；内容页左文右图交替+primary 底线标题；数据页 KPI 面板矩阵或表格+accent 标记异常值；引用页左侧竖线引文+出处右对齐；总结页三列要点卡片+底部行动建议。

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters

## page_types
- 封面页：白底居中标题的学术开篇页
- 目录页：编号列表的研究路线页
- 内容页：要点分条的讲解主体页
- 数据页：数据面板或表格的证据页
- 引用页：左竖线引文与出处的参考页
- 总结页：要点卡片与结论收束页
