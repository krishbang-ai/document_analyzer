#!/usr/bin/env node
/*
Starter deck builder for exec-deck-builder skill.
Adapt content, keep visual primitives and rhythm consistent.
*/

const path = require("path");
const PptxGenJS = require("pptxgenjs");

const COLORS = {
  WHITE: "FFFFFF",
  INK: "111827",
  TEXT_SECONDARY: "6B7C93",
  TEXT_LABEL: "9DABB8",
  BORDER: "E8ECF0",
  CARD_FILL: "F7F8FA",
};

const FONT = "Aptos";
const DECK_CAPTION = "Executive Readout | Draft";

function createDeck() {
  const pptx = new PptxGenJS();
  pptx.layout = "LAYOUT_WIDE";
  pptx.author = "exec-deck-builder";
  pptx.subject = "Executive deck";
  pptx.title = "Executive Deck";
  pptx.lang = "en-US";
  return pptx;
}

function addHeader(slide, title, subtitle) {
  slide.addText(title, {
    x: 0.6, y: 0.35, w: 12.1, h: 0.45,
    fontFace: FONT, color: COLORS.INK, fontSize: 24, bold: true,
  });
  if (subtitle) {
    slide.addText(subtitle, {
      x: 0.6, y: 0.83, w: 12.1, h: 0.28,
      fontFace: FONT, color: COLORS.TEXT_SECONDARY, fontSize: 10.5,
    });
  }
}

function secLabel(slide, text, x, y, w = 3.2) {
  slide.addText(text.toUpperCase(), {
    x, y, w, h: 0.2,
    fontFace: FONT, color: COLORS.TEXT_LABEL, fontSize: 8, bold: true, charSpace: 1.2,
  });
}

function addFooter(slide, caption = DECK_CAPTION) {
  slide.addShape("line", {
    x: 0.6, y: 7.05, w: 12.1, h: 0,
    line: { color: COLORS.BORDER, pt: 0.5 },
  });
  slide.addText(caption, {
    x: 0.6, y: 7.08, w: 12.1, h: 0.2,
    fontFace: FONT, color: COLORS.TEXT_LABEL, fontSize: 8,
  });
}

function card(slide, { x, y, w, h, title, body }) {
  slide.addShape("roundRect", {
    x, y, w, h, rectRadius: 0.07,
    fill: { color: COLORS.CARD_FILL }, line: { color: COLORS.BORDER, pt: 0.5 },
  });
  slide.addText(title, {
    x: x + 0.2, y: y + 0.14, w: w - 0.4, h: 0.24,
    fontFace: FONT, color: COLORS.INK, fontSize: 10.5, bold: true,
  });
  slide.addText(body, {
    x: x + 0.2, y: y + 0.43, w: w - 0.4, h: h - 0.55,
    fontFace: FONT, color: COLORS.TEXT_SECONDARY, fontSize: 9.5, valign: "top",
  });
}

function emphasisStrip(slide, text, y = 5.85) {
  slide.addShape("roundRect", {
    x: 0.6, y, w: 12.1, h: 0.72, rectRadius: 0.07,
    fill: { color: COLORS.INK }, line: { color: COLORS.INK, pt: 0 },
  });
  slide.addText(text, {
    x: 0.9, y: y + 0.22, w: 11.5, h: 0.28,
    fontFace: FONT, color: COLORS.WHITE, fontSize: 11, bold: true,
  });
}

function openingSlide(pptx) {
  const slide = pptx.addSlide();
  addHeader(slide, "Q3 Executive Strategy Readout", "What we learned, what it means, and where to act next");
  secLabel(slide, "why this readout", 0.6, 1.35);
  card(slide, { x: 0.6, y: 1.58, w: 3.9, h: 2.0, title: "Context", body: "Three workstreams advanced in parallel with a shared decision horizon." });
  card(slide, { x: 4.72, y: 1.58, w: 3.9, h: 2.0, title: "Goal", body: "Align leadership on readiness by area and sequence next actions." });
  card(slide, { x: 8.84, y: 1.58, w: 3.86, h: 2.0, title: "Success", body: "Leave with one shared takeaway and a clear near-term execution plan." });
  emphasisStrip(slide, "Core takeaway: consistency of structure reveals where readiness diverges.");
  addFooter(slide);
}

async function main() {
  const pptx = createDeck();
  openingSlide(pptx);
  const output = path.resolve(process.cwd(), "deck.pptx");
  await pptx.writeFile({ fileName: output });
  console.log(`Wrote ${output}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
