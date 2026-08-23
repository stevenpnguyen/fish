---
description: Sync game features from fish.py into game.py and verify pygbag compatibility.
---

You are updating `game.py`, the pygbag-compatible twin of `fish.py`. Keep the two games' mechanics in parity while preserving game.py's pygbag-safe structure.

## Context

- `fish.py` is the source of truth for gameplay: a pgzero game that runs everything at module import time (`pygame.init()`, image loading, Actor creation, `clock.schedule` at module scope).
- `game.py` is the pygbag twin and runs two ways:
  1. `make run` → `pgzrun game.py` (pgzero injects `screen`, `Actor`, `clock`, `keyboard`, `sounds`).
  2. `make build` / `make serve` → `pygbag`, whose entry point `main.py` imports `game` and injects shims for `screen`, `Actor`, `keyboard`, `clock`, then calls `game.init()`.
- Do not break `main.py`'s expectations of game.py.

## game.py structural rules (do NOT change these)

- Every asset/actor is a module-level global initialized to `None`; nothing is loaded at import time.
- All images, actors, and clock schedules are created inside `init()`.
- `draw()` calls `init()` lazily if `bg is None`.
- `Actor("name")` / `Actor("name.png")` must match a file in `images/`; the pygbag shim appends `.png` only if the name has no extension.
- Hide/show helpers set `x = -1000` to hide and `clock.schedule(...)` to respawn.

## Sync procedure

1. Read `fish.py` and `game.py` in full.
2. For every actor/feature in fish.py, confirm game.py has the equivalent:
   - actor global declared `None` and instantiated in `init()` with the same image, initial position, and initial `clock.schedule` timings;
   - movement deltas in `update()`;
   - hide/show functions with matching respawn timings;
   - catch handler in `on_mouse_down(pos)` with the same money reward, respawn position, trophy tiers, and `sounds.<name>.play()` calls;
   - background switching in `draw()` (e.g. `if money >= 10000: screen.blit(bg2, (0, 0))`).
3. Apply only the missing or changed parts. Match fish.py's values exactly; keep game.py's structure and naming style.
4. pygbag compatibility checks:
   - No pygame/asset calls at module level in game.py — everything must live in `init()`.
   - For every `sounds.X.play()` referenced in game.py: ensure `sounds/X.ogg` exists, because pygbag cannot play `.wav` in the browser. If only `sounds/X.wav` exists, add an `.ogg` version and say so. If the file is missing entirely, flag it rather than inventing one.
   - `main.py` must expose a `sounds` shim so `sounds.X.play()` does not raise at runtime under pygbag. If main.py lacks one and game.py uses sounds, add one that loads `sounds/<name>.ogg` via `pygame.mixer.Sound` and plays it.
5. Verify:
   - `python3 -m py_compile game.py main.py`
   - `pgzrun game.py` starts without import errors (desktop smoke test).
   - `make build` succeeds if pygbag is available; if it is not installed or takes too long, skip it and say so.
6. Report a concise summary of what was synced and any pygbag fixes applied (new `.ogg` files, `main.py` shim, etc).
