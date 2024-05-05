import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from mlProject.config.configuration import ConfigurationManager
from mlProject.components.data_ingestion import DataIngestion
from mlProject import logger


STAGE_NAME = "Data Ingestion Stage"
class DataIngestionTrainingPiepline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()                             
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<\n")
        obj = DataIngestionTrainingPiepline()
        obj.main()
        logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e



"""
Refer to research/01_data_ingestion.ipynb for details
"""