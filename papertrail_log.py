import logging
from logging.handlers import SysLogHandler


PAPERTRAIL_HOST = "logs5.papertrailapp.com"
PAPERTRAIL_PORT = 25167


def log_message() -> object:
    logger = logging.getLogger("edwardtsatsu")
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    logger.addHandler(handler)

    return logger


def even_number(number):
    try:
        log = log_message()
        if number % 2 == 0:
            log.info(f"ths number {number} is even")
        else:
            log.info(f"ths number {number} is odd")
    except Exception as e:
        log.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    even_number(5396)
    even_number(2)
    even_number(3)
    even_number("four")
