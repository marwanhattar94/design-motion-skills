# Design & Motion Skills

55 agent skills for design, UI and motion, collected from 14 open-source repos and **kept live automatically**. Works with Claude (Cowork / claude.ai), Claude Code and any agent that reads `SKILL.md` files.

## How it stays live
- A GitHub Action (`.github/workflows/sync.yml`) runs every day at 03:00 UTC. It pulls every repo in `sources.json`, rebuilds `skills/`, and commits only if something changed. Each upstream commit is pinned in `THIRD_PARTY.md`.
- Run it on demand: **Actions → Sync upstream skills → Run workflow**.
- Claude's `skill-library` loader skill pulls this repo at the start of a task, so Claude always uses the latest version.

## Add a new skill repo
Add an entry to `sources.json`, then commit or run the workflow:
```json
{"repo": "owner/name", "license": "MIT", "skills": ["skills/*"]}
```
`skills` takes glob paths to folders that contain a `SKILL.md` (use `"."` when it sits at the repo root). Repos with no `SKILL.md` can be wrapped: put a hand-written `custom/<name>/SKILL.md` here and map upstream docs into it with `"wrappers"` (see the Lenis entry).

## Install
**Claude / Cowork:** add the `loader/skill-library/SKILL.md` skill to your account. It fetches this repo when needed.

**Claude Code (plugin):**
```
/plugin marketplace add marwanhattar94/design-motion-skills
/plugin install design-motion-skills@rawa-design-skills
```
Run `/plugin marketplace update` to pull new versions.

**Manual:** `git clone https://github.com/marwanhattar94/design-motion-skills.git && cp -r design-motion-skills/skills/* ~/.claude/skills/`

**Upload zips:** `scripts/zip-skills.sh`, then upload from `dist/` in Settings → Capabilities → Skills.

## Catalog

### [greensock/gsap-skills](https://github.com/greensock/gsap-skills)

| Skill | Use it for |
|---|---|
| `gsap-core` | Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). Use when the user asks for a JavaScript animation library, … |
| `gsap-frameworks` | Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue, Nuxt, Svelte, SvelteKit, or asks about GSAP with Vue/Svelt… |
| `gsap-performance` | Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations, reducing jank, or when the user asks about animation performance, FPS, or smoot… |
| `gsap-plugins` | Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics plugins, CustomEase, EasePack, CustomWiggle, CustomBounce,… |
| `gsap-react` | Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks about GSAP with React, useGSAP, or cleanup on unmount. Recommend GSAP for React … |
| `gsap-scrolltrigger` | Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax, pinned sections, or when the user asks about ScrollTrigger, … |
| `gsap-timeline` | Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing keyframes, or when the user asks about animation sequencing, timelines, or animat… |
| `gsap-utils` | Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks about gsap.utils, clamp, mapRange, random, snap, toArray, wrap, or helper utilities … |

### [pbakaus/impeccable](https://github.com/pbakaus/impeccable)

| Skill | Use it for |
|---|---|
| `impeccable` | Use when the user wants to design, redesign, shape, critique, audit, polish, simplify, harden, animate, or otherwise improve a frontend interface: websites, landing pages, dashboards, product UI, components, forms, setti… |

### [darkroomengineering/lenis](https://github.com/darkroomengineering/lenis)

| Skill | Use it for |
|---|---|
| `lenis` | Smooth scrolling with Lenis (darkroom.engineering). Use when a page, landing page, microsite or artifact needs smooth/inertia scrolling, scroll-linked animation synced with GSAP ScrollTrigger, smooth anchor links, or fix… |

### [DavidHDev/react-bits](https://github.com/DavidHDev/react-bits)

| Skill | Use it for |
|---|---|
| `react-bits` | React Bits component library (reactbits.dev) — animated UI components, text animations, backgrounds and micro-interactions in JS/TS with CSS or Tailwind. Use when building a React page or artifact that needs a striking a… |

### [21st-dev/skill](https://github.com/21st-dev/skill)

| Skill | Use it for |
|---|---|
| `21st-ai` | Generate and iterate on UI with 21st AI from the terminal via the `21st` CLI (`@21st-dev/cli`): sketch a UI from a prompt, preview the variants in the browser, edit any variant in place with a natural-language change, an… |
| `21st-cli-use` | Search, install and pull code from the 21st.dev catalog with the `21st` CLI (`@21st-dev/cli`): find React/shadcn components, themes and templates, print a component's code or a theme's CSS, install an item into the proje… |
| `21st-design-sync` | Look at the current project's design (its shadcn / Tailwind CSS variables and color tokens) and publish it to the 21st.dev community as a shareable theme, using `21st publish-theme`. Use when the user says "publish my th… |
| `21st-registry` | Publish your own work to 21st.dev and manage it from the terminal with the `21st` CLI (`@21st-dev/cli`): publish a React component to a team library, publish a CSS theme or a template listing, edit / unpublish / delete y… |
| `21st-ui-build` | Build or substantially change production UI using the current project's design context, existing components, and grounded 21st inspiration. Use when implementing a page, section, component, responsive redesign, or visual… |
| `21st-ui-explore` | Explore and compare multiple meaningfully different UI directions grounded in the current project's design system and 21st inspiration. Use when the user wants options, variants, concepts, a redesign direction, visual ex… |
| `21st-ui-review` | Review existing UI against the project's design context, accessibility expectations, responsive behavior, interaction quality, and high-confidence production rules. Use for UI audits, design QA, frontend review, accessib… |

### [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

| Skill | Use it for |
|---|---|
| `captions-overlay` | Overlay doctrine for captions in HyperFrames videos — the caption MODEL (drop / rail / embed) and the rule that captions are an OVERLAY composited on top of the film, never a reserved bottom band you shift content up to … |
| `changelog-video` | Turn a weekly changelog .md into a finished branded changelog video (square 1080, ~45-60s, Annie VO, animated brand background, mock-UI visualizations, lowkey captions). Use when the user provides a changelog/digest mark… |
| `cut-the-curve` | The technique catalog: five velocity-matched SEAMS (zoom-through, INVERSE zoom-through, cut-the-curve, waterfall cut, rack-focus blur-cut) plus the two in-scene techniques — waterfall ENTRY (staggered arrival cascades fo… |
| `figma` | Bring Figma into a HyperFrames video - rendered assets, brand tokens, components, storyboard frames as reconstructed motion (frames read as states, not slides), shaders and connector-assisted motion. Use when the person … |
| `hyperframes` | Read first to make, edit, animate or render any video with HyperFrames (HTML rendered to video), including launch films, explainers, music videos, charts, maps, vertical clips, title cards, captions and overlays. Holds t… |
| `hyperframes-cli` | The HyperFrames CLI by job - scaffold, check, look at frames, edit the timeline, preview, render locally or in the cloud, publish, project history - plus reading its JSON and recovering from build or render failures. |
| `hyperframes-registry` | About 450 ready-made HyperFrames blocks and components installed as editable source - transitions, overlays, titles, kinetic type, captions, charts, map overlays, 3D, camera moves. Use it before hand-building any named v… |
| `media-use` | Get or make any media for a HyperFrames video - music, sound effects, images, icons, logos, voiceover, avatar and generated video, transcripts, cutouts, colour grades and looks - with HeyGen or free local tools, and mix … |
| `motion-doctrine` | GATEWAY — load FIRST before composing any HyperFrames animation or video. The high-level motion law that makes a multi-scene video feel like ONE continuous camera move instead of a stack of independently-animated slides.… |
| `oversized-cursor` | House-style oversized macOS cursor technique for HyperFrames launch videos. Load whenever a scene involves cursors or a pointer-led action, when kicking off a UI scene, when igniting a morph/transition/typing run with a … |
| `remotion-to-hyperframes` | Bring existing video code or footage into HyperFrames and verify it frame by frame against the original - Remotion first, also Motion Canvas, Lottie, Three.js, p5.js, canvas or plain HTML/CSS animation, or renders from M… |
| `reverse-any-video` | Rebuild any video file as an editable HyperFrames project - motion graphics, talking heads, live action or AI-generated footage. Measure and watch it, rebuild every layer, then check the render against the original frame… |
| `seam-craft` | Render-correctness doctrine for scene-to-scene seams in HyperFrames launch videos — the prerequisites that make transitions composite correctly on the master timeline. Load when assembling the master timeline / index.htm… |
| `slideshow` | Build a HyperFrames slideshow to present live - slides, fragment reveals, branching hotspots and presenter mode with speaker notes, served by `hyperframes present` - or turn an existing page into one. Use when the person… |

### [feitangyuan/onetake](https://github.com/feitangyuan/onetake)

| Skill | Use it for |
|---|---|
| `onetake` | Make short product / skill motion videos (10–30 s, narrated feature demos up to ~60 s) the way high-end launch clips are made — kinetic type, real UI as the material, a hand that causes every reaction, beats that carry i… |

### [MegaTroll222/VOX-COLLAGE-BROLL](https://github.com/MegaTroll222/VOX-COLLAGE-BROLL)

| Skill | Use it for |
|---|---|
| `collage-broll-explainers` | Turn a ~5-second voiceover line, opinion sentence, or abstract concept into a premium editorial halftone paper-collage B-roll clip — optionally with a fitted voiceover. Load this skill whenever the user says "collage b-r… |

### [JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase)

| Skill | Use it for |
|---|---|
| `claude-animation-base` | Hand-painted character animation in p5.js + p5.brush (John Heibel's Claude Animation Base, featuring the Clawd character). Use when the user wants a short handmade-looking animated video or scene with a character — story… |

### [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)

| Skill | Use it for |
|---|---|
| `lemo-opuscar` | Direct and produce a short film made entirely in code, in one of the styles of the Lemo-Opuscar library (e.g. Impasto Oil Painting 油画厚涂, Watercolor Brush 水彩笔刷, Ukiyo-e 浮世绘, Satellite Briefing 卫星简报, Exploded Teardown 产品拆解… |

### [showheyohtaki/motion-prompt](https://github.com/showheyohtaki/motion-prompt)

| Skill | Use it for |
|---|---|
| `motion-prompt` | Motion Prompt (showheyohtaki.github.io/motion-prompt) is a numbered library of names for motion-graphics moves, camera moves and transitions, UI components, landing-page and web effects, and photo looks and lighting, eac… |

### [emilkowalski/skills](https://github.com/emilkowalski/skills)

| Skill | Use it for |
|---|---|
| `animate` | Build an animation from scratch, making the decisions in the order that determines whether it feels right — should it animate at all, what purpose, which tool, which properties, which curve and duration, how it interrupt… |
| `animate-expo` | Build animations in React Native and Expo, making the decisions in the order that determines whether they feel right — should it animate, which thread it runs on, which properties, spring or timing, how the gesture hands… |
| `animation-performance` | Keep web animations inside the frame budget — animate composite-only properties, keep motion off the main thread when the page is busy, and find the cause when an animation drops frames. Covers the layout/paint/composite… |
| `animation-vocabulary` | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in; "the iOS rubber-band scroll" → Rubber-banding). Use when t… |
| `apple-design` | Apple's approach to interface design and fluid, physical motion, translated for the web. Use when building or reviewing gesture-driven UI, spring animations, drag/swipe/sheet interactions, momentum and interruptible tran… |
| `ask-sonner` | Guide to Sonner, the React toast library — install and wire up the Toaster, pick the right toast() call, promise and loading toasts, updating, dismissing and persisting toasts, styling, theming and icons, positioning and… |
| `break-ui` | Try to break a piece of UI by feeding it worst-case data — long names, unbreakable emails, one-letter names, missing fields, huge counts, zero items, long labels, non-Latin text, emoji, extreme numbers — then render it b… |
| `emil-design-eng` | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. |
| `find-animation-opportunities` | Search a codebase or UI for places that don't animate but should, and reject everything that shouldn't. Read-only; it proposes motion with exact values, it does not implement it. Use when the user asks "what could be ani… |
| `improve-animations` | Survey a codebase's animation and motion code as a senior motion advisor, then produce a prioritized audit and self-contained implementation plans for other agents (or cheaper models) to execute. Read-only on source code… |
| `mobile-native` | Make a web app feel native on a phone — the small CSS and meta-tag fixes that separate "a website in a browser" from something that feels installed. Covers sticky hover states, tap highlight flashes, the 100vh bug, input… |
| `pick-ui-library` | Pick the right library for a given frontend task from a curated, opinionated list — numbers, OTP inputs, charts, command menus, virtualization, drag and drop, toasts, state, styling, and more. Only runs when explicitly i… |
| `prototype` | Build multiple genuinely different versions of a UI piece you describe, rendered behind a visual picker so you can flip through them live and promote the one that feels right. Only runs when explicitly invoked; it does n… |
| `remove-animations` | Find the animations an interface doesn't need and remove them — motion on keyboard actions, high-frequency surfaces, functional data, and decoration with no purpose — then clean up what they leave behind. Edits code, but… |
| `review-animations` | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. Default to flagging; approval is earned. |
| `write-swift` | How to write modern Swift well — modeling with value types, Swift 6 data-race safety and approachable concurrency (@concurrent, main-actor-by-default, actors, task groups), protocols and generics (some vs any), API desig… |

### [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)

| Skill | Use it for |
|---|---|
| `design-taste-frontend` | tasteskill v2, the anti-slop frontend skill. Art direction for websites, distilled from a study of 247 curated gallery sites (One Page Love, Awwwards Sites of the Day). Deals researched directions (idea, composition, typ… |

### [haidrrrry/claude-remotion-skill](https://github.com/haidrrrry/claude-remotion-skill)

| Skill | Use it for |
|---|---|
| `remotion-motion-graphics` | Create and edit professional motion graphics videos with Remotion (React-based video). Use this skill EVERY time the user wants to create a video, edit a video, animate something, build an intro/outro/logo animation, mak… |

## Licences
Every skill keeps its upstream licence (see each folder and `THIRD_PARTY.md`). **onetake** is PolyForm **Noncommercial**, so don't use it for client or commercial work without the author's permission. **react-bits** is MIT + Commons Clause: use it freely, but don't resell the library. Files over 5 MB (demo videos and the like) are left out.
