# Load variables from .env
include .env
export

.PHONY: db-up db-down db-logs db-cli env-copy inspect-data ingest-data reset-data help

# --- Docker / Database Management ---

db-up: ## Start Postgres with Docker
	docker compose up -d

db-down: ## Stop Postgres and remove containers
	docker compose down

db-logs: ## Tail logs from Docker containers
	docker compose logs -f

db-cli: ## Open pgcli session into Postgres
	pgcli -h localhost -p $(HOST_PORT) -U $(POSTGRES_USER) -d $(POSTGRES_DB)

# --- Environment Setup ---

env-copy: ## Copy example.env to .env
	cp example.env .env

# --- Data Tasks ---

inspect-data: ## Inspect the first 1000 rows of the collisions dataset
	python scripts/inspect_dataset.py

ingest-data: ## Ingest the full dataset into Postgres
	@echo "Ingesting full dataset into Postgres..."
	uv run scripts/ingest_dataset.py --limit 0

reset-data: ## Truncate staging table crashes_raw
	@echo "Truncating staging table crashes_raw..."
	docker exec -i postgres-crashes psql -U $(POSTGRES_USER) -d $(POSTGRES_DB) -c "TRUNCATE TABLE crashes_raw;"

# --- Utility ---

help: ## Show this help message
	@echo "Available make commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' Makefile | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'
