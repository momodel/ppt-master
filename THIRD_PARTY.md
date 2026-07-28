# 教学版 NotebookLM 的 PPT Master 来源记录

- 官方上游：`hugohe3/ppt-master`
- 团队 fork：`momodel/ppt-master`
- Skill 分支：`codex/notebooklm-edu-skill`
- 上游目录：`skills/ppt-master/`
- 应用内技能名称：`ppt-master`

## 管理方式

`momodel/ppt-master:main` 是 `hugohe3/ppt-master:main` 的纯净镜像。`codex/notebooklm-edu-skill` 分支根目录即 `skills/ppt-master/` 的完整内容，叠加教学版 NotebookLM 的平台适配。

教学版 NotebookLM 通过 Git submodule 固定引用 skill 分支的具体 commit；构建和部署不追踪浮动分支。升级时只更新 submodule 指针和 `skills-lock.json`，不在应用仓库手工修改 Skill 文件。

## 当前应用适配

当前生成链路保持不变：教师先确认完整逐页大纲，随后运行唯一的 `pptMaster` 工作流。平台合同覆盖上游的多路线确认、图片获取、实时预览和 Shell 步骤；PPT 固定不使用任何图片，Agent 不获得 Shell 或网络工具，Python 只由应用以固定参数执行。

## 更新流程

1. 将 `momodel/ppt-master:main` 同步到 `hugohe3/ppt-master:main` 最新提交。
2. 把 main 的 `skills/ppt-master/` 变动合入 `codex/notebooklm-edu-skill`，处理与平台适配的冲突。
3. 在 `momodel/notebooklm-edu` 运行 `pnpm --dir server skill:ppt-master:update`。
4. 审查 submodule 指针与 lock 变化，运行兼容测试后合并。
