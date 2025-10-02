# Dimensional Modeling on NYC Collisions

## Overview

This module works with the NYC Motor Vehicle Collisions dataset to demonstrate the full workflow from ingestion into a staging table, through profiling, and towards dimensional modeling. The dataset contains over two million rows of reported collisions from 2012 to 2025.

## Setup

### Requirements

* Docker
* Python 3.10+
* [uv](https://github.com/astral-sh/uv) for Python dependency management
* pgcli (recommended) or psql for connecting to Postgres
* VS Code with SQL and Python extensions (optional, for development)

### Getting Started

```bash
# Copy environment file
make env-copy

# Start Postgres container
docker compose up -d

# Install dependencies (sync from pyproject.toml and uv.lock)
uv sync

# Inspect first 1000 rows from the NYC Open Data API
make inspect-data

# Ingest the full dataset (~2M rows)
make ingest-data

# Connect to Postgres using pgcli
make db-cli
```

### Adding New Dependencies

To ensure dependencies are tracked and reproducible, always use `uv add` rather than pip:

```bash
uv add psycopg2-binary
```

This updates both `pyproject.toml` and `uv.lock`, which should be committed to version control.

## Progress

* **Environment setup**: Docker Compose, Makefile, uv environment
* **Inspection**: `inspect_dataset.py` script to quickly preview structure and columns
* **Ingestion**: `ingest_dataset.py` script to fetch data from the NYC Open Data API and load into Postgres staging table `crashes_raw`
* **Profiling**: SQL queries to understand row counts, time span, data quality, and null percentages

## Profiling Results (snapshot)

* ~2 million rows covering 2012–2025
* Borough column: ~32% null
* On_street_name: ~22% null
* Injury/fatality counts: <1% null (high reliability)

## Makefile Commands

* `make env-copy` → copy example environment file
* `make db-up` → start Postgres
* `make db-cli` → open pgcli into Postgres
* `make inspect-data` → preview first 1000 rows from source API
* `make ingest-data` → ingest full dataset into staging
* `make reset-data` → truncate staging table
* `make db-down` → stop Postgres and remove container

## Next Steps

* Define composite type for crash statistics
* Create entity table for intersections/streets
* Implement cumulative joins and array-based modeling
* Run analytical queries using UNNEST
