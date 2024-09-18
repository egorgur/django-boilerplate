"""Try to setup environment and install packages with poetry."""

import os

try:
    os.system("poetry env use python")
    os.system("poetry install")
except Exception:
    print("Could not setup venv or install packages with poetry.")
