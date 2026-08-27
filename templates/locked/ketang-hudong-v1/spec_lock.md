<!-- ppt-master-schema: spec-lock/v1 -->
# Execution Lock: Workshop Interactive

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## communication
- audience: 课堂学习者（小组或全班）
- objective: 以提问与互动驱动学习
- core_message: 由确认大纲决定
- consumption_mode: balanced

## mode
- mode: instructional

## visual_style
- visual_style: soft-rounded

## colors
- background: #FFF8F0
- secondary_bg: #FFE8D6
- primary: #E76F51
- accent: #2A9D8F
- secondary_accent: #264653
- body_text: #333333

## typography
- font_family: "Microsoft YaHei", "Segoe UI", sans-serif
- title_family: "Microsoft YaHei", "Segoe UI", sans-serif
- body_family: "Microsoft YaHei", "Segoe UI", sans-serif
- annotation_family: "Microsoft YaHei", "Segoe UI", sans-serif
- body: 26
- title: 44
- subtitle: 32
- lead: 28
- annotation: 18

## icons
- library: phosphor-duotone
- inventory: hand-pointing, users-three, magic-wand, check-circle, brain

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
- 56px 外安全边距；米色暖底；标题左对齐，primary 色圆角标签前缀；主体区使用圆角卡片（12px）配 secondary_bg 底色；提问/讨论用 accent 色高亮框；正文 #333333 暖底可读。
### variation
- 封面页暖底大标题+底部互动提示色带；提问页大号问题文字居中+accent 色问号装饰+底部提示；讨论页左右双栏分组卡片+accent 色连接箭头；练习页编号任务列表+每条 secondary_bg 卡片+状态标记；总结页三列收获卡片+底部行动建议。

## forbidden
- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters

## page_types
- 封面页：暖底大标题的互动开篇页
- 目录页：编号列表的学习路线页
- 提问页：大字提问与提示的启发页
- 讨论页：双栏分组卡片的互动页
- 练习页：任务卡片列表的操作页
- 总结页：收获卡片与建议收束页
