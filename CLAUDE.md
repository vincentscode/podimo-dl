# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

No lint config. Install deps with `pip install -r requirements.txt`.

```bash
# Run the downloader (interactive prompts unless flags / env vars fill them in)
python podimo-dl.py [-p PODCAST_NAME_OR_UUID] [-d] [--premium-only] [--overwrite] [-o OUTPUT_BASE_DIR]

# Regenerate queries.py and mutations.py from Podimo's JS bundles
python generate.py

# Run tests (stdlib unittest, fully mocked — no network)
python -m unittest test_podimo_dl.py -v
# Single test:
python -m unittest test_podimo_dl.GetPodcastEpisodesTest.test_paginates_until_short_page
```

Note: `test_podimo_dl.py` imports `podimo-dl.py` via `importlib.util` because the hyphenated filename isn't a legal Python module name.

CLI flags: `-p` accepts either a podcast name (substring-matched against autocomplete results, first hit wins) or a UUID matching `8-4-4-4-12` hex — UUIDs short-circuit search and are passed straight to `get_podcast_episodes`. `-d/--download` skips the "Download Episodes?" prompt; `--premium-only` filters to PREMIUM episodes; `--overwrite` re-downloads existing files; `-o` overrides the output base directory (default `episodes/`). Files land at `<base>/<sanitized podcast title>/<sanitized episode title>.mp3`; the per-podcast folder is created if missing. For UUID input, `get_podcast_title` (one extra `podcastById` call) supplies the folder name, falling back to the UUID if the lookup returns nothing.

Credentials come from `.env` (gitignored, copied from `.env.example`): `PODIMO_EMAIL`, `PODIMO_PASSWORD`, `PODIMO_IS_CREATOR`. Any unset value falls through to an interactive prompt; `PODIMO_IS_CREATOR` is parsed as truthy on `1`/`true`/`yes`.

## Architecture

This is a single-purpose CLI that downloads podcast episodes from Podimo via their internal GraphQL API. Three concerns are split across files:

**`podimo-dl.py`** — the only runtime entry point. The `PodimoAPI` class wraps two GraphQL clients:
- `studio_client` → `https://studio.podimo.com/graphql` (used only when `is_creator=True`, with `scope: 'CREATOR'`)
- `public_client` → `https://podimo.com/graphql` (everything else: search, episode listing)

After `login()`, both transports share a token-bearing header set (no `Host` override — earlier versions set `Host: graphql.pdm-gateway.com` but the current API works without it; re-add if requests start 401-ing post-login).

The flow is: `login` → resolve podcast id (UUID input is used directly + `get_podcast_title` fetches the title for folder naming; otherwise `search_podcast` substring-filters `podcastsAutocomplete` results by title and returns the first hit) → `get_podcast_episodes` (paginates `podcastEpisodes` until a short page) → `download_episode` (urllib download into `<base>/<podcast>/`, then `eyed3` writes ID3v2.4 tags). Track numbers are parsed from title prefixes like `#42 Episode Title` via regex; otherwise track 0.

**`queries.py` and `mutations.py` are AUTO-GENERATED — do not hand-edit.** They are produced by `generate.py`, which fetches Podimo's webpack bundles and extracts every embedded `query …` / `mutation …` string. The bundle URLs hard-coded in `generate.py` (`js_url`, `js_studio_urls`) are versioned and will 404 when Podimo redeploys; when regenerating fails, fetch the current bundle URLs from `podimo.com` / `studio.podimo.com` and update those constants before rerunning. `podimo-dl.py` does `from queries import *` / `from mutations import *`, so regenerating may rename or remove the symbols it consumes (e.g. `queryTokenWithCredentials`, `queryUsePodcastsExistQuery`) — verify those still exist after regenerating.

When the regenerated query exists but has the wrong selection set, `podimo-dl.py` defines its own `gql(...)` override at the top of the file rather than editing the generated module. Current overrides: `queryPodcastEpisodesForDownload` (the generated `queryPodcastEpisodes` is the studio/creator variant — `converted: false, published: false`, no `audio` / `accessLevel`; the override uses `converted: true, published: true` and selects `audio { url }` + `accessLevel`) and `queryPodcastInfoForDownload` (minimal `podcastById` for folder-name lookup — note: the mobile/listener schema at `podimo.com/graphql` does *not* have `publicPodcastById` — that's a web-only field — even though `queries.py` is full of web queries that use it; use `podcastById` instead, and use a variable name that differs from `podcastId` since the validator's "never used" error is what you'll get if the field is unknown and gets stripped). If a future regeneration restores the listener-facing shape, the overrides can be dropped.
