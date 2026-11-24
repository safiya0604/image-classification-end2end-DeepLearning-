import os
import json
import joblib
from box.exceptions import BoxValueError
import yaml
import base64
from typing import Any
from pathlib import Path
from box import ConfigBox
from cnnclassfier import logger
from ensure import ensure_annotations

@ensure_annotations
def read_yaml(path_to_yaml:Path) ->ConfigBox:
    #read yaml file and return config box:config box type
    try:
        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)
            logger.info(f"yaml file:{path_to_yaml} loaded sucessfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories:list,verbose=True):
    #create list of directories  where list has path of each nd ignore if multiple dirs is to be created.Defaults to False
    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(F"CREATED DIRECTORY AT :{path}")         

@ensure_annotations
def get_size(path:Path)->set:
    #return size on kb
    size_in_kb=round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"

@ensure_annotations
def save_json(path:Path,data:dict):
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"json file saved at: {path}")

@ensure_annotations
def load_json(path:Path) -> ConfigBox:
    with open(path)as f:
        content=json.read(f)
    logger.info(f"json file loaded successfully from :{path}")
    
def decodeImage(imgstring,fileName):
    imgdata=base64.b64decode(imgstring)
    with open(fileName,"wb") as f:
        f.write(imgdata)
        f.close()
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath,"rb") as f:
        return base64.b64encode(f.read())   