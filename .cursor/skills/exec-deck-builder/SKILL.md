---
name: exec-deck-builder
description: Build clean, minimal black-and-white executive PowerPoint decks that follow a tight narrative arc. Use this skill whenever the user wants to create a presentation, slide, deck, readout, exec summary, or .pptx, especially for leadership, stakeholder, or strategy audiences. Trigger even when the user says "make a slide," "build a deck," "turn this into a presentation," or "create a readout." Default to this skill for executive-facing slide work unless the user clearly wants a colorful, branded, or playful style. Also use it to add slides to or restyle an existing deck built this way.
---

# Executive Deck Builder

A skill for producing restrained, high-credibility black-and-white slide decks with a clear story.

The aesthetic is deliberately minimal: white background, near-black text, gray supporting tones, and one dark emphasis treatment reserved for the single most important point per slide. No color, no gradients, no clip-art.

## Before You Build: Establish The Narrative

Never jump straight to slides. First, lock the story arc with the user. A deck is an argument, not a pile of facts.

Default arc:
- Opening: why we are here, what this covers, what success looks like
- Body slides: each advances one beat of the argument in a consistent template
- Summary: single cross-cutting takeaway and common threads
- Next steps (when relevant): what happens after this, sequenced

When the content has parallel areas (for example workstreams, regions, or products), use the same template for each area so contrast is easy to read side-by-side.

Ask at most 1-2 questions:
1. What is the core story and what should the audience walk away believing?
2. Who is the audience, and are there parallel areas that should share a template?

If enough context already exists, state the assumed arc in one line and proceed.

## Build Workflow

1. Read `references/design-system.md` for exact palette, type scale, spacing, and reusable components.
2. Read `references/verbiage-rules.md` before writing any slide copy.
3. Copy `tools/exec-deck-builder/build_deck.js` as the starting point; adapt content, not styling primitives.
4. Generate the `.pptx`.
5. Render to images and visually QA every slide (overflow, clipping, alignment).
6. Fix and re-render until clean.
7. Present output files with `present_files`.

## Environment Setup

Uses `pptxgenjs`, `react`, `react-dom`, `react-icons`, and `sharp`.

If dependency resolution fails:

```bash
npm install -g pptxgenjs react react-dom react-icons sharp
```

Render deck for QA:

```bash
python /mnt/skills/public/pptx/scripts/office/soffice.py --headless --convert-to pdf deck.pptx
pdftoppm -jpeg -r 110 deck.pdf page
```

Then inspect each `page-N.jpg` and correct layout issues.

## Core Design Principles (Non-Negotiable)

- Black-and-white only. Palette: `FFFFFF`, `111827`, `6B7C93`, `9DABB8`, `E8ECF0`, `F7F8FA`.
- One dark emphasis block per slide for the most important point.
- Minimal formatting and generous whitespace.
- Thin dividers (`0.5pt`), subtle card radii (`~0.06-0.08`), monochrome line icons only.
- One idea per slide. Split slides instead of cramming.
- Restrained type: title `~23-26pt`; section labels `~7.5-8pt` uppercase letter-spaced; body `~9.5-11pt`.
- Same footer on every slide: thin top border + small gray caption.

## Verbiage Discipline

Always describe, never judge. Do not label current processes as slow, manual, ad hoc, broken, or primitive.

Frame current-state language respectfully (for example, "draws on deep regional knowledge", "coordinates across many stakeholders"), then describe opportunities clearly.

Additional rules:
- Lead with the "so what"
- Cut filler
- Prefer concrete nouns over abstraction
- Keep parallel slides grammatically parallel
- Do not pre-bake conclusions for working sessions
- Do not overstate readiness (`ready now` vs `partial` vs `needs building`)

Read full rules in `references/verbiage-rules.md`.

## Quality Bar

Target pattern:
- Opening goals slide
- 3 parallel body slides (same template, one per area)
- Summary with single takeaway + common-thread cards
- Next steps with sequencing strip

White background throughout, one dark emphasis strip per body slide, monochrome icons, respectful language.
