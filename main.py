from textSummarizer.pipeline.num1_data_ing import DataIngestionTrainingPipeline
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
