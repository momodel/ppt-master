<!-- ppt-master-schema: design-spec/v1 -->
# 课堂互动 · 活力教学风 - Design Spec

## I. Canvas Specification

| Property | Value |
|---|---|
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 56px outer |
| Content Area | 1168 × 608 |

## II. Visual Theme

- **Mode**: instructional
- **Visual style**: energetic_classroom
- **Tone**: 明快、互动、有课堂温度

### Color Scheme

| Role | HEX | Purpose |
|---|---|---|
| Background | #FFF8F0 | 暖米色底 |
| Secondary | #FFE8D6 | 面板/卡片底色 |
| Primary | #E76F51 | 珊瑚橙：标题标签、关键动作 |
| Accent | #2A9D8F | 青绿：提问、讨论、确认 |
| Secondary accent | #264653 | 深蓝灰：次级强调 |
| Body text | #333333 | 深灰正文 |

## III. Layout System

- 56px 外安全边距
- 圆角卡片（12px）配 secondary_bg 底色
- 提问/讨论用 accent 色高亮框
- 标题 primary 色圆角标签前缀

## IV. Icon Policy

- Library: phosphor-duotone
- Inventory: hand-raising, users-three, lightbulb, check-circle, brain
