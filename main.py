from mlProject import logger
from mlProject.pieline.stage_01_data_ingestion import DataIngestionTrainingPiepline
from mlProject.pieline.stage_02_data_validation import DataValidationTrainingPiepline



STAGE_NAME = "Data Ingestion Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<\n")
        data_ing = DataIngestionTrainingPiepline()
        data_ing.main()
        logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME = "Data Validation Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<\n")
        obj = DataValidationTrainingPiepline()
        obj.main()
        logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e