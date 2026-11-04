# Sony Africa Gaming Revenue Model

An estimate of Sony's PlayStation revenue in Africa, built entirely from public data, with sensitivity analysis on the key assumptions.

## Background

This repo is a Python rewrite of the gaming side of my original research, written up in [`docs/Sony Africa.docx`](docs/Sony Africa.docx). The writeup covers the full methodology, data sources and reasoning behind each assumption. This code re-implements just the gaming model so it can be rerun, stress-tested and extended. The original model was built in Excel, and the Python base case is checked against it.

## Model structure

Revenue is split into two parts:

- **Case-study countries (South Africa, Egypt, Nigeria):** hardware and content spend per country, each multiplied by PlayStation's estimated market share.
- **Rest of Africa (RoA):** estimated from declared console imports, adjusted for customs-to-retail markup, grey-market imports and non-reporting countries. Hardware revenue is the new-console share of that inflow; content spend is a ratio of the inflow, capped at a ceiling.

Every assumption has a low, base and high value in `assumptions.csv`.

## Files

| File | Purpose |
|---|---|
| `assumptions.csv` | All model inputs, one row per assumption, with low / base / high columns |
| `model.py` | Revenue calculations, as pure functions of a parameter Series |
| `sensitivity.py` | Tornado analysis: flexes one assumption at a time and measures the change in total revenue |
| `plot.py` | Chart plotting function. |
| `main.py` | Entry point: loads assumptions, runs the base case and the tornado analysis |
| `docs/Sony Africa.docx` | Original writeup |

## Running it

```bash
uv sync
uv run main.py
```

This prints the base-case total and the assumptions ranked by their effect on it.

## Validation

The Python base case reproduces the Excel model's figure of $137.95mn, and `main.py` asserts this so any change that breaks the match is caught.

## Next steps

- Monte Carlo simulation across the low / high ranges
- Music revenue as a possible addendum
