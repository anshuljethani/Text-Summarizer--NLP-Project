from textSummarizer.pipeline.num1_data_ing import DataIngestionTrainingPipeline
from textSummarizer.pipeline.num2_data_valid import DataValidationTrainingPipeline
from textSummarizer.logging import logger,logging


#1

STAGE_NAME = "Data Ingestion stage"
try:
   logger.info(f"*** {STAGE_NAME} started *** ") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f"*** {STAGE_NAME} completed *** \n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e

#2

STAGE_NAME = "Data Validation stage"
try:
   logger.info(f"*** {STAGE_NAME} is getting started *** ") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f"*** {STAGE_NAME} completed *** \n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e