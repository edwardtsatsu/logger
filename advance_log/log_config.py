import logging
from logging.handlers import SysLogHandler
import os
from dotenv import load_dotenv
load_dotenv()

PAPERTRAIL_HOST = os.getenv("PAPERTRAIL_HOST")
PAPERTRAIL_PORT = int(os.getenv("PAPERTRAIL_PORT"))
ANALYZER = os.getenv("ANALYZER")


def create_logger() -> logging.Logger:
    logger = logging.getLogger(ANALYZER)
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    formatter = logging.Formatter(f'{ANALYZER} %(asctime)s %(levelname)s %(pathname)s:%(lineno)d %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
