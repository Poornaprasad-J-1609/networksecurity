from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import Training_pipeline_config
import sys

if __name__ =='__main__':
    try:
        trainingpipelineconfig = Training_pipeline_config()
        data_ingestion_config= DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        data_ingestion= DataIngestion(data_ingestion_config=data_ingestion_config)
        logging.info("initiate Data Ingestion")
        dataingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(dataingestion_artifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
  