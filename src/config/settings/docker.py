# IN_DOCKER gets imported from settings.__init__.py by split_settings
# MIDDLEWARE gets imported from settings.__init__.py by split_settings
if IN_DOCKER:  # type: ignore
    assert MIDDLEWARE[:1] == [  # type: ignore
        "django.middleware.security.SecurityMiddleware"
    ]
