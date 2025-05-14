import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("SeleniumTest")
    logger.setLevel(logging.INFO)
    handler = logging.FileHandler("logs/test.log")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    if not logger.handlers:
        logger.addHandler(handler)
    return logger