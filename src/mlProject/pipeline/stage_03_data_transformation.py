from mlProject.config.configuaration import ConfigurationManager
from mlProject.components.data_transformation import DataTransformation
from mlProject import logger
from pathlib import Path


STAGE_NAME = "Data Transformation Stage"
class DataTransformationPiepline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":
                config = ConfigurationManager()                             
                data_transformation_config = config.get_data_transfomration_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()
            else:
                raise Exception("Your Data Schema Is Not Valid")
        
        except Exception as e:
            print(e)


        

if __name__ == "__main__":
    try:
        logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<\n")
        obj = DataTransformationPiepline()
        obj.main()
        logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e



"""
Refer to research/03_data_transformation.ipynb for details
"""