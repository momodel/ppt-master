<!-- ppt-master-schema: design-spec/v1 -->
# Humanities Narrative Warm Paper - Design Spec

## I. Canvas Specification

| Property | Value |
|---|---|
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 72px outer (deliberately generous) |
| Content Area | 1136 × 576 (x:72–1208, y:72–648) |

## II. Visual Theme

### Theme Style

- **Mode**: narrative (story-driven, tension-turn-resolution)
- **Visual style**: warm_editorial
- **Tone**: 温和、典雅、有人文温度
- **References**: 文学讲义、人文通识课、博物馆解说

### Color Scheme

| Role | HEX | Purpose |
|---|---|---|
| Background | #FDF6E3 | 米色纸质底，营造温暖阅读感 |
| Secondary background | #F3EAD0 | 面板/引用区底色 |
| Primary | #C45A2C | 赭石/锈橙：标题前缀、关键词、装饰线 |
| Accent | #7A8B6F | 灰绿：引用装饰、次级强调 |
| Secondary accent | #5B7C99 | 灰蓝：时间标注、外部参照 |
| Body text | #3D2B1F | 深棕正文，米色底上确保可读 |

### Color Usage Rules

- 标题 primary 色圆点前缀 + 深棕标题文字
- 引用/装饰用 accent 灰绿
- 时间线/外部参照用 secondary_accent 灰蓝
- 正文深棕，不用纯黑
- 全文不使用高饱和色，保持纸质温和感

### Typography

| Property | Value |
|---|---|
| Title font | "STSong", "SimSun", Georgia, serif |
| Body font | "Microsoft YaHei", "Segoe UI", sans-serif |
| Annotation font | "STKaiti", "Microsoft YaHei", serif |
| Title size | 42px |
| Body size | 24px |
| Subtitle size | 32px |
| Annotation size | 18px |

## III. Layout System

### Global Principles

- 72px 宽外安全边距（强调留白）
- 标题左对齐，primary 色 6px 圆点前缀，位于 y 72–140px
- 主体内容区 y 140–620px
- 底部 y 620–672px 安静留白（不放页码或装饰）
- 米色纸质底不使用网格线、边框线
- 面板/引用区用 secondary_bg (#F3EAD0) 区块

### Page Type Layouts

#### 封面页
- 米色全幅底
- primary 色大号衬线标题 52px 左对齐（x=72, y=280）
- 副标题 28px 深棕
- 底部一条 2px accent 色细线（长 200px）+ 课程名/作者

#### 目录页
- 左侧 "目录" 二字用 serif 大字（primary 色，60px）
- 右侧章节列表，每条 primary 色序号 + 深棕章节名

#### 内容页
- 标题 primary 圆点前缀 + serif 标题
- 正文 sans-serif 分条，每条间距 12px
- 要点行首可用 accent 色小图标

#### 引用页
- 全页引文排版
- 大引号符号 accent 色（120px，装饰性）
- 引文正文 annotation_family（STKaiti 模楷体感）居中
- 引文下方左对齐出处标注

#### 对照页
- 双栏分裂布局
- 中间 1px primary 色竖线分隔
- 左右各一个主题标题 + 说明列表

#### 结语页
- 大留白居中
- primary 色 "结语" 二字（serif, 48px）
- 一句收束文本（annotation_family）

## IV. Icon Policy

- Library: phosphor-duotone
- Inventory: book-open, quote, feather, map-pin, calendar-blank
- 使用规则：仅用于要点行首装饰或引用页出处旁，尺寸 24×24px

## V. Forbidden

- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
- HTML named entities in text; write typography as raw Unicode and escape XML reserved characters
