from advance_log.log_config import create_logger


class NumberAnalyzer:
    def __init__(self,logger):
        self.logger = logger


    def is_even(self,number):
        try:
            if number % 2 == 0:
                self.logger.info(f"The number {number} is even")
            else:
                self.logger.info(f"The number {number} is odd")
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")




if __name__ == "__main__":
    analyzer = NumberAnalyzer(create_logger())

    analyzer.is_even(5396)
    analyzer.is_even(2)
    analyzer.is_even(3)
    analyzer.is_even("four")
