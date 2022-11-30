import logging
import colorlog
from datetime import datetime
import os

def get_logger(log_directory: str) -> logging.Logger:
    log_format = (
        '%(asctime)s - '
        '%(name)s - '
        '%(funcName)s - '
        '%(levelname)s - '
        '%(message)s'
    )
    bold_seq = '\033[1m'
    colorlog_format = (
        f'{bold_seq} '
        '%(log_color)s '
        f'{log_format}'
    )
    colorlog.basicConfig(format=colorlog_format)
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    fh = logging.FileHandler("app-" + datetime.now().strftime("%m-%d-%Y-%H:%M:%S") + ".log", mode='w')
    fh.setLevel(logging.DEBUG)
    formatter = logging.Formatter(log_format)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
