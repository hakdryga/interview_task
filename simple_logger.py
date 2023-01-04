import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
log_file_handler = logging.FileHandler('log.txt')
log_file_handler.setLevel(logging.DEBUG)
log_file_handler.setFormatter(formatter)
logger.addHandler(log_file_handler)