"""
src/mlProject/components/data_ingestion.py

Data ingestion.
"""
import os
from pathlib import Path
import urllib.request as request
import zipfile
from mlProject.logging.customLogger import logger
from mlProject.utils.common import get_size
from mlProject.entity.config_entity import DataIngestionConfig
import ssl

ssl._create_default_https_context = ssl._create_stdlib_context


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        filename = self.config.local_data_file
        # download data file from src url to local file
        if not os.path.exists(filename):
            filename, headers = request.urlretrieve(
                url=self.config.source_url,
                filename=filename
            )
            logger.info(
                f"{filename} downloaded with following info: \n{headers}")

        else:
            logger.info(
                f"{filename} already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        # unzip files in local data file
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
