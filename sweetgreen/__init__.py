"""
sweetgreen analysis repository
"""

import logging
import time


def getLogger():

    logger = logging.getLogger()

    if not logging.root.handlers:
        logger.setLevel(level=logging.INFO)

        file_handler = logging.FileHandler("SweetGreen.log", encoding="utf-8")

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)-8s %(name)s - %(message)s",
            "%Y-%m-%d %H:%M:%S UTC",
        )
        formatter.converter = time.gmtime

        file_handler.setFormatter(formatter)
        file_handler.converter = time.gmtime

        # Also log to console
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(stream_handler)

    return logger


from . import utils, data, web
