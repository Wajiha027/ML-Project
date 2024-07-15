# Student Performance Analysis

This repository contains a project for analyzing and predicting student performance based on various factors such as gender, parental level of education, lunch type, and test preparation course. The dataset includes scores for math, reading, and writing.

## Dataset

The dataset contains the following columns:
- `gender`: Gender of the student (male/female)
- `race_ethnicity`: Group the student belongs to
- `parental_level_of_education`: Highest level of education attained by parents
- `lunch`: Type of lunch (standard/free/reduced)
- `test_preparation_course`: Completion status of test preparation course (none/completed)
- `math_score`: Math score of the student
- `reading_score`: Reading score of the student
- `writing_score`: Writing score of the student

### Files Description

- `.dvc`: DVC (Data Version Control) configuration files for data tracking.
- `artifacts`: Directory containing generated artifacts.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `model.pkl`: Trained model file.
- `preprocessor.pkl`: Preprocessing pipeline file.
- `raw.csv.dvc`: DVC tracked raw data file.
- `test.csv`: Test dataset.
- `train.csv`: Training dataset.
- `notebook`: Directory containing Jupyter notebooks for EDA and model training.
  - `EDA STUDENT PERFORMANCE.ipynb`: Notebook for Exploratory Data Analysis.
  - `MODEL TRAINING.ipynb`: Notebook for model training and evaluation.
- `data`: Directory containing raw data files.
  - `raw.csv`: Raw dataset file.
- `src`: Source code directory.
  - `app.py`: Flask application for serving predictions.
  - `main.py`: Main script for running the application.
  - `template.py`: Template script for additional utilities.
- `.dvcignore`: Specifies files and directories to be ignored by DVC.
- `Dockerfile`: Docker configuration file for containerizing the application.
- `README.md`: Project description and documentation (this file).
- `requirements.txt`: List of dependencies required for the project.
- `setup.py`: Setup script for installing the project as a package.




