from Network_Security.Components.Data_Ingestion import DataIngestion
from Network_Security.Entity.config_entity import DataIngestionConfig
from Network_Security.Entity.config_entity import TrainingPipelineConfig
from Network_Security.Logging.Logger import logging
from Network_Security.Exception_Handling.Exception import NetworkSecurityException

if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiating Data Ingestion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)

    except Exception as e:
        raise NetworkSecurityException(e,sys)