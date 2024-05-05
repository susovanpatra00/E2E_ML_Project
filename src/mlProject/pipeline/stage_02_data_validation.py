from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_validation import DataValiadtion
from mlProject import logger


STAGE_NAME = "Data Validation Stage"
class DataValidationTrainingPiepline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()                             
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<\n")
        obj = DataValidationTrainingPiepline()
        obj.main()
        logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e



"""
Refer to research/02_data_validation.ipynb for details
"""