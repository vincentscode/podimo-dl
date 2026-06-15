# podimo-dl

## Requirements

- Python
- [`gql[aiohttp]`](https://github.com/graphql-python/gql) — GraphQL client
- [`eyed3`](https://eyed3.readthedocs.io) — ID3 tag writing

### Setup (recommended: virtual environment)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install gql[aiohttp] eyed3
```

## Usage

```bash
python podimo-dl.py
```

You will be prompted for your Podimo credentials and the podcast name to search for.

Optionally, create a `config.py` file using the format provided in `config.sample.py` to skip the credential prompts:

```bash
python podimo-dl.py --config -p "Podcast Name" --download
```

### Options

| Flag | Description |
|------|-------------|
| `-p / --podcast` | Podcast name to search for |
| `-c / --config` | Load credentials from `config.py` |
| `-d / --download` | Download without prompting |
| `--premium-only` | Only download PREMIUM episodes |
| `--overwrite` | Re-download files that already exist |
| `-o / --output` | Output directory for downloaded files |