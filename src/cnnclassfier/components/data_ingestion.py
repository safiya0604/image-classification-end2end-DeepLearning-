import os
import zipfile
import gdown
from cnnclassfier import logger
from cnnclassfier.utils.common import get_size
from cnnclassfier.entity.config_entity import DataIngestionConfig
import shutil

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config

    # def download_file(self) -> str:
    #     #fetch data from url
    #     try:
    #         dataset_url=self.config.source_url
    #         zip_download_dir=self.config.local_data_file
    #         os.makedirs("artifacts/data_ingestion",exist_ok=True)
    #         logger.info(f"Downloading data from {dataset_url} inot file {zip_download_dir}")
    #         file_id=dataset_url.split("/")[-2]
    #         prefix="http://drive.google.com/uc?/export=download&id="
    #         gdown.download(prefix+file_id,zip_download_dir)
    #     except Exception as e:
    #         raise e

    # def extract_zip_file(self):
    #     #extract zip file into the data dir
    #     unzip_path=self.config.unzip_dir
    #     os.makedirs(unzip_path,exist_ok=True)
    #     with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
    #         zip_ref.extractall(unzip_path)


    def direct_ingestion(self):
        try:
            unzip_path=self.config.unzip_dir
            os.makedirs(unzip_path,exist_ok=True)
            data_folder=self.config.direct_data_folder
            if not os.path.exists(data_folder):
                logger.info(f"Data not found at:{data_folder}")
            shutil.copytree(data_folder,unzip_path,dirs_exist_ok=True)
            logger.info(f"Datast copied successfully to {unzip_path}")
        except Exception as e:
            raise e
    