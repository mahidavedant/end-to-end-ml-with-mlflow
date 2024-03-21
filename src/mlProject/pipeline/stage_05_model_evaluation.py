"""
src/mlProject/pipeline/stage_05_model_evaluation.py

Pipeline
----------------------------------
Stage 05: Model evaluation       
----------------------------------
"""
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.model_evaluation import ModelEvaluation
from mlProject.logging.customLogger import logger

STAGE_NAME = 'Model Evaluation stage'


class ModelEvaluationTrainningPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_evaluation_config()
        model_eval = ModelEvaluation(config=model_eval_config)
        model_eval.log_into_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainningPipeline()
        obj.main()
        logger.info(
            f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\nX==========X")

    except Exception as e:
        logger.exception(e)
        raise e
