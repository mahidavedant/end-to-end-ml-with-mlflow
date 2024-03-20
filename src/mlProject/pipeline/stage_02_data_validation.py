"""
src/mlProject/pipeline/stage_02_data_validation.py

Pipeline
----------------------------------
Stage 02: Data validation          
----------------------------------
"""
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValidation
from mlProject.logging.customLogger import logger

STAGE_NAME = 'Data Validation stage'


class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(
            f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nX==========X")

    except Exception as e:
        logger.exception(e)
        raise e
