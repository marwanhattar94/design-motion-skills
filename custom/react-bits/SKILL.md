---
name: react-bits
description: React Bits component library (reactbits.dev) — animated UI components, text animations, backgrounds and micro-interactions in JS/TS with CSS or Tailwind. Use when building a React page or artifact that needs a striking animated text effect, background, card, cursor, carousel or micro-interaction, or when the user names a React Bits component.
---

# React Bits

The complete component index with links to every component's docs and source is in `references/llms.txt`. Search it (grep) for the effect you need — e.g. "Split Text", "Aurora", "Magnet", "Dock" — rather than reading it all.

## Workflow
1. Pick the component from `references/llms.txt` by category: UI Components, Animations, Backgrounds, Text Animations, Micro.
2. Choose the variant that matches the project: JS-CSS, JS-TW, TS-CSS, TS-TW.
3. Install via CLI in a real project:
   - shadcn: `npx shadcn@latest add @react-bits/<Component>-<VARIANT>` (as listed in the docs page)
   - jsrepo: `npx jsrepo add https://reactbits.dev/<variant>/<Category>/<Component>`
   For a single-file artifact, open the component's source URL from llms.txt and inline it.
4. Install the component's own dependencies (varies: `gsap`, `motion`, `three`, `ogl`, `@react-three/fiber`…). Check before use.
5. Tune props to the brand; do not ship default demo colors.

## Taste rules
- One hero effect per view. React Bits effects are loud — pair with calm layout (see `impeccable`, `design-taste-frontend`).
- Respect `prefers-reduced-motion`; provide a static fallback for WebGL backgrounds.
- Check performance on mobile (see `animation-performance`).

License: MIT + Commons Clause (free to use in products; the library itself may not be resold). React Bits Pro is a separate paid product.
