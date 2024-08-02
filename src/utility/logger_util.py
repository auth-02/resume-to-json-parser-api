import logging
import os
from logging.handlers import TimedRotatingFileHandler
import datetime

def get_logger(module):

    logs_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "..", 
        "logs"
    )


    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)


    log_file = os.path.join(
        logs_dir, 
        f"{module}_{datetime.datetime.now().strftime('%Y_%m_%d')}.txt"
    )

    logger = logging.getLogger(module)
    logger.setLevel(logging.DEBUG)

    fh = TimedRotatingFileHandler(log_file, when="midnight", interval=1, encoding="utf-8")
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger
