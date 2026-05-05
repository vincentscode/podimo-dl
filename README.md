# podimo-dl

Download episodes from a Podimo podcast you have access to.

## Setup

Requires Python 3. Install dependencies:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and fill it in:

```
PODIMO_EMAIL=you@example.com
PODIMO_PASSWORD=...
PODIMO_IS_CREATOR=false   # set to true to log in with creator/studio scope
```

Any value left out of `.env` falls through to an interactive prompt at runtime.

## Usage

```bash
python podimo-dl.py [-p PODCAST_NAME_OR_UUID] [-d] [--premium-only] [--overwrite] [-o OUTPUT_BASE_DIR]
```

`-p` accepts either a podcast name (substring-matched, first hit wins) or a podcast UUID (8-4-4-4-12 hex), which skips the search step. Without `-p` you'll be prompted.

Other flags:

- `-d, --download` — skip the "Download Episodes?" confirmation prompt.
- `--premium-only` — only download episodes flagged `PREMIUM`.
- `--overwrite` — re-download episodes whose files already exist.
- `-o OUTPUT_BASE_DIR` — base output directory (default `episodes/`).

Files land at `<base>/<podcast title>/<episode title>.mp3`. The per-podcast folder is created automatically.
