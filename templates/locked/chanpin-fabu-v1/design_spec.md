<!-- ppt-master-schema: design-spec/v1 -->
# 产品发布 · 深空展示风 - Design Spec

## I. Canvas Specification

| Property | Value |
|---|---|
| Format | PPT 16:9 |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Margins | 60px outer |
| Content Area | 1160 × 600 |

## II. Visual Theme

- **Mode**: custom
- **Visual style**: deep_space_showcase
- **Tone**: 深邃、聚焦、科技感

### Color Scheme

| Role | HEX | Purpose |
|---|---|---|
| Background | #0A0A1A | 深空黑底 |
| Secondary | #12122A | 卡片/面板底色 |
| Primary | #7B68EE | 紫色主强调（渐变起点） |
| Accent | #00D9FF | 青色高光（渐变终点） |
| Secondary accent | #FF6B9D | 粉色辅助 |
| Body text | #E8E8F0 | 浅紫白正文 |

## III. Layout System

- 60px 外安全边距
- 特性卡片 secondary_bg 底圆角 12px 配 1px accent 边框
- 对比面板左右分裂配 accent 分隔线
- 标题 primary->accent 渐变色文字

## IV. Icon Policy

- Library: phosphor-duotone
- Inventory: rocket-launch, star, sparkle, thumbs-up
