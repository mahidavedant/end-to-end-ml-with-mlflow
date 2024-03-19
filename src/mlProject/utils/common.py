"""
src/mlProject/utils/common.py

Module for commong utility functions.
"""
import os
from box.exceptions import BoxValueError
import yaml
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from mlProject.logging.customLogger import logger


@ensure_annotations
def create_directories(directory_paths: list, verbose=True):
    """
    Create list of directories.

    Args:
      directory_paths (list): list of path of directories.
    """
    for path in directory_paths:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB.

    Args:
      path (Path): path like input.

    Returns:
      str: size in KB
    """
    size_in_kb = round(os.path.getsize(path))
    return f"~ {size_in_kb} KB"


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read YAML file and return it.

    Args:
      path_to_yaml (Path): path like input

    Raises:
      ValueError: if yaml file is empty
      e: empty file 

    Returns:
      ConfigBox: configbox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file: {yaml_file} loaded successfully!")

            return ConfigBox(content)

    except BoxValueError:
        raise ValueError('YAML file is empty.')
    except Exception as e:
        raise e


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save json data.

    Args:
      path (Path): Path to json file.
      data (dict): data to be saved to json file.
    """
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)

    logger.info(f"JSON file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Load json file.

    Args:
      path (Path): Path to json file.

    Returns:
      ConfigBox: configbox type
    """
    with open(path) as f:
        content = json.load(path)
    logger.info(f"JSON file loaded from: {path}")

    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Save json data.

    Args:
      data (Any): data to be saved as binary.
      path (Path): Path to binary file.
    """
    joblib.dump(data, path)
    logger.info(f"Binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load binary file.

    Args:
      path (Path): Path to binary file.

    Returns:
      Any: Object stored in file.
    """
    data = joblib.load(path)
    logger.info(f"Binary file loaded from: {path}")

    return data
