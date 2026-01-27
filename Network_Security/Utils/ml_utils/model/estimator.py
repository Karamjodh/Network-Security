import os
import sys
from Network_Security.Logging.Logger import logging
from Network_Security.Exception_Handling.Exception import NetworkSecurityException
from Network_Security.Constants.Training_Pipeline import SAVED_MODEL_DIR,MODEL_FILE_NAME

class NetworkModel:
    def __init__(self,preprocessor,model):
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def predict(self,x):
        try:
            X_transform = self.preprocessor.transform(x)
            Y_hat = self.model.predict(X_transform)
            return Y_hat
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)