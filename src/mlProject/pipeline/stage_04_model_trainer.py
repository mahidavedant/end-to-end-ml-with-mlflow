"""
src/mlProject/pipeline/stage_04_model_trainer.py

Pipeline
----------------------------------
Stage 04: Model trainer       
----------------------------------
"""
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_trainer import ModelTrainer
from mlProject.logging.customLogger import logger
from pathlib import Path

STAGE_NAME = 'Model Trainer stage'


class ModelTrainerTrainningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainningPipeline()
        obj.main()
        logger.info(
            f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nX==========X")

    except Exception as e:
        logger.exception(e)
        raise e

