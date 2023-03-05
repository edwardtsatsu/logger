import logging
from logging.handlers import SysLogHandler
from coloredlogs import ColoredFormatter
import os
from dotenv import load_dotenv

load_dotenv()

ANALYZER = os.getenv("ANALYZER")
PAPERTRAIL_HOST = os.getenv("PAPERTRAIL_HOST")
PAPERTRAIL_PORT = int(os.getenv("PAPERTRAIL_PORT"))

def create_logger() -> logging.Logger:
    logger = logging.getLogger(ANALYZER)
    logger.setLevel(logging.DEBUG)

    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    handler.setLevel(logging.DEBUG)

    formatter = ColoredFormatter(f'{ANALYZER} %(asctime)s %(levelname)s %(pathname)s:%(lineno)d %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger







