"""Settings file that is used when running app in github action."""

DEBUG = True
SECRET_KEY = "githubworkflowdjangosecretkey"

# Database settings must be same in the .yaml git actions files in .github
DATABASES = { # DATABASE prod settings
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db", ## Also being set in git actions file (for example see .github/workflow/commit.yaml)
        "PORT": "5432",
        "ATOMIC_REQUESTS": True,
        "CONN_MAX_AGE": 600,
    }
}
