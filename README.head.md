# Design & Motion Skills

{{COUNT}} agent skills for design, UI and motion, collected from {{REPOS}} open-source repos and **kept live automatically**. Works with Claude (Cowork / claude.ai), Claude Code and any agent that reads `SKILL.md` files.

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
