# Locked Templates（冻结模板库）

教学版 NotebookLM 应用验收通过的设计合同模板。每套模板冻结一套完整视觉合同（`design_spec.md` + `spec_lock.md`）与节奏／页面类型／图标参数（`meta.json`）；生成期选定一套直接定死使用，不做自由设计。

## 使用方式

选择、落盘与适配规则由 [`references/locked-template-contract.md`](../references/locked-template-contract.md) 定义：第一层（主 Agent）按规则选模板并逐字落盘，第二层（页面 Worker）按落盘后的 `spec_lock.md` 执行。应用代码不做模板选择与节奏适配。

## 每套文件

| 文件 | 说明 |
|---|---|
| `meta.json` | 模板身份与冻结参数（字段见 locked-template-contract.md） |
| `design_spec.md` | 冻结视觉设计说明（逐字落盘，禁止修改） |
| `spec_lock.md` | 冻结执行锁（仅 `## page_rhythm` 允许按实际页数循环展开） |

## 当前模板

keji-jiangjie-v1、shuxue-jihe-v1、ketang-hudong-v1、renwen-xushi-v1、shangwu-baogao-v1、xueshu-jianding-v1、chanpin-fabu-v1、lishi-dangan-v1（各模板学科场景与节奏参数见其 `meta.json`）。

入库要求：明确构图语言（非通用安全词）、无图片资源、`pptx_structure.mode: flat`、`rhythmPattern` 可循环展开到任意页数、`pageTypes` 覆盖大纲常见页面角色。
