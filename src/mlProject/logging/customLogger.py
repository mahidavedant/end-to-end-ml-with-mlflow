"""
src/mlProject/logging/customLogger.py

Custom logger.
"""
import os
import sys
import logging

LOG_FORMAT = '%(asctime)s %(module)s:%(lineno)d %(levelname)s %(message)s'
DATE_FMT = '%b %d %H:%M:%S'

log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'running_logs.log')

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=LOG_FORMAT,
    datefmt=DATE_FMT,
    handlers={
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    }
)

logger = logging.getLogger(__name__)
