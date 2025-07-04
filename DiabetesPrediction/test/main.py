import streamlit as st
import pandas as pd
import requests

# API URL
URL_BASE = 'https://diabete-975813296636.europe-west8.run.app'
#URL_BASE = '127.0.0.1:8000'



def send_for_prediction(data):
    """ Sends the data to the API and retrieves predictions. """
    response = requests.post(f"{URL_BASE}/predict", json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def main():
    st.set_page_config(page_title="Diabetes Prediction App", page_icon="🧬")

    st.title("Diabetes Prediction Application")
    st.write("Please upload a CSV file containing patient data.")

    # File upload by the user
    file = st.file_uploader("Choose a CSV file", type='csv')
    if file is not None:
        # Load the data
        data = pd.read_csv(file)           

        # Display the loaded data
        st.write("Loaded data:")
        st.write(data)

        if st.button("Predict"):
            # Predict each row of the loaded data
            predictions = []
            for _, row in data.iterrows():
                api_data = row.to_dict()
                result = send_for_prediction(api_data)
                if result:
                    predictions.append({'prediction': result['results'], 'diabetes_probability': result.get('probability', 'N/A')})
                else:
                    predictions.append({'prediction': 'Error', 'diabetes_probability': 'N/A'})

            # Display the results
            st.write("Predictions:")
            st.table(predictions)
        else:
            st.write("Click the 'Predict' button to get the results.")

if __name__ == "__main__":
    main()
