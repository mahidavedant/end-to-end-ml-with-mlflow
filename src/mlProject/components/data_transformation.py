"""
src/mlProject/components/data_transformation.py

Data transformation.
"""
import os
import pandas as pd
from mlProject.logging.customLogger import logger
from mlProject.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # Note: We can add different data transformations such as Scaler, Onehot encoding etc.
    # All kinds of EDA in ML cycle can also be passed here before passing data to the model.
    # Only train test split is added here because data is already clean and ready for use.

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)
        # train test split (0.80, 0.20)
        train, test = train_test_split(data)

        train.to_csv(os.path.join(
            self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(
            self.config.root_dir, 'test.csv'), index=False)

        logger.info("Splitted data into train and test sets.")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
