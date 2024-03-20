"""
testing.py

Run test to make sure everything is running as expected.
"""
from mlProject.logging.customLogger import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

# test stage-01
STAGE_NAME = 'Data Ingestion stage'
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(
        f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nX==========X")

except Exception as e:
    logger.exception(e)
    raise e

# test stage-02
STAGE_NAME = 'Data Validation stage'
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(
        f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nX==========X")

except Exception as e:
    logger.exception(e)
    raise e
