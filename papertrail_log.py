import logging
from logging.handlers import SysLogHandler


class NumberAnalyzer:
    def __init__(self, logger):
        self.logger = logger

    def is_even(self, number):
        try:
            if number % 2 == 0:
                self.logger.info(f"The number {number} is even")
            else:
                self.logger.info(f"The number {number} is odd")
        except Exception as e:
            self.logger.exception(f"An error occurred: {str(e)}")


def create_logger(analyzer):
    logger = logging.getLogger(analyzer)
    logger.setLevel(logging.DEBUG)
    handler = SysLogHandler(address=(PAPERTRAIL_HOST, PAPERTRAIL_PORT))
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(pathname)s:%(lineno)d %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    load_dotenv()

    PAPERTRAIL_HOST = os.getenv("PAPERTRAIL_HOST")
    PAPERTRAIL_PORT = int(os.getenv("PAPERTRAIL_PORT"))
    ANALYZER = os.getenv("ANALYZER")

    logger = create_logger(ANALYZER)
    analyzer = NumberAnalyzer(logger)

    analyzer.is_even(5396)
    analyzer.is_even(2)
    analyzer.is_even(3)
    analyzer.is_even("four")
