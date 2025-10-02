# Load variables from .env
include .env
export

.PHONY: db-up db-down db-logs db-cli env-copy inspect-data ingest-data reset-data

# --- Docker / Database Management ---

db-up:
	docker compose up -d

db-down:
	docker compose down

db-logs:
	docker compose logs -f

db-cli:
	pgcli -h localhost -p $(HOST_PORT) -U $(POSTGRES_USER) -d $(POSTGRES_DB)

# --- Environment Setup ---

env-copy:
	cp example.env .env

# --- Data Tasks ---

inspect-data:
	python scripts/inspect_dataset.py

ingest-data:
	@echo "Ingesting full dataset into Postgres..."
	uv run scripts/ingest_dataset.py --limit 0

reset-data:
	@echo "Truncating staging table crashes_raw..."
	docker exec -i postgres-crashes psql -U $(POSTGRES_USER) -d $(POSTGRES_DB) -c "TRUNCATE TABLE crashes_raw;"
