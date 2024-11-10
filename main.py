from mlProject import logger
logger.info('End-To-End MLOPs Project With Deployment on AWS')

from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline


STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e


STAGE_NAME = "Data Validation Stage"
try:
   logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
   obj = DataValidationTrainingPipeline()
   obj.main()
   logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
   logger.exception(e)
   raise e


STAGE_NAME = "Data Transformation Stage"
if __name__ == '__main__':
   try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      obj = DataTransformationTrainingPipeline()
      obj.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
   except Exception as e:
      logger.exception(e)
      raise e
   

STAGE_NAME = "Model Trainer Stage"
if __name__ == '__main__':
   try:
      logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
      obj = ModelTrainerTrainingPipeline()
      obj.main()
      logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
   except Exception as e:
      logger.exception(e)
      raise e
   


import os
os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/jhahemantx/mlops.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="jhahemantx"
os.environ["MLFLOW_TRACKING_PASSWORD"]="1949f38fd472b54be1def399cc28ce4a14a2b791"

STAGE_NAME = "Model Evaluation Stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
    
import mlflow
mlflow.start_run()
print("MLflow tracking URI:", mlflow.get_tracking_uri())
mlflow.end_run()

