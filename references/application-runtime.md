# 教学版 NotebookLM PPT 运行合同

本文件是应用适配层，对保留的 WorkBuddy Strategist / Executor 参考具有覆盖优先级。

## 已由应用完成

- 项目资料已经转换并写入 `sources/course_material.md`。
- 教师已经确认完整逐页大纲，原文位于 `confirmed_outline.md`。
- 应用已经建立项目目录、任务状态、取消信号和总超时。
因此不要重新处理来源、询问用户、启动确认 UI、选择品牌模板或创建项目。

## 大模型决策范围

大模型自主决定并锁定：

- 内容如何从资料展开到每页；
- 模式和视觉风格，可使用 `custom`；
- HEX、字体栈、字号、留白、布局与页面节奏；
- 图标是否使用、使用哪些真实文件；
- 图表是否使用、使用哪个真实模板；

代码不得替大模型选择上述方案，只验证合同和资源真实性。

图片不是设计选项：本应用固定不使用任何图片。

## 不可改变的内容

- `confirmed_outline.md` 的页数、页码、顺序、页标题和教学意图。
- 课程事实只能来自 `sources/course_material.md`。
- `deck_manifest.json.slides` 必须逐项对应确认大纲，每页 `layout` 必须完整承接 `design_spec.md` 对该页规划的构图、区域关系、视觉焦点与留白。
- `spec_lock.md ## layout` 必须包含 `principles` 和 `variation`：前者锁定全局网格、对齐、形状与留白原则，后者约束跨页构图变化，避免相邻页面机械重复。

## 图片合同

- 本应用固定不使用任何图片。`design_spec.md` 不写图片资源列表，`spec_lock.md` 不得包含 `## images` section，`deck_manifest.json` 不得包含图片字段，页面 SVG 不得包含 `<image>`。
- 禁止 `ai`、`web`、`slice`、`user`、远程 URL、data URI、`asset://` 和虚构文件。

## 图标与图表合同

- 图标只能来自 Strategist 阶段的 `search_ppt_icons` 返回值，并在 `spec_lock.md ## icons` 锁定；每页实际使用的完整 `library/name` 同时写入 `deck_manifest.iconRefs`，Executor 不再重复搜索。
- 每个图标占位符必须把 `data-icon`、`x`、`y`、`width`、`height`、`fill` 直接写在自闭合 `<use>` 自身；`fill` 不得从父级、`currentColor`、`style` 或继承获得。生成提示和错误页重写提示都必须内联这条完整语法。
- 通用图标整份只用一套库；`simple-icons` 仅用于正文真实出现的品牌。
- 图表模板名必须存在于 `templates/charts/charts_index.json`，并按需读取对应 SVG。
- 不得把代码提供的候选当作设计推荐；搜索结果只是存在性证明，最终选择由大模型做出。

## Agent 工具边界

可用：技能读取、项目文件读取／列出／搜索、项目文件写入、受控图标搜索。

不可用：Shell、任意代码执行、网络、浏览器、图片生成、图片搜索、图片切片、音频、PPTX 美化、品牌模板。

## 隔离并发与状态

- 同一个任务 Agent 可通过项目文件状态连续调用。
- `spec_lock.md` 是每页开始时必须重读的执行真源。
- 应用把锁定模式与视觉风格的具体参考、全局版式合同和当前页 `layout` 直接预加载到逐页请求；Executor 不需要自行查找，也不得忽略或退化这些合同。
- Strategist 完成后，应用为每页建立只包含执行锁和本页输出目录的隔离工作区，固定最大并发数为 2；结果仍按 `01.svg`、`02.svg`……顺序汇总。
- 单页校验失败时使用当前 SVG、执行锁和当前页错误片段做轻量完整重写，最多 3 次；页面技能激活不附带无关资源目录索引，模型网络重试不占内容重写次数。
- 全部页面完成后先质量检查；报告中的错误页继续使用仅含执行锁和当前 SVG 的隔离目录，固定最多并发 2 页、最多 6 个模型步骤轻量修复，不让 Agent 查找质量脚本或扫描全项目。复检通过后再生成备注，最后由应用运行固定 Python 导出链。
