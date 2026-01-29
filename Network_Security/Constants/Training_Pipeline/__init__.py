import os
import numpy as np

"""
defining common constant variables
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME = "NetworkSecurity"
ARTIFACT_DIR = "Artifacts"
FILE_NAME = "phishingData.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

SAVED_MODEL_DIR = os.path.join("saved_models") 
MODEL_FILE_NAME = "model.pkl"

"""
Data Ingestion related constant 
"""
DATA_INGESTION_COLLECTION_NAME : str = "NetworkData"
DATA_INGESTION_DATABASE_NAME : str = "karamjodh_db_user"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO : float = 0.2



#                                         --------feature_store/phishingData.csv
#                                        |
#                                        |
# Artifacts/TimeStamp/data_ingestion------                       --------train.csv
#                                        |                      |
#                                        |                      |
#                                         ---------ingested------
#                                                               |
#                                                               |
#                                                                --------test.csv

"""
Data Validation related constants 
"""

DATA_VALIDATION_DIR_NAME : str = "data_validation"
DATA_VALIDATION_VALID_DIR : str = "validated"
DATA_VALIDATION_INVALID_DIR : str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR : str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME : str = "report.yaml"
PREPROCESSING_OBJECT_FILE_NAME : str = "preprocessing.pkl"
SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")

"""
Data transformation related constants
"""
DATA_TRANSFORMATION_DIR_NAME : str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR : str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR : str = "transformed_object"
DATA_TRANSFORMATION_TRANSFORMED_IMPUTER_PARAMS : dict = {
    "missing_values" : np.nan,
    "n_neighbors" : 3,
    "weights" : "uniform",
}

"""
Model Trainer related constants
"""

MODEL_TRAINER_DIR_NAME = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD = 0.05

TRAINING_BUCKET_NAME = "networksecuritykrm"