import os
import logging
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s %(module)s %(levelname)s %(message)s', datefmt='%b %d %H:%M:%S')

project_name = 'mlProject'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/customLogger.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",    
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "notebooks/trials.ipynb",
    "templates/index.html"
]


# Create folder structure from list of files
for filepath in list_of_files:
    filepath = Path(filepath)
    directory, filename = os.path.split(filepath)

    # Create directory
    if directory != "":
        os.makedirs(directory, exist_ok=True)
        logging.info(f"Creating directory: {directory} for file {filename}")

    # Create file
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"File {filename} already exists.")
