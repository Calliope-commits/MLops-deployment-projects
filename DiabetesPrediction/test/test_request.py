import requests

# base URL of the api
url_base = 'https://diabeteprediction-975813296636.europe-west9.run.app'

# Ttest endpoint
response = requests.get(f"{url_base}/")
print("Response from the home endpoint:", response.text)
# example data for prediction
data_predict = {
    "Pregnancies": 2,
    "Glucose": 138,
    "BloodPressure": 62,
    "SkinThickness": 35,
    "Insulin": 0,
    "BMI": 33.6,
    "DiabetesPedigreeFunction": 0.127,
    "Age": 47
}



# Test the prediction endpoint
response = requests.post(f"{url_base}/predire", json=data_predict)  # Removed the trailing slash
print("Response from the prediction endpoint:", response.text)

# Example data for prediction with high probability of diabetes
data_predict_high_diabetes_risk = {
    "Pregnancies": 8,
    "Glucose": 180,
    "BloodPressure": 90,
    "SkinThickness": 40,
    "Insulin": 300,
    "BMI": 40.0,
    "DiabetesPedigreeFunction": 1.2,
    "Age": 60
}

# Test the prediction endpoint with high diabetes risk data
response = requests.post(f"{url_base}/predire", json=data_predict_high_diabetes_risk)
print("Response from the prediction endpoint with high diabetes risk data:", response.text)