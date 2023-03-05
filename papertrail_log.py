import logging
from logging.handlers import SysLogHandler
import os
from dotenv import load_dotenv


load_dotenv()

PAPERTRAIL_HOST = os.getenv("PAPERTRAIL_HOST")
PAPERTRAIL_PORT = int(os.getenv("PAPERTRAIL_PORT"))
analyzer = os.getenv("ANALYZER")


def create_logger():
    logger = logging.getLogger(analyzer)
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(pathname)s:%(lineno)d %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


def even_number(number):
    try:
        log = create_logger()
        if number % 2 == 0:
            log.info(f"ths number {number} is even")
        else:
            log.info(f"ths number {number} is odd")
    except Exception as e:
        log.exception(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    even_number(5396)
    even_number(2)
    even_number(3)
    even_number("four")
