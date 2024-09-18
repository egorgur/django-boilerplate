import os

from invoke import task


@task(name="copysettings")
def copy_settings(c):
    """
    Copy the project's settings from the templates.

    Mkdir ./local folder and copy the settings templates in it.
    """

    if not os.path.exists("local"):
        os.makedirs("local")
    # TODO! Rework the cmd commands with os.system() or other os. methods
    c.run("cp src/config/settings/templates/settings.devsetup.py ./local/settings.dev.py")
    c.run("cp src/config/settings/templates/settings.testing.py ./local/settings.testing.py")
    c.run("cp src/config/settings/templates/settings.prod.py ./local/settings.prod.py")
