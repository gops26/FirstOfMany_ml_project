from sklearn.ensemble import AdaBoostRegressor, GradientBoostingRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import Ridge, LinearRegression, Lasso
from xgboost import XGBRegressor
from sklearn.neighbors import KNeighborsRegressor

from src.logger import logging
from src.exceptions import CustomException
from src.utils import save_object,evaluate_model
from dataclasses import dataclass
import os, sys

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:,-1]
            )

            models = {
                "random forest":RandomForestRegressor(),
                "Decision tree regressor":DecisionTreeRegressor(),
                "ada boost": AdaBoostRegressor(),
                "ridge": Ridge(),
                "lasso": Lasso(),
                "linear_model": LinearRegression(),
                "xgb regressor": XGBRegressor(),
                "k nearest neighbor regressor":KNeighborsRegressor()

            }
            params = {
                "random forest":{
                    "n_estimators":[50,100,200,500,1000],
                    "criterion":["squared_error", "absolute_error", "friedman_mse", "poisson"],
                    "max_depth":[1,2,5,8,10],
                    "max_features":["sqrt", "log2"]
                },
                "Decision tree regressor":{
                    "criterion":["squared_error", "absolute_error", "friedman_mse", "poisson"],
                    "max_depth":[1,2,5,8,10],
                    "max_features":["sqrt", "log2"],
                    # "n_estimators":[50,100,200,500,1000],

                    
                },
                "ridge":{},
                "lasso":{},
                "ada boost": {
                    "n_estimators":[50,100,200,500,1000],
                    "loss":['linear', 'square', 'exponential'],
                    'learning_rate':[0.01,0.1]
                },
                "linear_model":{},
                "xgb regressor": {
                    "n_estimators":[50,100,200,500,1000],
                    "max_depth":[1,2,5,8,10],
                    "learning_rate":[0.1,0.01]

                },
                "k nearest neighbor regressor":{
                    "n_neighbors":[2,3,4,5,6],
                    "algorithm":["ball_tree", "kd_tree", "brute"],
                    "weights":["uniform", "distance"],
                    "leaf_size":[10,20,30,40,50]
                }
            }
            model_report:dict= evaluate_model(X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test, models=models, params=params)

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("best optimized model not found")
            logging.info(f"best found model on both training and testing dataset") 

            save_object(
                self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            logging.info("saved model object ")
          
            return best_model_score
        except Exception as e:
            raise CustomException(e, sys)
