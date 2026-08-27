<!-- ppt-master-schema: design-spec/v1 -->
# Business Report Dark Professional - Design Spec

## I. Canvas Specification

| Property | Value |
|---|---|
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 48px outer |
| Content Area | 1184 × 624 (x:48–1232, y:48–672) |

## II. Visual Theme

### Theme Style

- **Mode**: pyramid (answer-first, evidence-led)
- **Visual style**: corporate_analytical
- **Tone**: 深沉、专业、数据驱动
- **References**: 咨询报告、商务汇报、决策文档

### Color Scheme

| Role | HEX | Purpose |
|---|---|---|
| Background | #1A1A2E | 深色石墨底，聚焦内容 |
| Secondary background | #16213E | 面板/区域抬升色 |
| Primary | #E94560 | 主强调：标题竖线、封面渐变起点、编号色 |
| Accent | #F5C518 | 金色高光：KPI 数字、关键结论、封面横线 |
| Secondary accent | #53C2C6 | 青色辅助：正面趋势、数据确认 |
| Body text | #D4D4D8 | 浅灰正文，深底可读 |

### Color Usage Rules

- 标题区域 primary 色竖线前缀 + 白色标题文字
- 数据面板 secondary_bg 底色圆角矩形，数字用 accent 金色
- 警告/风险用 primary 色标记
- 正面确认/推荐用 secondary_accent 青色
- 全文不使用纯白 (#FFFFFF) 正文，保持深色体系一致性

### Typography

| Property | Value |
|---|---|
| Title font | "Segoe UI", "Microsoft YaHei", sans-serif |
| Body font | "Segoe UI", "Microsoft YaHei", sans-serif |
| Annotation font | "Consolas", "Segoe UI", monospace |
| Title size | 40px |
| Body size | 22px |
| KPI number size | 48px |
| Annotation size | 16px |

## III. Layout System

### Global Principles

- 48px 外安全边距
- 标题左对齐，primary 色 4px 竖线前缀，位于 y 48–110px
- 主体内容区 y 110–650px
- 底部 y 650–672px 放置页码 + 章节标签 + primary 色 3px 横线
- 数据面板使用 secondary_bg (#16213E) 圆角 8px 矩形
- 面板间距 24px

### Page Type Layouts

#### 封面页
- 全幅 primary 色线性渐变背景（从 #E94560 到 #1A1A2E，135°）
- 白色大标题 56px 居中
- 副标题 28px 浅灰居中
- 底部一条 4px 金色 (#F5C518) 横线，长度 160px 居中

#### 目录页
- 左侧 30% 宽度放置 "目录" 竖排大字（primary 色）
- 右侧 70% 放置编号列表，每条 primary 色大编号 + 白色标题

#### 内容页
- 标题区 primary 竖线 + 白色标题
- 主体区域分条要点，每条 secondary_bg 底色圆角行
- 要点编号用 primary 色

#### 数据页
- 标题区同上
- 主体区域 KPI 面板矩阵（2×2 或 1×3）
- 每个面板 secondary_bg 底色，数字 48px accent 色，标签 18px 灰色
- 面板间距 24px

#### 对比页
- 标题区同上
- 主体左右分裂，中间 2px 分隔线 (#D4D4D8)
- 两侧各一个观点标题 + 证据列表

#### 结论页
- 标题区同上
- 主体三列卡片，顶部 primary 色编号大字
- 卡片 secondary_bg 圆角底
- 底部一条 accent 金色横线 + 行动建议文本

## IV. Icon Policy

- Library: phosphor-duotone
- Inventory: chart-bar, trend-up, target, lightbulb, warning, check-circle
- 使用规则：仅用于 KPI 面板标签旁或要点行首，尺寸 32×32px

## V. Chart Templates

- KPI 数字面板（不使用图表库，直接文本排版）
- 流程时间线（横向，节点用 accent 金色圆点）

## VI. Forbidden

- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
