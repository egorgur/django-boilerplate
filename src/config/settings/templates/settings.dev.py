"""Template for local development settings."""

DEBUG = True
SECRET_KEY = "some_secret_key"


# Database settings must be same in docker-compose.dev.yml
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": 600,
    }
}

LOGGING["loggers"]["src"]["level"] = "DEBUG"  # type: ignore # noqa: F821
