# Execution Lock

> Skeleton for Strategist. A project `spec_lock.md` contains only filled `##` sections and `- key: value` data lines.
> Executor must re-read it before every page. Values not listed here must not appear in generated SVG.

## canvas
- viewBox: 0 0 1280 720
- format: PPT 16:9

## mode
- mode: instructional

For `mode: custom`, add one filled `mode_behavior` line.

## visual_style
- visual_style: swiss-minimal

For `visual_style: custom`, add one filled `visual_style_behavior` line. Do not put HEX values in the behavior text.

## layout
- principles: 12-column grid; explicit alignment anchors; one dominant focal region; whitespace separates teaching hierarchy
- variation: Adjacent pages must not repeat the same card grid; alternate focal, split, sequence, comparison, and diagram compositions as content requires

Both lines are required. `principles` locks the deck-wide grid, alignment, shape, hierarchy, and whitespace logic. `variation` states how page compositions vary while staying in one visual system.

## colors
- bg: #FFFFFF
- secondary_bg: #F5F7FA
- primary: #......
- accent: #......
- secondary_accent: #......
- text: #......
- text_secondary: #......
- border: #......

Keep only colors actually used. All values are six-digit HEX.
`#FFFFFF` is an application-reserved base color and is always accepted by preflight; keep it listed when the design uses white.

## typography
- font_family: "Microsoft YaHei", Arial, sans-serif
- title_family: "Microsoft YaHei", Arial, sans-serif
- emphasis_family: Georgia, SimSun, serif
- code_family: Consolas, "Courier New", monospace
- body: 24
- title: 42
- subtitle: 32
- annotation: 18
- footnote: 16

All sizes are unitless px numbers. Add a named slot for every recurring semantic role. Every font stack must end in a PowerPoint-safe installed family.

## icons
- library: chunk-filled
- inventory: target, chart-bar, lightbulb

Allowed primary libraries: `chunk-filled`, `tabler-filled`, `tabler-outline`, `phosphor-duotone`. Use only exact names returned by controlled icon search. Add `stroke_width: 1.5|2|3` for `tabler-outline`. Add `brand_library: simple-icons` only when the course material contains a real brand. Omit this section when no icons are used.

Do not add an `## images` section. The application rejects all image contracts and `<image>` elements.

## page_rhythm
- P01: anchor
- P02: dense
- P03: custom-dialogue

Every page must appear exactly once. Common values are `anchor`, `dense`, and `breathing`; a custom value is allowed when it has a matching behavior below.

## rhythm_behaviors
- custom-dialogue: Alternating question and answer zones with generous center whitespace; one teaching prompt at a time, no card grid.

Omit this section when every page uses a common rhythm. Each custom rhythm name must have one concrete behavior line.

## page_charts
- P05: bar_chart

Only list chart basenames that exist in `templates/charts/charts_index.json`. Omit this section when no indexed chart template is used.

## forbidden
- Mixing primary icon libraries
- rgba()
- Remote URLs, data URIs, asset://, fabricated image paths
- AI-generated, web-sourced, sliced, formula-rendered, placeholder, or template-bundled images
- `<style>`, `class`, `<foreignObject>`, `textPath`, `@font-face`, `<animate*>`, `<script>`, `<iframe>`, `<symbol>`+`<use>`
- `<g opacity>`
- HTML named entities except XML escaping for `& < > " '`
