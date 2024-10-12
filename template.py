import os
from pathlib import Path

# Project name (root folder)
project_name = "us_visa"

# List of folders and files to create in the project structure
list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifact_entity.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
]


def create_project_structure(list_of_files):
    for file in list_of_files:
        file_path = Path(file)
        directory = file_path.parent  # Get the directory of the file

        # Create the directories if they don't exist
        directory.mkdir(parents=True, exist_ok=True)

        # Create the file
        if not file_path.exists():
            file_path.touch()  # This will create an empty file
            print(f"Created file: {file_path}")
        else:
            print(f"File already exists: {file_path}")


if __name__ == "__main__":
    create_project_structure(list_of_files)
    print("Project structure created successfully.")
