DEBUG = True

LOGGING["formatters"]["colored"] = {  # type: ignore # noqa: F821
    "()": "colorlog.ColoredFormatter",
    "format": "%(log_color)s%(asctime)s %(levelname)s %(name)s %(name)s %(bold_white)s%(message)s",
}
LOGGING["loggers"]["src"]["level"] = "DEBUG"  # type: ignore # noqa: F821
LOGGING["loggers"]["console"]["level"] = "DEBUG"  # type: ignore # noqa: F821
LOGGING["loggers"]["console"]["formatters"] = "colored"  # type: ignore # noqa: F821
