# Artifact Ownership Specification（应用运行版）

每类事实只从一个拥有者读取，不得建立第二份互相漂移的真源。

## Ownership Matrix

| Artifact | Owns | Contract |
| --- | --- | --- |
| `sources/course_material.md` | 课程事实、数据、案例和术语 | Strategist 与 Executor 的唯一内容事实来源 |
| `confirmed_outline.md` | 页数、页码、页序、页标题、教学意图 | 不得增删、合并、拆分、重排或改写标题 |
| `design_spec.md` | 人类可读的整体设计叙事和逐页内容展开 | Strategist 写，后续角色读 |
| `spec_lock.md` | 颜色、字体、图标、节奏和图表的字面执行值 | Executor 每页开始前重读；与设计叙事冲突时本文件优先 |
| `deck_manifest.json` | 与确认大纲一一对应的页面执行清单，包含每页具体 `layout` | 页面数量、顺序和版式意图不得变化 |
| `templates/charts/` | 可用图表模板 | 只能使用索引中真实存在的模板 basename |
| `templates/icons/` | 可用图标文件 | 只能使用受控搜索返回并写入锁的真实文件 |
| `svg_output/` | 大模型逐页生成的作者源 | 质量检查和原生 DrawingML PPTX 读取此目录 |
| `notes/total.md` | 全部讲者备注的作者源 | 页面数量和顺序必须与 deck manifest 一致 |
| `notes/slide_*.md` | 拆分后的逐页备注 | 由 `total_md_split.py` 从 `notes/total.md` 派生 |
| `svg_final/` | 图标和教师原图已内嵌的自包含预览 | 由 `finalize_svg.py` 从 `svg_output/` 重建，不在此目录直接修页 |
| `exports/` | 最终 PPTX | 由 `svg_to_pptx.py` 固定参数导出 |

## Invariants

- 内容事实只来自 `course_material.md`，页面边界只来自 `confirmed_outline.md`。
- `design_spec.md` 解释设计；`spec_lock.md` 执行设计。
- `svg_output/` 是唯一页面作者源；任何修复都先改这里，再重新生成 `svg_final/` 和 PPTX。
- `svg_final/` 是可丢弃派生物，必须能够完全重建。
- 原生 PPTX 从 `svg_output/` 导出；网页预览从 `svg_final/` 读取。
- 应用运行 Python；Agent 不执行 Shell、网络、浏览器或图片工具。

## Regeneration

| Derived artifact | Regenerate from | Application command |
| --- | --- | --- |
| `notes/slide_*.md` | `notes/total.md` | `total_md_split.py` |
| `svg_final/` | `svg_output/` and local assets | `finalize_svg.py` |
| Native PPTX | `svg_output/`, notes, and local assets | `svg_to_pptx.py` |
