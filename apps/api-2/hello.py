import utils
from utils.logging import init_logging, Format, LogLevels

LOG = init_logging(format=Format.console, log_level=LogLevels.DEBUG)


def main():
    LOG.info(utils.hello())

    LOG.warning("warning message")

    try:
        raise Exception("Houston, we have a problem")
    except Exception as e:
        LOG.error(e, exc_info=True, stack_info=True)

    LOG.debug("debug message after exception")


if __name__ == "__main__":
    main()
