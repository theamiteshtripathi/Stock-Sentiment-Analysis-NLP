import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "stockSentimentAnalysis"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/preprocessing/__init__.py",
    f"src/{project_name}/preprocessing/clean_text.py",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/models/train.py",
    f"src/{project_name}/models/predict.py",
    f"src/{project_name}/models/evaluate.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/visualization/__init__.py",
    f"src/{project_name}/visualization/visualize.py",
    "notebooks/model_exploration.ipynb",
    "data/raw/.gitkeep",
    "data/processed/.gitkeep",
    "models/.gitkeep",
    "tests/.gitkeep",
    "requirements.txt",
    "README.md",
    ".gitignore"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, "w", encoding="utf-8") as f:
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filename}")
