"""
src/mlProject/components/model_trainer.py

Model trainer.
"""
import os
import pandas as pd
import joblib
from mlProject.logging.customLogger import logger
from sklearn.linear_model import ElasticNet
from mlProject.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        # Train and test sets
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # Model building and training
        lr = ElasticNet(alpha=self.config.alpha,
                        l1_ratio=self.config.l1_ratio, random_state=42)
        lr.fit(train_x, train_y)

        # Save model
        joblib.dump(lr, os.path.join(
            self.config.root_dir, self.config.model_name))
