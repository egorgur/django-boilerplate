LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "standard",
            "filters": [],
        },
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "logs/debug.log",
            "encoding": "utf-8",
            "formatter": "standard",
            "filters": [],
        },
    },
    "loggers": {
        logger_name: {
            "level": "WARNING",
            "propagate": True,
            "handlers": ["file"],
        } for logger_name in ("django", "django.request", "django.db.backends", "django.template", "src", "console")
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["console"],
    }
}

