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
