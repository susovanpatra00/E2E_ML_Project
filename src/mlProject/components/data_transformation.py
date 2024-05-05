import os
from mlProject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlProject.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    ## Note: We can add diff data transformation techniques such as Scalar, PCA and etc
    # We can perform all kinds of EDA in ML Cycle here before passing it to the model
    # Here we will only split the data nothng else to keep it simple (as already cleaned)

    def train_test_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splitted data into training and test sets")
        logger.info(f"Train Data Shape : {train.shape}")
        logger.info(f"Test Data Shape: {test.shape}")



    

