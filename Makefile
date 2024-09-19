# ----------------------------------------------------------------------------
# Makefile Commands.
# ============================================================================

# ----------------------------------------------------------------------------
# Project
# ============================================================================
.PHONY: setupenv
setupenv:
	python scripts/setup_environment.py



# ----------------------------------------------------------------------------
# Ruff linting
# ============================================================================
.PHONY: lintcheck
lintcheck:
	poetry run ruff check
.PHONY: lintfix
lintfix:
	poetry run ruff check --fix

# ----------------------------------------------------------------------------
# Pytest
# ============================================================================
.PHONY: test
test:
	poetry run pytest -v -rs -n auto


# ----------------------------------------------------------------------------
# Git hooks
# ============================================================================
.PHONY: i-pre-commit
i-pre-commit:
	poetry run pre-commit uninstall ; poetry run pre-commit install

.PHONY: pre-commit
pre-commit:
	poetry run pre-commit run --all-files


# ----------------------------------------------------------------------------
# Python poetry
# ============================================================================
.PHONY: install
install:
	poetry install


# ----------------------------------------------------------------------------
# Django
# ============================================================================
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


# ----------------------------------------------------------------------------
# Docker
# ============================================================================
.PHONY: up-dev
up-dev:
	docker-compose build
	docker-compose -f docker-compose.dev.yml up --force-recreate db

.PHONY: up-production
up-production:
	docker-compose build
	docker-compose -f docker-compose.yml up


# ----------------------------------------------------------------------------
# General
# ============================================================================
.PHONY: update
update: install migrate install-pre-commit ;
