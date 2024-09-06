"""Template for local development settings."""
DEBUG = True
SECRET_KEY = "some_secret_key"

IN_DOCKER = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": 600,
    }
}

LOGGING['formatters']['colored'] = {  # type: ignore
    "()": "colorlog.ColoredFormatter",
    "format": "%(log_color)s%(asctime)s %(levelname)s %(name)s %(name)s %(bold_white)s%(message)s",
}
LOGGING["loggers"]["src"]["level"] = "DEBUG"  # type: ignore
LOGGING["loggers"]["console"]["level"] = "DEBUG"  # type: ignore
LOGGING["loggers"]["console"]["formatters"] = "colored"  # type: ignore
