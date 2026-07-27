---
name: ppt-master
description: 教学版 NotebookLM 的唯一 PPT 生产技能。依据教师确认大纲和课程资料，由大模型完成设计、逐页 SVG、备注与可编辑 PPTX 所需内容。
---

# PPT Master（应用运行版）

本技能由 WorkBuddy `Mo-PPT生成（大语言模型版）` 精简适配而来。应用已经完成资料摄入、大纲生成和教师确认；本技能只负责确认后的视觉与内容执行。

## 最高优先级应用覆盖

1. `confirmed_outline.md` 是页数、页码、页序、页标题和教学意图的唯一真源，不得增删、合并、拆分或重排。
2. 跳过原技能的 Eight Confirmations、确认网页、模板选择、实时预览编辑器和浏览器交互。模式、视觉风格、配色、字体、布局、节奏、图标、图表由大模型自动判断。
3. 本次生成不使用任何图片。禁止 `ai`、`web`、`slice`、`user`、远程 URL、data URI、`asset://` 和虚构文件；不得输出 `<image>`，也不得写图片合同或图片字段。
4. 每次 Executor 调用只生成一页。应用可在冻结设计锁后，把不同页面放入互相隔离的目录并固定最多并发 2 页；每页开始前仍必须重新读取 `spec_lock.md`，不得读取或修改其它页。
5. Agent 只使用技能读取、项目文件读写和受控图标搜索工具。不得执行 Shell、Python、网络、浏览器、图片生成或图片搜索。
6. Python 脚本只由应用以固定参数依次执行：`total_md_split.py` → `finalize_svg.py` → `svg_to_pptx.py`。
7. `svg_output/` 是可编辑 PPTX 的作者源；`svg_final/` 是图标已内嵌的网页预览源。

完整应用合同见 [`references/application-runtime.md`](references/application-runtime.md)。当该文件与保留的上游 Strategist / Executor 参考发生冲突时，以应用合同和本文件为准。

## 标准项目结构

```text
sources/course_material.md
confirmed_outline.md
design_spec.md
spec_lock.md
deck_manifest.json
svg_output/
svg_final/
notes/
exports/
```

## 受控工作流

### 1. Strategist

必须读取：

- `references/application-runtime.md`
- `references/strategist.md`
- `templates/design_spec_reference.md`
- `templates/spec_lock_reference.md`
- `templates/charts/charts_index.json`
- `templates/icons/README.md`

输出：

- `design_spec.md`：完整设计叙事与逐页内容展开。
- `spec_lock.md`：模式、视觉风格、全局版式原则、颜色、字体、图标、页面节奏和图表的执行锁。
- `deck_manifest.json`：严格对应确认大纲的逐页执行清单；每页必须包含从 `design_spec.md` 承接的具体 `layout`。

允许 `mode: custom`、`visual_style: custom`、自定义 HEX、自定义 PPT 安全字体栈和自定义页面节奏。`spec_lock.md ## layout` 必须锁定整份课件的版式原则和跨页变化规则；`design_spec.md` 的每页 Layout 必须同步写入 `deck_manifest.slides[].layout`，不能只留在人类可读说明中。`#FFFFFF` 是应用保留基础色。图表名必须存在于图表索引；图标必须由 Strategist 通过受控搜索验证，并把每页实际使用的完整 `library/name` 写入 `deck_manifest.iconRefs`。不得写 `spec_lock.md ## images` 或任何图片字段。

### 2. Executor

每次调用只执行当前页；应用层可对隔离目录固定并发 2：

1. 重新读取 `spec_lock.md`。
2. 使用应用提示中已经压缩好的本页 `deck_manifest` 内容与 `layout`、全局版式合同、锁定模式和视觉风格的具体参考、允许颜色、字体和图标；不要再读取完整课程资料或其它页面。
3. 仅在本页有锁定图表时读取对应图表 SVG；Executor 不再搜索图标。
4. 只生成当前页完整 SVG 到隔离目录的 `svg_output/<页码>.svg`。
5. 失败时只读取当前 SVG、执行锁和校验错误，按原 `layout` 完整重写本页；不得把修复降级成通用卡片网格，不得重新走整套资料分析，最多 3 次。

SVG 必须：

- 使用 `xmlns="http://www.w3.org/2000/svg"` 和 `viewBox="0 0 1280 720"`。
- 只使用 `spec_lock.md` 中的 HEX 与字体。
- 图标只用 `<use data-icon="库/名称" x="..." y="..." width="..." height="..." fill="#允许的六位HEX"/>`，名称必须在锁定库存中。六个属性必须直接写在自闭合 `<use>` 自身；尤其不得省略 `fill`，不得依赖父级 `<g>`、`currentColor`、`style` 或继承，也不得写 `href` / `xlink:href`。
- 禁止 `foreignObject`、`script`、`style`、动画、远程资源和普通 `<use href>`。

### 3. 质量修复

应用运行 `svg_quality_checker.py`。如有错误，应用只提取报告中的错误页，为每页建立仅含 `spec_lock.md` 和当前 SVG 的隔离目录，并固定最多并发 2 页轻量重写；不要读取质量脚本、报告文件、其它页面或其它项目资料。全部错误清零后才能生成备注。

### 4. 备注与导出

- 写 `notes/total.md`，每页都有讲解重点、过渡语和适合时的提问／提醒。
- 应用依次拆分备注、生成自包含 `svg_final/`、从 `svg_output/` 导出原生 DrawingML PPTX。
- 任一必需页面、备注、质量检查或导出失败，整份任务失败。

## 保留参考

- Strategist：`references/strategist.md`
- Executor：`references/executor-base.md`
- SVG/PPT 约束：`references/shared-standards.md`
- 模式：`references/modes/`
- 视觉风格：`references/visual-styles/`
- 图表：`templates/charts/`
- 图标：`templates/icons/`
- 设计合同：`templates/design_spec_reference.md`、`templates/spec_lock_reference.md`
