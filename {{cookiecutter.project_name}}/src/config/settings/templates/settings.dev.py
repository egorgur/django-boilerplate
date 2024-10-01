"""Template for local development settings."""

DEBUG = True
SECRET_KEY = "some_secret_key"

IN_DOCKER = False

# Database settings must be same in docker-compose.dev.yaml
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5433", # IMPORTANT! changed the database port to allow use of the Postgres from docker
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": 600,
    }
}
