<!-- ppt-master-schema: design-spec/v1 -->
# 科技讲解 · 清爽学术风 - Design Spec

## I. Canvas Specification

| Property | Value |
|---|---|
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 60px outer |
| Content Area | 1160 × 600 (x:60–1220, y:60–660) |

## II. Visual Theme

### Theme Style

- **Mode**: instructional
- **Visual style**: blueprint
- **Theme**: 工程蓝图教学
- **Tone**: 精密、系统、学术工程感

### Color Scheme

| Role | HEX | Purpose |
|---|---|---|
| Background | #0D2740 | 深蓝纸面，蓝图底色 |
| Secondary background | #13405E | 面板/区域抬升色 |
| Primary | #4FC3F7 | 天蓝主强调：标题、标注线、坐标轴 |
| Accent | #FFB74D | 橙色高光：关键条件、采样点、警告 |
| Secondary accent | #81C784 | 绿色确认：正面结论、验证通过 |
| Body text | #E0E0E0 | 浅灰正文，深底可读 |

### Color Usage Rules

- 标题使用 primary 色加粗 + 白色正文
- 关键条件/公式/警告用 accent 橙色
- 正面确认/验证结论用 secondary_accent 绿色
- 蓝图网格线用 secondary_bg 色（#13405E）
- 正文浅灰 #E0E0E0 确保深底可读

### Typography

| Property | Value |
|---|---|
| Title font | "Microsoft YaHei", "Segoe UI", sans-serif |
| Body font | "Microsoft YaHei", "Consolas", monospace, sans-serif |
| Annotation font | "Microsoft YaHei", "Consolas", monospace, sans-serif |
| Title size | 42px |
| Body size | 24px |
| Subtitle size | 32px |
| Lead size | 28px |
| Annotation size | 18px |

## III. Layout System

### Global Principles

- 60px 外安全边距
- 蓝图坐标网格背景（secondary_bg 色细线，间距 40px）
- 标题左对齐位于 60–130px
- 主体内容区 130–620px
- 所有线框、标注线、坐标轴使用 primary 色
- 关键条件/警告用 accent 色
- 正面确认用 secondary_accent 色

### Page Type Layouts

#### 封面页
- 全幅深蓝底 + 蓝图网格
- primary 色大标题居中
- 副标题浅灰居中
- 底部一条 accent 色色带 + 核心结论文字

#### 内容页
- 左文右图或左图右文交替
- 蓝图网格背景 + 标注线引出关键概念
- 正文分条排列，行间距 8px

#### 数据页
- 居中 hero 元素（公式/数字/图表）
- 辐射标注线连接相关解释
- 上下留白

#### 对比页
- 左右分裂布局
- 中部用 accent 色标记关键差异
- 两侧各一个观点 + 证据

#### 总结页
- 三列纵向矩阵
- 底部色带放置收束要点

## IV. Icon Policy

- Library: phosphor-duotone
- Inventory: waveform, wave-sine, math-operations, warning-circle, funnel, brain, check-circle
- 使用规则：仅用于要点行首或概念旁标注，尺寸 28×28px

## V. Forbidden

- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
