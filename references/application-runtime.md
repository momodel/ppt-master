# 教学版 NotebookLM PPT 运行合同

本文件是应用适配层，对保留的 WorkBuddy Strategist / Executor 参考具有覆盖优先级。

## 已由应用完成

- 项目资料已经转换并写入 `sources/course_material.md`。
- 教师已经确认完整逐页大纲，原文位于 `confirmed_outline.md`。
- 应用已经建立项目目录、任务状态、取消信号和总超时。
- 应用已按课程主题**确定性套用**冻结模板设计合同：`design_spec.md`、`spec_lock.md`（节奏已按页数展开）在项目目录根，`selected-template/` 为只读归档（meta.json、layout-map.json、layouts/）。
因此不要重新处理来源、询问用户、启动确认 UI、选择模板或创建项目。

## 设计合同：模板库直接定死

设计合同（`design_spec.md` + `spec_lock.md`）由 skill 冻结模板库 `templates/locked/` **直接定死**：模板选择与落盘由应用在 Agent 启动前确定性完成（无模型调用），规则见 [`locked-template-contract.md`](./locked-template-contract.md)。大模型不再选择模板，不再设计模式和视觉风格、HEX、字体栈、字号、留白、布局与页面节奏；视觉身份以已套用模板的冻结核同为准，禁止修改。

大模型（主 Agent）自主决定并锁定：

- 内容如何从资料展开到每页；
- 每页 `layout` 从模板 `pageTypes` 中选哪个，并映射到 `selected-template/layout-map.json` 中的布局母版；
- 图标只从模板 `iconRefs` 库存中选择使用哪些；
- 图表是否使用、使用哪个真实模板。

模板选择与合同落盘是应用侧确定性代码的职责，Agent 不得重复或改写；其余方案由大模型决定，代码只验证合同和资源真实性。

图片不是设计选项：本应用固定不使用任何图片。

## 跳过视觉确认后的模板选择（应用确定性直出）

应用跳过八项视觉确认，模板选择由应用在 Agent 启动前按 [`locked-template-contract.md`](./locked-template-contract.md) 确定性完成，规则：

- 匹配 课程标题 + `confirmed_outline.md` + `sources/course_material.md` 全文与各模板 `subjects` 标签：先比**学科专属标签**命中数（排除场景泛用标签：通用、课堂、互动、实训、通识、展示），再比总命中数，平局按固定顺序（无命中回退 `keji-jiangjie-v1`）。
- “教学”“课程”“培训”“亲和”本身不是选择或更换某套模板的理由；选择依据只能是学科／场景标签与课程文本的匹配。
- 选定模板后整份课件共用其冻结核同；不得逐页或中途更换视觉体系，不得在模板之外“再设计”。
- 无图片约束只取消图片资源，不取消视觉表达：模板的排版、比例、线条、图标、图表与留白语言完整保留，不能用重复卡片填补原本可能放图片的位置。

## 不可改变的内容

- `design_spec.md` 与 `spec_lock.md` 必须逐字来自所选冻结模板（仅 `## page_rhythm` 允许按实际页数循环展开）；禁止自创或改写视觉合同段落。
- `confirmed_outline.md` 的页数、页码、顺序、页标题和教学意图。
- 课程事实只能来自 `sources/course_material.md`。
- `deck_manifest.json.slides` 必须逐项对应确认大纲，每页 `layout` 必须完整承接 `design_spec.md` 对该页规划的构图、区域关系、视觉焦点与留白。
- `spec_lock.md ## layout` 必须包含 `principles` 和 `variation`：前者锁定全局网格、对齐、形状与留白原则，后者约束跨页构图变化，避免相邻页面机械重复。
- `spec_lock.md ## pptx_structure` 必须写 `mode: flat`；不写 structured 映射段。
- `spec_lock.md ## canvas` 必须同时写 `viewBox` 和 `format`（如 PPT 16:9）。

## 跨页构图多样性

卡片可以作为局部信息容器，但不得成为整份课件的默认版式：

- 把卡片作为主构图的页面不得超过总页数的三分之一，且不得连续出现三页；仅改变卡片数量、横竖排列、圆角或底色不算新的构图。
- 四页及以上的课件必须在整份 `deck_manifest` 中使用至少三种真正不同的构图家族；九页及以上至少四种。构图家族自由命名，不受代码枚举限制，例如单焦点排版、编辑式分栏、时间线、流程／因果图、坐标／光谱、矩阵／表格、辐射关系、路径图、舞台式问答或非卡片对比。
- 每页 `layout` 的开头必须写 `构图家族：<自由命名>`，随后描述主要区域关系、视觉焦点和留白。相邻页面优先切换构图家族；同一构图家族再次出现时必须改变阅读路径或主导视觉关系。
- `spec_lock.md ## layout - variation` 必须按页码列出构图家族分配，明确哪些页允许以卡片为主。不得把“居中卡片、三张卡片、四张卡片、左右卡片”列为不同变化。
- 模板入库验收时已核对：其 `spec_lock.md ## layout - variation` 的构图家族分配满足上述要求；运行时禁止因“不满足”而改写或更换模板合同。

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
- 第一层完成后，应用为每页建立只包含执行锁和本页输出目录的隔离工作区，并发数由 `PPT_PAGE_CONCURRENCY` 控制（默认 4）；结果仍按 `01.svg`、`02.svg`……顺序汇总。
- 单页校验失败时使用当前 SVG、执行锁和当前页错误片段做轻量完整重写，最多 3 次；页面技能激活不附带无关资源目录索引，模型网络重试不占内容重写次数。
- 全部页面完成后先质量检查；报告中的错误页继续使用仅含执行锁和当前 SVG 的隔离目录，固定最多并发 2 页、最多 6 个模型步骤轻量修复，不让 Agent 查找质量脚本或扫描全项目。复检通过后再生成备注，最后由应用运行固定 Python 导出链。
