import logging





def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.warning('This is a warning message')
    logging.info('This is an info message')
    logging.debug('This is a debug message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')



if __name__ == '__main__':
    main()
