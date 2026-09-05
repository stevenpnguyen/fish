# Fish

A Pygame Zero clicker game: click the fish to earn money, avoid the sea snake so you don't lose what you earned, and progress through levels with up to 4 trophies.

## Features

- Click the fish to gain money
- Avoid the sea snake or lose your earnings
- Level up and unlock up to 4 trophies

## Running

Install dependencies:

```
pip install -r requirements.txt
```

Run locally with Pygame Zero:

```
make run
```

## Building

- **Web build**: `make build` packages the game for the browser with `pygbag`. The result is written to `build/web` and a `CNAME` is copied in for the custom domain.
- **Desktop executable**: `make build-exe` builds a standalone executable with PyInstaller using `fish.spec`.

Other targets:

- `make serve` — serve the game locally for the browser build
- `make clean` — remove the `build/` directory

## Deployment

Pushing to `main` triggers the GitHub Actions workflow (`.github/workflows/build-and-deploy.yml`), which:

- Builds the web package and deploys it to GitHub Pages (`fish.snguyen.au`)
- Builds desktop executables for Linux and Windows and uploads them as artifacts

## Project layout

- `game.py` — the primary game logic (used for the Pygame Zero local run)
- `fish.py` — self-contained game variant that drives its own pygame window
- `main.py` — pygame entry point with a shim that lets `game.py` run under plain pygame (used by `pygbag`/web builds)
- `executable/launcher.py` — launcher used for desktop builds
- `images/`, `sounds/` — game assets
- `code/` — a lighter copy of the game
