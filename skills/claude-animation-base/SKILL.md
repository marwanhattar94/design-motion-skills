---
name: claude-animation-base
description: Hand-painted character animation in p5.js + p5.brush (John Heibel's Claude Animation Base, featuring the Clawd character). Use when the user wants a short handmade-looking animated video or scene with a character — storyboard, shot-by-shot build, contact-sheet self-checks, rendered to MP4.
---

# Claude Animation Base

This skill wraps the starter kit at github.com/JohnHeibel/ClaudeAnimationBase. The rules and full API are in `references/ANIMATION_GUIDE.md` — read it completely before writing any scene. `references/README.md` covers running and rendering.

## Workflow
1. Get the kit: `git clone --depth 1 https://github.com/JohnHeibel/ClaudeAnimationBase.git && cd ClaudeAnimationBase && npm install` (needs Node, Chrome/Chromium, ffmpeg; on Linux Playwright's Chromium is found automatically).
2. Storyboard first (shots, beats, timing), then build shot by shot in `src/scenes/`.
3. Check your own work with contact sheets / stills from `render.mjs` before the full render.
4. Render: `node render.mjs --clip --out=out/video.mp4` (add `--soft-gl` with no GPU; avoid watercolour fills on slow machines).

## Guide principles (summary — the guide wins on conflict)
Handmade, alive, one continuous piece, no on-screen text, transitions always, something happens in every scene; brush strokes, flat 2D and boiling linework; timing for the viewer; core character-animation principles.
