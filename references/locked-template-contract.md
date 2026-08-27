# 冻结模板设计合同（Locked Design Contract）

本文件是教学版 NotebookLM 应用适配层：设计合同（`design_spec.md` + `spec_lock.md`）不再由大模型自由设计，而是**直接由冻结模板库定死**。它规定第一层（主 Agent）如何选择并落盘模板、第二层（页面 Worker）如何按落盘合同执行，并覆盖 skill 内一切「大模型自主决定视觉语言」的描述。

## 两层职责

- **第一层（主 Agent）**：读取模板库，依据大纲主题选一套模板，按本文件规则逐字落盘；允许的确定性适配只有节奏页数展开与逐页版式映射。
- **第二层（页面 Worker）**：以落盘后的 `spec_lock.md` 与本页 `layout`、`rhythm`、`layoutTemplate` 为执行真源，只写本页 SVG；不得重新选择模板或改动视觉合同。

## 模板库位置与构成

`templates/locked/<template-id>/`，每套三个文件：

- `meta.json`：模板身份与冻结参数。字段：`id`、`title`、`description`、`styleId`、`layoutPack`（presentation_core / editorial_bleed / report_core 之一）、`sourceCommit`、`rhythmPattern`（可循环节奏模式）、`pageTypes`（允许的页面类型 ID）、`iconRefs`（冻结图标库存，`library/name`）、`subjects`（适用场景标签）。
- `design_spec.md`：冻结的视觉设计说明，逐字落盘。
- `spec_lock.md`：冻结的执行锁（canvas、communication、mode、visual_style、colors、typography、icons、page_rhythm、pptx_structure、layout、forbidden、page_types）。

## 模板选择（第一层职责）

1. 读取 `templates/locked/` 下全部 `meta.json`。
2. 用 `confirmed_outline.md` 的主题与 `sources/course_material.md` 的学科匹配各模板 `subjects` 标签：命中数最多者胜出；平局按下述固定顺序。
3. 无明确命中时回退 `keji-jiangjie-v1`（通用）。
4. 选择一经确定不得更换；整份课件共用一套冻结核同，禁止中途换模板或混用两套视觉体系。

固定顺序（平局／回退用）：keji-jiangjie-v1、shuxue-jihe-v1、ketang-hudong-v1、renwen-xushi-v1、shangwu-baogao-v1、xueshu-jianding-v1、chanpin-fabu-v1、lishi-dangan-v1。

## 落盘规则（定死）

选定模板后：

1. 将 `design_spec.md` 与 `spec_lock.md` **逐字**写入项目目录根。禁止修改其中任何视觉身份段落（mode、visual_style、colors、typography、layout principles、forbidden）。
2. 唯一允许的机械适配：把 `## page_rhythm` 段落替换为 `meta.json.rhythmPattern` 按实际页数循环展开的 `P01..Pnn` 序列。例：pattern 为 [anchor, dense, dense, breathing, anchor]、共 8 页时，P06=anchor、P07=dense、P08=dense。
3. `spec_lock.md` 缺少 `## page_types` 段落时按 `meta.json.pageTypes` 补写；已存在则不动。
4. 在项目目录写入 `selected-template/design_spec.md` 与 `selected-template/spec_lock.md` 同内容归档（只读参照）。

## 逐页版式映射（deck_manifest.json）

- `slides` 与 `confirmed_outline.md` 逐页对应；页码、页序、页标题、教学意图不可改变。
- 每页 `layout` 必须从 `meta.json.pageTypes` 中选一个页面类型 ID。
- 每页 `layoutTemplate` 按「页面类型角色 → 布局母版」映射（布局包取 `meta.json.layoutPack`）。角色判定：页面类型 ID 含下表关键词即取该角色，多词命中取表中靠前角色，均不命中取 content：

| 角色 | 判定关键词 | presentation_core | editorial_bleed | report_core |
|---|---|---|---|---|
| cover | 封面、开篇 | 01_title_slide.svg | 01_hero_full.svg | 01_cover.svg |
| toc | 目录、议程、路线 | 03_section_header.svg | 07_triptych.svg | 03_agenda.svg |
| section | 章节、过渡 | 03_section_header.svg | 05_chapter_full.svg | 02_section_divider.svg |
| data | 数据、图表、证据、指标 | 19_chart_insight.svg | 07_triptych.svg | 08_chart_insight.svg |
| compare | 对比、矩阵 | 05_comparison.svg | 08_image_grid_four.svg | 11_matrix_2x2.svg |
| quote | 引用、金句 | 10_hero_statement.svg | 06_quote_over_image.svg | 06_three_block.svg |
| ending | 总结、结尾、收束 | 10_hero_statement.svg | 10_closing_full.svg | 13_closing.svg |
| visual | 图文、图解、案例、视觉 | 08_content_caption.svg | 04_split_bleed_reverse.svg | 05_two_content.svg |
| content（默认） | 其余 | 02_title_content.svg | 03_split_bleed.svg | 04_title_content.svg |

- 布局母版路径统一写 `templates/layouts/<layoutPack>/templates/<文件名>`（相对 skill 根），经 `delegate_page_worker` 的 `layoutTemplate` 传给第二层。
- 布局母版只提供区域骨架；母版中的 `<image>` 占位已由应用侧复制时去除，Worker 不得自行添加任何图片。
- 每页 `rhythm` 取适配后 `spec_lock.md ## page_rhythm` 对应页码的值。
- 每页 `layout` 描述开头必须写 `构图家族：<模板 variation 中的命名>`，并承接模板 `spec_lock.md ## layout - variation` 对该构图家族的约定。

## 图标与图表

- 图标只能来自所选模板 `meta.json.iconRefs` 库存（格式 `library/name`）；`search_ppt_icons` 只用于验证文件存在，不是设计推荐。
- `spec_lock.md ## icons` 已冻结库存，不得增删；每页实际使用的图标写入 `deck_manifest.json.slides[].iconRefs`。
- 图表模板名必须存在于 `templates/charts/charts_index.json`。

## 禁止事项

- 不得自行设计或调整配色、字体、字号、模式、视觉风格、节奏模式。
- 不得引入第二套视觉体系；不得为「更美观」修改冻结核同。
- 不得改变页数、页序、页标题、教学意图。
- 不得在 `spec_lock.md` 写 `## images`；本应用不使用任何图片（见 `application-runtime.md`）。
