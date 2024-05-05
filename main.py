from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPiepline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPiepline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationPiepline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPiepline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

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
    


STAGE_NAME = "Data Transformation Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<\n")
        obj = DataTransformationPiepline()
        obj.main()
        logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME = "Model Trainer Stage"
if __name__ == "__main__":
    try:
        logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<\n")
        obj = ModelTrainerTrainingPiepline()
        obj.main()
        logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx============x")
    except Exception as e:
        logger.exception(e)
        raise e
    


STAGE_NAME = "Model evaluation stage"
if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e