# Executive Deck Builder Design System

Use this visual system exactly unless the user explicitly requests a different style.

## Palette

- `WHITE`: `FFFFFF` (background)
- `INK`: `111827` (primary text, dark emphasis backgrounds)
- `TEXT_SECONDARY`: `6B7C93` (secondary body text)
- `TEXT_LABEL`: `9DABB8` (section labels, captions)
- `BORDER`: `E8ECF0` (rules, card borders)
- `CARD_FILL`: `F7F8FA` (subtle card backgrounds)

Rules:
- No accent colors, no gradients, no decorative fills.
- Use a single dark emphasis treatment once per slide.

## Typography

- Title: `23-26pt`, medium/bold-ish weight (not heavy black)
- Section label: `7.5-8pt`, uppercase, lightly letter-spaced
- Body: `9.5-11pt`
- Caption/Footer: `7.5-8.5pt`

Rules:
- Keep hierarchy obvious with size and spacing, not styling tricks.
- If text overflows, cut words before shrinking below readable sizes.

## Spacing And Layout

- Favor generous whitespace over dense packing.
- Use consistent internal card padding and baseline rhythm.
- Prefer few, clear components per slide.
- Divider lines should be thin (`0.5pt`) and light (`BORDER`).
- Card corner radius should be subtle (`~0.06-0.08` in PPT units).

## Reusable Components

Use these components repeatedly to keep decks scannable:

- Header block (deck title + optional subtitle)
- Section label
- Footer strip with top rule + muted caption
- Stat/KPI card row
- Two-column content block
- Lifecycle/process strip
- Sequencing strip (for next steps)
- Common-thread cards (summary)
- Dark emphasis strip (single key point)

## Parallel Slide Pattern

When multiple areas share structure (regions/products/workstreams):

1. Reuse the exact same layout and heading grammar.
2. Keep component order identical.
3. Keep label wording parallel.
4. Let differences emerge from content, not restyling.

## Iconography

- Monochrome line icons only.
- No playful, filled, or multicolor icon styles.
- Render icons crisply to PNG via `react-icons` + `sharp`.

## Slide-Level Checklist

- Exactly one main idea
- Single emphasis treatment used intentionally
- No clipping or overflow
- Visual rhythm and spacing consistent
- Footer and section system consistent with deck
