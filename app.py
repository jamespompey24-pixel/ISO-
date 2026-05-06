import streamlit as st
import pickle
import numpy as np

# Title of the app
st.title('david John')

# Load the saved model (this assumes model.pkl is in the same folder)
try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Error: 'model.pkl' not found. Pease ensure the model file is in this project folder.")
    st.stop() # Stop the execution of the app

# Create sliders for user input
st.subheader("Adjust Features:")
BuyingPrice = st.slider("Select Buying Price (10 = highest)", 0, 10, 5)
Maintenance = st.slider("Select Maintenance Level (10 = highest)", 0, 10, 5)
Doors = st.slider("Select Number of Doors (10 = highest)", 0, 10, 5)
Persons = st.slider("Select Persons (10 = highest)", 0, 10, 5)
Luggage = st.slider("Select Luggage Boot Size (10 = highest)", 0, 10, 5)
Safety = st.slider("Select Safety Level (10 = highest)", 0, 10, 5)

# Optional: Add icons or labels
st.write("---")

# Prediction button
if st.button("Predict Car Acceptability"):
    # Reshape input for the model
    features = np.array([[BuyingPrice, Maintenance, Doors, Persons, Luggage, Safety]])
    prediction = model.predict(features)
    
    # Optional: If your model output is 0/1, map it to labels
    # acceptability = "Acceptable" if prediction[0] == 1 else "Unacceptable"
    
    st.header(f"The model predicts: {prediction[0]}")