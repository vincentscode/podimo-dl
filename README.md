# podimo-dl

### Setup

You need [Python](https://www.python.org/) to run this program. Depending on your installation the program may be invoced as either `python` or `python3`.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python podimo-dl.py
```

You will be prompted for your Podimo credentials and the podcast name to search for.

Optionally, create a `config.py` file using the format provided in `config.sample.py` to skip the credential prompts:

```bash
python podimo-dl.py --config -p "Podcast Name or ID" --download
```

### Options

| Flag | Description |
|------|-------------|
| `-p / --podcast` | Podcast name to search for or Podcast ID |
| `-c / --config` | Load credentials from `config.py` |
| `-d / --download` | Download without prompting |
| `--premium-only` | Only download premium episodes |
| `--overwrite` | Re-download and overwrite files that already exist |
| `-o / --output` | Output directory for downloaded files |
