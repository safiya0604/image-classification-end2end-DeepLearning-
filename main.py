from cnnclassfier import logger
from cnnclassfier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnclassfier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from cnnclassfier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from cnnclassfier.pipeline.stage_04_evaluation import EvaluationPipeline
STAGE_NAME="Data ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started")
    obj=DataIngestionPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Prepare base Model"
try:
    logger.info("***********")
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} <<<<<<<<<<<")
    prepare_base_model=PrepareBaseModelPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx==============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Training"
try:
    logger.info("***********")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started")
    model_trainer=ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="EVALUATION STAGE"
try:
    logger.info("***********")
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started")
    model_evaluation=EvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed")
except Exception as e:
    logger.exception(e)
    raise e