import joblib
import pandas as pd
# Load the model from the file
model = joblib.load('./model/random_forest_model.pkl')

# Load the diabetes dataset
diabetes = pd.read_csv("./model/data/diabetes.csv")

# Remove the 'Outcome' column
data_without_outcome = diabetes.drop('Outcome', axis=1)

# Make predictions with the loaded model
predictions = model.predict(data_without_outcome)

# Display the predictions
print(predictions)