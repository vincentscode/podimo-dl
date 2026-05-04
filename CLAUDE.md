# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

No lint config. Install deps with `pip install -r requirements.txt`.

```bash
# Run the downloader (interactive prompts unless flags / env vars fill them in)
python podimo-dl.py [-p PODCAST_NAME] [-d] [--premium-only] [--overwrite] [-o OUTPUT_DIR]

# Regenerate queries.py and mutations.py from Podimo's JS bundles
python generate.py

# Run tests (stdlib unittest, fully mocked — no network)
python -m unittest test_podimo_dl.py -v
# Single test:
python -m unittest test_podimo_dl.GetPodcastEpisodesTest.test_paginates_until_short_page
```

Note: `test_podimo_dl.py` imports `podimo-dl.py` via `importlib.util` because the hyphenated filename isn't a legal Python module name.

CLI flags: `-d/--download` skips the "Download Episodes?" prompt; `--premium-only` filters to PREMIUM episodes; `--overwrite` re-downloads existing files.

Credentials come from `.env` (gitignored, copied from `.env.example`): `PODIMO_EMAIL`, `PODIMO_PASSWORD`, `PODIMO_IS_CREATOR`. Any unset value falls through to an interactive prompt; `PODIMO_IS_CREATOR` is parsed as truthy on `1`/`true`/`yes`.

## Architecture

This is a single-purpose CLI that downloads podcast episodes from Podimo via their internal GraphQL API. Three concerns are split across files:

**`podimo-dl.py`** — the only runtime entry point. The `PodimoAPI` class wraps two GraphQL clients:
- `studio_client` → `https://studio.podimo.com/graphql` (used only when `is_creator=True`, with `scope: 'CREATOR'`)
- `public_client` → `https://podimo.com/graphql` (everything else: search, episode listing)

After `login()`, both transports get a shared `Host: graphql.pdm-gateway.com` header alongside the bearer token — Podimo routes the request URLs through that gateway, so this header override is required for subsequent calls to authenticate.

The flow is: `login` → `search_podcast` (substring-filters `publicSearch` results by title and returns the first match) → `get_podcast_episodes` → `download_episode` (urllib download, then `eyed3` writes ID3v2.4 tags). Track numbers are parsed from title prefixes like `#42 Episode Title` via regex; otherwise track 0.

**`queries.py` and `mutations.py` are AUTO-GENERATED — do not hand-edit.** They are produced by `generate.py`, which fetches Podimo's webpack bundles and extracts every embedded `query …` / `mutation …` string. The bundle URLs hard-coded in `generate.py` (`js_url`, `js_studio_urls`) are versioned and will 404 when Podimo redeploys; when regenerating fails, fetch the current bundle URLs from `podimo.com` / `studio.podimo.com` and update those constants before rerunning. `podimo-dl.py` does `from queries import *` / `from mutations import *`, so regenerating may rename or remove the symbols it consumes (e.g. `queryTokenWithCredentials`, `queryUsePodcastsExistQuery`, `queryPodcastEpisodes`) — verify those still exist after regenerating.
