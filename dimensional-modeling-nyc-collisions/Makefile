# Load variables from .env
include .env
export

up:
	docker compose up -d

down:
	docker compose down

logs:
	docker compose logs -f

pgcli:
	pgcli -h localhost -p $(HOST_PORT) -U $(POSTGRES_USER) -d $(POSTGRES_DB)

copy-env:
	cp example.env .env

inspect:
    python scripts/inspect_dataset.py --url "https://data.cityofnewyork.us/resource/h9gi-nx95.csv?$limit=1000"


ingest-full:
	@echo "Truncating staging table crashes_raw..."
	docker exec -i postgres-crashes psql -U $(POSTGRES_USER) -d $(POSTGRES_DB) -c "TRUNCATE TABLE crashes_raw;"
	@echo "Ingesting full dataset..."
	uv run scripts/ingest_dataset.py --limit 0
