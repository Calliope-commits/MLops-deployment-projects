# Creation of the API with Flask
from pydantic import BaseModel  # Used for data validation, encapsulates the features
import numpy as np
import pandas as pd  # Used for data manipulation
import joblib  # Used to load the saved model
from flask import Flask, request, jsonify  # Flask for the API

# Load the random forest model from disk
model = joblib.load('random_forest_model.pkl')

# Definition of the input data schema with Pydantic
# This ensures that the received data matches the model's expectations
class InputData(BaseModel):
    Pregnancies: float  # Number of pregnancies
    Glucose: float  # Plasma glucose concentration at 2 hours in an oral glucose tolerance test
    BloodPressure: float  # Diastolic blood pressure (mm Hg)
    SkinThickness: float  # Triceps skinfold thickness (mm)
    Insulin: float  # Serum insulin over 2 hours (mu U/ml)
    BMI: float  # Body mass index (weight in kg/(height in m)^2)
    DiabetesPedigreeFunction: float  # Diabetes pedigree function
    Age: float  # Age (years)

# Create the Flask application instance
app = Flask(__name__)

# Define the root route that returns a welcome message
@app.route("/", methods=["GET"])
def home():
    """ Root endpoint that provides a welcome message. """
    return jsonify({"message": "Welcome to the diabetes diagnosis prediction API"})

# Define the route for diabetes predictions
@app.route("/predire", methods=["POST"])
def predict():
    """
    Endpoint for predictions using the loaded model.
    The input data is validated and transformed into a DataFrame for processing by the model.
    """
    if not request.json:
        return jsonify({"error": "No JSON provided"}), 400
    
    try:
        # Extracting and validating input data using Pydantic
        data = InputData(**request.json)
        data_df = pd.DataFrame([data.dict()])  # Convert to DataFrame

        # Use the model to predict and obtain probabilities
        predictions = model.predict(data_df)
        probabilities = model.predict_proba(data_df)[:, 1]  # Probability of the positive class (diabetes)

        # Compile results into a dictionary
        results = data.dict()
        results['prediction'] = int(predictions[0])
        results['diabetes_probability'] = probabilities[0]

        # Return results as JSON
        return jsonify({"results": results})
    except Exception as e:
        # Error handling and return an error response
        return jsonify({"error": str(e)}), 400

# Entry point to run the application
if __name__ == "__main__":
    app.run(debug=True, port=8000)  # Launch the application on port 8000 with debug mode enabled
