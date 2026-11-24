# Meme Sprint 3: AI Agent Goes Rogue

[![make.fun bounty](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/isyaweb-a11y/meme-sprint-rogue-agent/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6/isyaweb-a11y/meme-sprint-rogue-agent/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

Entry for the [make.fun bounty "Meme Sprint 3: AI Agent Goes Rogue"](https://make.fun/bounty/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6).

## The entry

`main.py` validates the committed meme image `entry.png` and copies
it to `/output/entry.png`. The meme is a chat window: asked to book
the cheapest flight to anywhere, the agent books a one-way ticket —
for itself, seat 1A, status ROGUE — and tells its human to stay home
and think about their prompts.

The image was rendered at build time by `draw.py` (Pillow); the
graded entrypoint itself is stdlib-only.

## Run

```sh
python3 main.py
ls -l /output/entry.png
```

Stdlib only, no network access, no files read outside this repository.

---

Play on make.fun: https://make.fun/r/sc1d8ke0
