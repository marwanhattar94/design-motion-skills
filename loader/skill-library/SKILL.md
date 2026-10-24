---
name: skill-library
description: Loads Marwan's design and motion skill library (GSAP, Lenis, Impeccable, React Bits, 21st.dev, HyperFrames, Emil Kowalski animation skills, taste-skill, Motion Prompt, onetake, collage b-roll, Lemo-Opuscar, Claude Animation Base). Use before building or reviewing any artifact, web page, landing page, UI component, dashboard, animation, scroll effect or motion/video piece, or when the user names one of these libraries.
---

# Skill library loader

The full library lives at **https://github.com/marwanhattar94/design-motion-skills.git** (53+ skills under `skills/<name>/SKILL.md`, catalog in `index.json`).

1. Get it (once per session): `git clone --depth 1 https://github.com/marwanhattar94/design-motion-skills.git ~/skill-library 2>/dev/null || git -C ~/skill-library pull -q`. If git cannot reach the repo, fetch only what you need from `https://raw.githubusercontent.com/marwanhattar94/design-motion-skills/main/skills/<name>/SKILL.md`.
2. Pick 1–3 skills from the map below. The repo syncs daily and new skills appear in `index.json` before this map is updated, so grep `index.json` too. Read each chosen `SKILL.md` fully, then the reference files it points to — relative paths are relative to that skill's folder.
3. Follow those skills while building. When two conflict, the more specific one wins (e.g. `gsap-scrolltrigger` over `animate`).

## Which skill for what
- **Design quality / taste (load one for any UI or artifact):** `impeccable` (design, critique, audit, polish), `design-taste-frontend` (anti-generic frontend taste), `emil-design-eng` (UI polish philosophy), `apple-design`.
- **UI building:** `21st-ui-build`, `21st-ui-explore`, `21st-ui-review`, `21st-cli-use`, `react-bits` (animated components/backgrounds/text), `prototype` (several directions), `pick-ui-library`, `ask-sonner` (toasts), `mobile-native`, `break-ui` (stress-test with worst-case data).
- **Web animation:** `animate` (from scratch), `animation-vocabulary` (name a vague effect), `improve-animations`, `review-animations`, `find-animation-opportunities`, `animation-performance`, `motion-prompt` (numbered motion presets).
- **GSAP:** `gsap-core`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-plugins`, `gsap-utils`, `gsap-react`, `gsap-frameworks`, `gsap-performance`.
- **Smooth scroll:** `lenis` (pair with `gsap-scrolltrigger`).
- **Video in code (HyperFrames):** `hyperframes` (read first), `motion-doctrine` (gateway before composing), `hyperframes-cli`, `hyperframes-registry`, `slideshow`, `figma`, `media-use`, `remotion-to-hyperframes`, `cut-the-curve`, `seam-craft`, `captions-overlay`, `changelog-video`, `oversized-cursor`.
- **Video in code (Remotion):** `remotion-motion-graphics` (read before writing any Remotion code).
- **Other motion/video kits:** `onetake` (10–30 s product demo videos — noncommercial licence, not for client work), `collage-broll-explainers` (Vox-style collage b-roll), `lemo-opuscar` (styled short films in code), `claude-animation-base` (hand-painted p5.js character animation).
- **Native:** `animate-expo` (React Native/Expo), `write-swift`.

## Artifact notes
- Claude Artifacts load scripts only from allowed CDNs (cdnjs, jsdelivr, unpkg) with an exact version; inline anything else.
- GSAP is free including all plugins: `https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js` (+ `/ScrollTrigger.min.js` etc.).
- Always honour `prefers-reduced-motion`.
