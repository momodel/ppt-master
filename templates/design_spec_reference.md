# {project_name} - Design Spec

> Human-readable design narrative. `spec_lock.md` is the machine-readable execution contract and wins if the two diverge.
> The application has already obtained teacher approval for `confirmed_outline.md`; all design values below are chosen automatically by the model.

## I. Project Information

| Item | Value |
| --- | --- |
| Project Name | {project_name} |
| Canvas Format | PPT 16:9, 1280 × 720 |
| Page Count | [must equal confirmed outline] |
| Target Audience | [derive from course material and outline] |
| Use Case | Classroom teaching |
| Content Boundary | Facts only from `sources/course_material.md`; page order and titles from `confirmed_outline.md` |
| Design Intent | [one concise paragraph] |

## II. Canvas Specification

| Property | Value |
| --- | --- |
| Dimensions | 1280 × 720 |
| viewBox | `0 0 1280 720` |
| Safe Margins | [model decision] |
| Content Area | [calculated values] |

## III. Visual Theme

### Narrative and Style

- Mode: [preset id or `custom`]
- Mode behavior: [required only for `custom`]
- Visual style: [real preset id or `custom`]
- Visual style behavior: [required only for `custom`; describe shape, density, whitespace, typography character, and texture without HEX]
- Tone: [teaching tone]

### Color Scheme

The model selects the palette directly. List only colors that will actually appear in SVG pages.

| Role | HEX | Purpose |
| --- | --- | --- |
| Background | `#......` | Main page background |
| Secondary background | `#......` | Secondary regions |
| Primary | `#......` | Titles and structural emphasis |
| Accent | `#......` | Key data and teaching emphasis |
| Secondary accent | `#......` | Secondary emphasis |
| Body text | `#......` | Main text |
| Secondary text | `#......` | Captions and annotations |
| Border/divider | `#......` | Separators and outlines |

## IV. Typography System

All sizes are unitless px numbers. Every recurring semantic role uses one locked size deck-wide.

### Font Plan

| Role | Font stack | Usage |
| --- | --- | --- |
| Default/body | [PPT-safe stack] | Body content |
| Title | [PPT-safe stack] | Page and section titles |
| Emphasis | [PPT-safe stack or same as body] | Quotes and emphasis |
| Code | [PPT-safe monospace stack] | Code only |

Every stack must end in a PowerPoint-safe installed family such as `Microsoft YaHei`, `SimSun`, `Arial`, `Times New Roman`, or `Consolas`.

### Size Roles

| Role | Size | Notes |
| --- | --- | --- |
| body | [number] | Required baseline |
| title | [number] | Page title |
| subtitle | [number] | Subtitle or section lead |
| annotation | [number] | Chart labels and annotations |
| footnote | [number] | Page number or source note |
| [additional recurring role] | [number] | Add when required by the outline |

## V. Layout and Rhythm

### Deck-wide principles

- [grid and alignment strategy]
- [whitespace and density strategy]
- [shape and divider strategy]
- [how charts, icons, and provided images integrate]
- [how repetitive card grids are avoided]

### Page rhythm vocabulary

- `anchor`: cover, section node, or final landing page.
- `dense`: comparisons, data, procedures, or multi-point explanation.
- `breathing`: one idea, key question, quote, or visual pause.
- Custom rhythm: allowed when the model names it and writes its executable layout, density, whitespace, and narrative behavior into `spec_lock.md ## rhythm_behaviors`.

Every page must receive exactly one rhythm in `spec_lock.md`.

## VI. Icon System

- Primary library: [one of `chunk-filled`, `tabler-filled`, `tabler-outline`, `phosphor-duotone`, or `none`]
- Stroke width: [only for `tabler-outline`]
- Brand library: [`simple-icons` only when a real brand appears, otherwise omit]
- Approved inventory: [only exact names returned by controlled icon search]
- Usage rules: [size, color, and semantic consistency]

If icons do not improve comprehension, write `none` and omit the icon lock.

## VII. Visualization Reference List

Only include pages that actually require a data chart, process diagram, timeline, matrix, framework, or other structured visualization.

| Page | Visualization | Source facts/data | Template basename | Adaptation plan |
| --- | --- | --- | --- | --- |
| P## | [type] | [exact course-material basis] | [real name from `charts_index.json` or `no-template-match`] | [how to render accurately] |

Never invent a chart template name. `no-template-match` means the model will construct the visualization using native SVG primitives.

## VIII. Confirmed Content Outline

Add one subsection per confirmed page. Keep page number, page order, title, and teaching intent verbatim.

### Slide 01 - [confirmed title]

- Teaching intent: [confirmed intent]
- Core message: [one assertion sentence]
- Rhythm: `anchor` / `dense` / `breathing`
- Layout: [specific composition: name the major regions, their relationship, visual focal point, and whitespace; copy this intent into the matching `deck_manifest.slides[].layout`]
- Content blocks: [fully expanded content based on course material]
- Visualization: [real chart basename, `native-svg`, or `none`]
- Icons: [approved icon names or `none`]
- Transition: [connection to next confirmed page]

Repeat until every confirmed page is represented exactly once.

Every per-slide `Layout` is an execution contract, not commentary. The matching `deck_manifest.slides[].layout` must carry the same composition intent so an isolated Executor can implement it without reading this file.

## IX. Speaker Notes Requirements

`notes/total.md` must contain one section per page in the same order, including:

- explanation emphasis;
- transition sentence;
- optional classroom question or teaching reminder when appropriate.

## X. Technical Constraints Reminder

1. SVG uses `xmlns="http://www.w3.org/2000/svg"` and `viewBox="0 0 1280 720"`.
2. Text wrapping uses `<tspan>`; `foreignObject`, `<style>`, classes, scripts, animation, iframe, `textPath`, and `@font-face` are forbidden.
3. Colors and fonts must come from `spec_lock.md`; `rgba()` is forbidden.
4. Images are not supported: do not write `<image>`, image contracts, image fields, image paths, remote URLs, data URIs, or `asset://`.
5. Icons use `<use data-icon="library/name" .../>` and must exist in the locked inventory.
6. Arbitrary `<use href>` and fabricated resource names are forbidden.
7. `svg_output/` is the native editable PPTX source; `svg_final/` is the self-contained preview source.
