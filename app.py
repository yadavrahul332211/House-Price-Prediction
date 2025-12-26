import streamlit as st
import pickle
import numpy as np

# Load trained model
model = pickle.load(open("model/house_price_model.pkl", "rb"))

st.title("🏠 House Price Prediction App")
st.write("Enter house area to predict price")

area = st.number_input("Area (in sq ft)", min_value=100)

if st.button("Predict Price"):
    input_data = np.array([[area]])
    prediction = model.predict(input_data)
    st.success(f"Predicted House Price: {prediction[0]:.2f}")
