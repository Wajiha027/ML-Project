import sys
import os
from flask import Flask, request, render_template
import pandas as pd
from src.MLProject.exception import CustomException
from src.MLProject.utils import load_object
from src.MLProject.pipelines.prediction_pipeline import PredictPipeline, CustomData

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_datapoint():
    try:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course', 'none'),  # Set default if None
            reading_score=int(request.form.get('reading_score')),
            writing_score=int(request.form.get('writing_score'))
        )
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results)
    
    except Exception as e:
        raise CustomException(e, sys)

if __name__ == "__main__":
    app.run(debug=True)
