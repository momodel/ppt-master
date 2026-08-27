<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock: Humanities Narrative Warm Paper

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- audience: 通识课或人文学科的听众
- objective: 以叙事方式展开讲解，建立理解与共情
- core_message: 由确认大纲决定
- consumption_mode: balanced

## mode
- mode: narrative

## visual_style
- visual_style: editorial

## colors
- background: #FDF6E3
- secondary_bg: #F3EAD0
- primary: #C45A2C
- accent: #7A8B6F
- secondary_accent: #5B7C99
- body_text: #3D2B1F

## typography
- font_family: "Microsoft YaHei", "Segoe UI", sans-serif
- title_family: "STSong", "SimSun", Georgia, serif
- body_family: "Microsoft YaHei", "Segoe UI", sans-serif
- annotation_family: "STKaiti", "Microsoft YaHei", serif
- body: 24
- title: 42
- subtitle: 32
- lead: 28
- annotation: 18
- footnote: 15

## icons
- library: phosphor-duotone
- inventory: book-open, quotes, book-open-text, map-pin, calendar-blank

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
- 72px 宽外安全边距（比常规更宽松，强调留白呼吸感）；米色纸质底不使用网格线或分隔线；标题左对齐位于 72–140px，primary 色 6px 圆点前缀；主体内容区 140–620px；引用文本使用 annotation_family 斜体感（通过 STKaiti 模拟）；正文 #3D2B1F 深棕在米色底上确保对比度。
### variation
- 封面页全幅米色底，primary 色大号衬线标题居左，底部一条 2px accent 色细线 + 作者/课程名；内容页标题+大段正文，标题用 serif 大字，正文用 sans-serif 分条；引用页全页引文排版，大引号符号 accent 色装饰，引文正文 annotation_family 居中；对照页双栏分裂，中间 1px primary 色竖线分隔，左右各一个主题+说明列表；结语页大留白居中，primary 色「结语」二字 + 一句收束文本。

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters

## page_types
- 封面页：米色底衬线大标题的开篇页
- 目录页：章节列表配序号的导读页
- 内容页：要点分条的讲解正文页
- 引用页：大引号装饰的原文引述页
- 对照页：双栏对照的主题分析页
- 结语页：留白居中的收束寄语页
