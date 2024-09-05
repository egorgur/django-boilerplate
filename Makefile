.PHONY: check
check:
	poetry run ruff check

.PHONY: install-pre-commit
install-pre-commit:
	poetry run pre-commit uninstall ; poetry run pre-commit install

.PHONY: pre-commit
pre-commit:
	poetry run pre-commit run --all-files

.PHONY: install
install:
	poetry install

.PHONY: migrate
migrate:
	poetry run python -m src.manage migrate

.PHONY: migrations
migrations:
	poetry run python -m src.manage makemigrations

.PHONY: runserver
runserver:
	poetry run python -m src.manage runserver

.PHONY: superuser
superuser:
	poetry run python -m src.manage createsuperuser

.PHONY: update
update: install migrate ;
