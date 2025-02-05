from enum import Enum
import time
import logging
import logging.config


class Format(Enum):
    console = "console"
    json = "json"


class LogLevels(Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"


def init_logging(
    log_level: LogLevels = LogLevels.INFO, format: Format = Format.console
) -> logging.Logger:
    LOG_CONFIG = {
        "version": 1,
        "handlers": {
            "stdout": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": format.value,
            }
        },
        "formatters": {
            "json": {
                "format": (
                    '{"msg":"%(message)s","level":"%(levelname)s",'
                    '"file":"%(filename)s","line":%(lineno)d,'
                    '"module":"%(module)s","func":"%(funcName)s"}'
                ),
                "datefmt": "%Y-%m-%dT%H:%M:%SZ",
            },
            "console": {
                "format": "%(asctime)s %(levelname)s : %(message)s [%(module)s.%(funcName)s - %(filename)s:%(lineno)d]",
                "datefmt": "%Y-%m-%dT%H:%M:%SZ",
            },
        },
        "root": {"handlers": ["stdout"], "level": log_level.value},
    }
    logging.Formatter.converter = time.gmtime
    logging.config.dictConfig(LOG_CONFIG)
    logger = logging.getLogger(__name__)

    return logger
