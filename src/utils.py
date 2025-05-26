import numpy as np
import pandas as pd
import dill,pickle
import sys,os
from sklearn.model_selection import GridSearchCV  
from sklearn.metrics import r2_score 

from src.exceptions import CustomException
from src.logger import logging

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as er:
        raise CustomException(er,sys)
    
def load_object(filepath):
        with open(filepath,'rb') as f:
            object_ = dill.load(f)
        return object_
    
def evaluate_model(X_train, y_train, X_test, y_test, models:dict, params):
    try:
        reports={}
        for i in range(len(list(models.values()))):
            model_name = list(models.keys())[i]

            model = list(models.values())[i]
            param = params[model_name]

            logging.info("grid search started")
            gs = GridSearchCV(estimator=model, cv=3, param_grid=param)
            gs.fit(X_train, y_train)
            model.set_params(**gs.best_params_)
            logging.info("grid search selected best param")


            model.fit(X_train, y_train) 

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_score= r2_score(y_train, y_train_pred)
            test_score= r2_score(y_test, y_test_pred)

            reports[model_name] =test_score
        
        return reports


    except Exception as e:
        raise CustomException(e, sys)
