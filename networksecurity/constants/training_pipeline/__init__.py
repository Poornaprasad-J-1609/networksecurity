import os
import sys
import pandas as pd
import numpy as np

TARGET_COLUMN = 'CLASS_LABEL'
PIPELINE_NAME = 'NetworkSecurity'
ARTIFACT_DIR = 'Artifacts'
FILE_NAME = 'data.csv'
TRAIN_FILE_NAME:str='train.csv'
TEST_FILE_NAME:str='test.csv'

DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str="PRASADAI"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_store"
DATA_INGESTION_INGESTION_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2