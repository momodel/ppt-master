<!-- ppt-master-schema: design-spec/v1 -->
# 学术报告 · 白净简洁风 - Design Spec

## I. Canvas Specification

| Property | Value |
|---|---|
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 64px outer |
| Content Area | 1152 × 592 (x:64–1216, y:64–656) |

## II. Visual Theme

### Theme Style

- **Mode**: pyramid
- **Visual style**: academic_clean
- **Tone**: 严谨、克制、白纸感

### Color Scheme

| Role | HEX | Purpose |
|---|---|---|
| Background | #FFFFFF | 纯白纸面 |
| Secondary background | #F0F4F8 | 面板/数据区底色 |
| Primary | #1E3A5F | 深海军蓝：标题、底线、引文竖线 |
| Accent | #C0392B | 学术红：异常标记、关键发现 |
| Secondary accent | #276674A | 学院绿：正面确认、通过验证 |
| Body text | #2C3E50 | 深灰正文 |

### Typography

| Property | Value |
|---|---|
| Title font | "Microsoft YaHei", "Segoe UI", sans-serif |
| Body font | "Microsoft YaHei", "Segoe UI", sans-serif |
| Title size | 40px |
| Body size | 24px |

## III. Layout System

- 64px 外安全边距
- 标题左对齐，primary 色 3px 底线装饰
- 数据面板 secondary_bg 浅灰底圆角矩形
- 引文左侧 primary 竖线 + 斜体

## IV. Icon Policy

- Library: phosphor-duotone
- Inventory: file-text, magnifying-glass, graduation-cap, lightbulb

## V. Forbidden

- `mask`, `<style>`, `class`, external CSS, `<foreignObject>`, `<textPath`, `@font-face`, `<animate*>`, `<set>`, `<script>` / event attributes, `<iframe>`
