---
name: lenis
description: Smooth scrolling with Lenis (darkroom.engineering). Use when a page, landing page, microsite or artifact needs smooth/inertia scrolling, scroll-linked animation synced with GSAP ScrollTrigger, smooth anchor links, or fixes for nested scroll and modals under a smooth scroller.
---

# Lenis — smooth scroll

Full upstream docs (settings, methods, events, troubleshooting): `references/README.md`. Read the relevant section before using an option you have not used before.

## Install
- Bundler: `npm i lenis` → `import Lenis from 'lenis'` and `import 'lenis/dist/lenis.css'`.
- No build step / single-file HTML: load `https://unpkg.com/lenis@1.3.27/dist/lenis.css` and `https://unpkg.com/lenis@1.3.27/dist/lenis.min.js` (pin the exact version). In a Claude Artifact, external hosts other than the allowed CDNs may be blocked — prefer `cdn.jsdelivr.net/npm/lenis@1.3.27/dist/lenis.min.js`, or inline the file.

## Setup
```js
const lenis = new Lenis({ autoRaf: true, anchors: true, allowNestedScroll: true });
```
Either `autoRaf: true` OR drive it yourself — never both:
```js
function raf(t){ lenis.raf(t); requestAnimationFrame(raf); } requestAnimationFrame(raf);
```

## With GSAP ScrollTrigger (most common pairing)
```js
const lenis = new Lenis();
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);
```
(Do not also set `autoRaf` here.) See the `gsap-scrolltrigger` skill for trigger setup.

## Rules
- Always include lenis.css (or the equivalent `html.lenis` rules) — missing it causes jank and broken `scroll-behavior`.
- Nested scrollable areas: add `data-lenis-prevent` to the element (or `allowNestedScroll: true`).
- Modals: `lenis.stop()` on open, `lenis.start()` on close.
- Respect reduced motion: skip Lenis (or use `lerp: 1`) when `matchMedia('(prefers-reduced-motion: reduce)').matches`.
- Programmatic scroll: `lenis.scrollTo(target, { offset, duration })`.
- Do not smooth-scroll inside iframes-in-iframes or with `position: sticky` hacks that rely on native scroll timing without testing.
