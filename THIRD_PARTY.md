# 教学版 NotebookLM 的 PPT Master 来源记录

- 官方上游：`hugohe3/ppt-master`
- 团队 fork：`momodel/ppt-master`
- 平台集成分支：`codex/notebooklm-edu-integration`
- Skill 发布分支：`codex/notebooklm-edu-skill`
- 上游目录：`skills/ppt-master/`
- 应用内技能名称：`ppt-master`

## 管理方式

`codex/notebooklm-edu-integration` 从 fork 的 `main` 接收官方更新，并只在 `skills/ppt-master/**` 内维护教学版 NotebookLM 的必要适配。每次该目录更新后，GitHub Actions 会把它发布为根目录即 Skill 内容的 `codex/notebooklm-edu-skill` 分支。

教学版 NotebookLM 通过 Git submodule 固定引用发布分支的具体 commit；构建和部署不追踪浮动分支。升级时只更新 submodule 指针和 `skills-lock.json`，不在应用仓库手工修改 Skill 文件。

## 当前应用适配

当前生成链路保持不变：教师先确认完整逐页大纲，随后运行唯一的 `pptMaster` 工作流。平台合同覆盖上游的多路线确认、图片获取、实时预览和 Shell 步骤；PPT 固定不使用任何图片，Agent 不获得 Shell 或网络工具，Python 只由应用以固定参数执行。

## 更新流程

1. 将 fork 的 `main` 同步到官方上游最新提交。
2. 把 `main` 合入 `codex/notebooklm-edu-integration`，只处理与平台适配真正重叠的冲突。
3. 推送集成分支；发布工作流更新 `codex/notebooklm-edu-skill`。
4. 在 `momodel/notebooklm-edu` 运行 `pnpm --dir server skill:ppt-master:update`。
5. 审查 submodule 指针与 lock 变化，运行兼容测试后合并。
