from Network_Security.Entity.artifact_entity import ClassificationMetricArtifact
from Network_Security.Exception_Handling.Exception import NetworkSecurityException
from sklearn.metrics import f1_score,precision_score,recall_score

def get_classification_score(Y_true,Y_pred)->ClassificationMetricArtifact:
    try:
        model_f1_score = f1_score(Y_true,Y_pred)
        model_recall_score = recall_score(Y_true,Y_pred)
        model_precision_score = precision_score(Y_true,Y_pred)
        classification_metric = ClassificationMetricArtifact(
            f1_score = model_f1_score,recall_score = model_recall_score,precision_score=model_precision_score)
        return classification_metric
    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
