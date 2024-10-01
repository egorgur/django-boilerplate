"""Template for testing."""

DEBUG = True

# Test database !! SET YOUR LOCAL DATABASE FOR TESTING OR USE IN-DOCKER POSTGRES !!
DATABASES = { # IN-DOCKER postgres
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
