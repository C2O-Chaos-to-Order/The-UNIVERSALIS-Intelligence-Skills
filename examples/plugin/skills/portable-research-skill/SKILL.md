---
name: portable-research-skill
description: Summarizes a supplied research corpus and identifies contradictions. Use when a user requests a source-grounded research summary.
license: MIT
compatibility: Local Python 3.12 runtime; no network required.
metadata:
  author: example-maintainer
  version: "1.0.0"
---

# Portable Research Skill

1. Read only supplied files under references/.
2. Preserve source provenance and limitations.
3. Distinguish quotation, paraphrase, and inference.
4. Report unresolved contradictions instead of silently reconciling them.
5. Do not use network access or paths outside the skill package.
