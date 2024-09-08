import os.path
import ipdb
from pathlib import Path

from split_settings.tools import include, optional

BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

# Prefix for project environment variables namespace.
ENVIRONMENT_PREFIX = "DJANGO_PROJECT_"

LOCAL_SETTINGS_PATH: str | None = os.getenv(f"{ENVIRONMENT_PREFIX}LOCAL_SETTINGS_PATH")

if not LOCAL_SETTINGS_PATH:
    LOCAL_SETTINGS_PATH = "local/settings.dev.py"

if not os.path.isabs(LOCAL_SETTINGS_PATH):
    LOCAL_SETTINGS_PATH = str(BASE_DIR / LOCAL_SETTINGS_PATH)

# Order of the settings loading
include(
    "base.py",
    "app_specific.py",
    optional(LOCAL_SETTINGS_PATH),
    "environment.py",
    "docker.py",
    "logging.py",
)
