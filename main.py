from mlProject import logger
from mlProject.pieline.stage_01_data_ingestion import DataIngestionTrainingPiepline



STAGE_NAME = "Data Ingestion Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<\n")
        data_ing = DataIngestionTrainingPiepline()
        data_ing.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e