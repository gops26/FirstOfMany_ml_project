import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.logger import logging
from src.exceptions import CustomException
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation, DataTransformationConfig
from src.utils import save_object
from src.components.model_trainer import ModelTrainer
@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artifacts",'train.csv')
    test_data_path:str = os.path.join("artifacts",'test.csv') 
    raw_data_path:str = os.path.join("artifacts",'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("data ingestion initiated ")
        try:
            df=pd.read_csv("notebooks\\data\\stud.csv")
            logging.info("reading the dataset as dataframe")
            # directory creation
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            # rawfile saving
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("train test split initiated")

            train_set, test_set = train_test_split(df, test_size=0.3, random_state=42)
            # train set file saving
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            # test set file saving
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            
            logging.info("data ingestion complete")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,

            )
        except Exception as e:
            raise CustomException(e,sys)



if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()

    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data_path,test_data_path)

    modeltrainer = ModelTrainer()
    best_model_r2 = modeltrainer.initiate_model_trainer(train_arr, test_arr)
    print("bestmodel score is ", best_model_r2 )


    
    
