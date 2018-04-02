# pylint: disable=C0111, C0103
import logging
import config

logger = logging.getLogger(config.MODULE_NAME)
logger.setLevel(config.LOG_LEVEL)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

if config.LOG_TO_FILE:
    fh = logging.FileHandler(config.LOG_FILE)
    fh.setLevel(config.LOG_LEVEL)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

if config.LOG_TO_STREAM:
    ch = logging.StreamHandler()
    ch.setLevel(config.LOG_LEVEL)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
