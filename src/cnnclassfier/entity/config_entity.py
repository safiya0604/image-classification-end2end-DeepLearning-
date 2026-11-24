from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir:Path
    source_url:str
    local_data_file:Path
    unzip_dir:Path
    direct_data_folder:Path

@dataclass(frozen=True)
class PreprareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights: str
    params_classes: int

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    train_model_path: Path
    updated_base_model_path: Path
    training_data: Path
    params_epochs: int
    params_batch_size: int
    params_is_augmentation: bool
    params_image_size: list

@dataclass(frozen=True)
class EvaluationConfig:
    path_of_model: Path
    training_data: Path
    all_params: dict
    mlflow_uri: str
    params_image_size: list
    params_batch_size: int








    
    #same as ml project but in this we are just defining the type unlike converting the name to path in ml project
    #and it is updated with config.yaml string unlike directly as before but my config manger
    #these values are assign my manager in pipeline part when we call component class throgh an object and object needs its attribute that is passed there