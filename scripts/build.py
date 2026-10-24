#!/usr/bin/env python3
"""Rebuild skills/ from the upstream repos listed in sources.json.

Usage: python3 scripts/build.py            (clones/pulls into .upstream/)
To add a repo: add an entry to sources.json and run this (or let the daily GitHub Action do it).
"""
import glob, json, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UP = os.path.join(ROOT, ".upstream")
OUT = os.path.join(ROOT, "skills")
cfg = json.load(open(os.path.join(ROOT, "sources.json")))
MAX = cfg.get("max_file_mb", 5) * 1024 * 1024


def sh(*a, cwd=None):
    subprocess.run(a, cwd=cwd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                   env={**os.environ, "GIT_LFS_SKIP_SMUDGE": "1"})


def fetch(repo):
    d = os.path.join(UP, repo.replace("/", "_"))
    if os.path.isdir(os.path.join(d, ".git")):
        sh("git", "fetch", "-q", "--depth", "1", "origin", "HEAD", cwd=d)
        sh("git", "reset", "-q", "--hard", "FETCH_HEAD", cwd=d)
    else:
        sh("git", "clone", "-q", "--depth", "1", f"https://github.com/{repo}.git", d)
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=d, text=True).strip()
    return d, sha


def frontmatter(path):
    t = open(path, encoding="utf-8").read()
    if not t.startswith("---"):
        return {}
    fm = t.split("---", 2)[1]
    name = re.search(r"^name:\s*[\"']?([\w.-]+)", fm, re.M)
    m = re.search(r"^description:\s*(.*?)(?=^[\w-]+:|\Z)", fm, re.S | re.M)
    desc = " ".join(re.sub(r"^[>|]-?\s*", "", m.group(1).strip()).split()).strip("\"'") if m else ""
    return {"name": name.group(1) if name else None, "description": desc}


def copy_tree(src, dst, include=None):
    names = include if include else os.listdir(src)
    for n in names:
        s = os.path.join(src, n)
        if not os.path.exists(s) or n in (".git", "node_modules"):
            continue
        if os.path.isdir(s):
            shutil.copytree(s, os.path.join(dst, n), ignore=shutil.ignore_patterns(".git", "node_modules"), dirs_exist_ok=True)
        else:
            os.makedirs(dst, exist_ok=True)
            shutil.copy2(s, os.path.join(dst, n))
    for r, _, fs in os.walk(dst):
        for f in fs:
            p = os.path.join(r, f)
            if os.path.getsize(p) > MAX:
                os.remove(p)


def main():
    os.makedirs(UP, exist_ok=True)
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    rows, owner = [], {}
    for s in cfg["sources"]:
        d, sha = fetch(s["repo"])
        found = []
        for pat in s.get("skills", []):
            for sd in sorted(glob.glob(os.path.join(d, pat))):
                if os.path.isfile(os.path.join(sd, "SKILL.md")):
                    found.append((sd, frontmatter(os.path.join(sd, "SKILL.md")).get("name") or os.path.basename(sd)))
        for sd, name in found:
            if name in owner:
                sys.exit(f"Skill name clash: {name} from {s['repo']} and {owner[name]}")
            owner[name] = s["repo"]
            copy_tree(sd, os.path.join(OUT, name), s.get("include"))
        for name, files in s.get("wrappers", {}).items():
            if name in owner:
                sys.exit(f"Skill name clash: {name}")
            owner[name] = s["repo"]
            copy_tree(os.path.join(ROOT, "custom", name), os.path.join(OUT, name))
            for src, dst in files.items():
                p = os.path.join(d, src)
                if os.path.exists(p):
                    os.makedirs(os.path.dirname(os.path.join(OUT, name, dst)), exist_ok=True)
                    shutil.copy2(p, os.path.join(OUT, name, dst))
            found.append((None, name))
        if not found:
            print(f"WARNING: no skills found in {s['repo']}", file=sys.stderr)
        s["_sha"] = sha
        s["_names"] = [n for _, n in found]

    for name in sorted(owner):
        fm = frontmatter(os.path.join(OUT, name, "SKILL.md"))
        rows.append({"name": name, "source": f"https://github.com/{owner[name]}", "description": fm.get("description", "")})
    json.dump(rows, open(os.path.join(ROOT, "index.json"), "w"), indent=1, ensure_ascii=False)
    with open(os.path.join(ROOT, ".sources"), "w") as f:
        for name in sorted(owner):
            f.write(f"{name}|{owner[name]}\n")

    lines = ["# Third-party sources", "", "Copied from the repositories below under their licences; copyright stays with the original authors. Pinned commit = the version currently in this repo.", "", "| Source | Licence | Commit | Skills |", "|---|---|---|---|"]
    for s in cfg["sources"]:
        lines.append(f"| https://github.com/{s['repo']} | {s.get('license','see repo')} | `{s['_sha'][:7]}` | {', '.join(s['_names'])} |")
    open(os.path.join(ROOT, "THIRD_PARTY.md"), "w").write("\n".join(lines) + "\n")

    cat = []
    for s in cfg["sources"]:
        cat += [f"\n### [{s['repo']}](https://github.com/{s['repo']})\n", "| Skill | Use it for |", "|---|---|"]
        for r in rows:
            if r["source"].endswith("/" + s["repo"]):
                d = r["description"]
                d = (d[:220] + "…") if len(d) > 220 else d
                cat.append(f"| `{r['name']}` | {d.replace('|', '/')} |")
    head = open(os.path.join(ROOT, "README.head.md")).read()
    tail = open(os.path.join(ROOT, "README.tail.md")).read()
    open(os.path.join(ROOT, "README.md"), "w").write(head.replace("{{COUNT}}", str(len(rows))).replace("{{REPOS}}", str(len(cfg["sources"]))) + "\n## Catalog\n" + "\n".join(cat) + "\n\n" + tail)
    print(f"Built {len(rows)} skills from {len(cfg['sources'])} repos")


if __name__ == "__main__":
    main()
