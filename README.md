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

## Files Description

- `.dvc`: DVC (Data Version Control) configuration files for data tracking.
- `artifacts`: Directory containing generated artifacts.
  - `model.pkl`: Trained model file.
  - `preprocessor.pkl`: Preprocessing pipeline file.
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `mlruns/0`: Directory containing MLflow experiment runs.
- `meta.yaml`: Metadata for the MLflow experiment.
- `notebook`: Directory containing Jupyter notebooks for EDA and model training.
  - `EDA STUDENT PERFORMANCE.ipynb`: Notebook for Exploratory Data Analysis.
  - `MODEL TRAINING.ipynb`: Notebook for model training and evaluation.
- `data`: Directory containing raw data files.
  - `raw.csv`: Raw dataset file.
- `src/MLProject`: Source code directory.
  - `components`: Contains modules for data ingestion, transformation, and model training.
  - `pipelines`: Contains prediction pipelines
  - `exception.py`: Custom exception handling.
  - `logger.py`: Logging configuration.
  - `utils.py`: Utility functions.
- `templates`: Directory containing HTML templates for the Flask application.
  - `home.html`: Template for displaying prediction results.
  - `index.html`: Template for inputting data for prediction.
- `.dvcignore`: Specifies files and directories to be ignored by DVC.
- `README.md`: Project description and documentation (this file).
- `requirements.txt`: List of dependencies required for the project.
- `setup.py`: Setup script for installing the project as a package.
- `app.py`: Flask application for serving predictions.
- `main.py`: Main script for running the application.
- `template.py`: Template script for additional utilities.

## HTML Files

### `index.html`
This file contains the form for inputting student data for prediction. It includes fields for gender, race/ethnicity, parental level of education, lunch type, test preparation course, reading score, and writing score.

### `home.html`
This file displays the prediction results after the form in `index.html` is submitted.

## How to Run

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Student-Performance-Analysis

2. **Create a virtual environment and activate it**:
  ```python -m venv venv
  source venv/Scripts/activate  # On Windows
  source venv/bin/activate      # On Unix or MacOS

3. **Install the dependencies**:
  ```pip install -r requirements.txt

4. **Run the Flask application**:
  ```python app.py

5. **Access the application**:
  Open your web browser and go to http://127.0.0.1:5000/ to access the home page. Fill out the form to get predictions for the math score based on the input data.


## MLflow and DagsHub
This project also uses MLflow to track experiments and log model parameters, metrics, and artifacts. The experiment runs are logged in the mlruns directory.

To visualize and manage the experiments, the project is integrated with DagsHub, which provides a user-friendly interface for tracking ML experiments.

### Running MLflow Tracking
You can run the MLflow tracking server using the following command:
```mlflow ui
