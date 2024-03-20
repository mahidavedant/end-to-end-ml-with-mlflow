"""
main.py
"""
from mlProject.logging.customLogger import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPipeline
from mlProject.pipeline.stager_04_model_trainer import ModelTrainerTrainningPipeline


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


# test stage-03
STAGE_NAME = 'Data Transformation stage'
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    data_transformation = DataTransformationPipeline()
    data_transformation.main()
    logger.info(
        f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nX==========X")

except Exception as e:
    logger.exception(e)
    raise e


# test stage-04
STAGE_NAME = 'Model Trainer stage'
try:
    logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    obj = ModelTrainerTrainningPipeline()
    obj.main()
    logger.info(
        f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nX==========X")

except Exception as e:
    logger.exception(e)
    raise e
