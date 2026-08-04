import logging
import os

os.makedirs("reports", exist_ok=True)

LOG_FILE = os.path.join("reports", "api_test.log")

logger = logging.getLogger("APITestLogger")
logger.setLevel(logging.INFO)

# Remove existing handlers
if logger.hasHandlers():
    logger.handlers.clear()

file_handler = logging.FileHandler(LOG_FILE, encoding="utf-8")
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.propagate = False