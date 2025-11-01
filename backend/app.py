import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("modal_price_model.pkl")

st.title("🌾 Agricultural Market Price Prediction App ")

st.write("Enter market details to predict the **Modal Price**")

State = st.text_input("State")
District = st.text_input("District")
Market = st.text_input("Market")
Commodity = st.text_input("Commodity")
Variety = st.text_input("Variety")
Grade = st.text_input("Grade")

Min_price = st.number_input("Minimum Price", min_value=0)
Max_price = st.number_input("Maximum Price", min_value=0)

day = st.number_input("Day", min_value=1, max_value=31)
month = st.number_input("Month", min_value=1, max_value=12)
year = st.number_input("Year", min_value=2000, max_value=2050)

price_spread = Max_price - Min_price

input_data = pd.DataFrame([{
    "Min_x0020_Price": Min_price,
    "Max_x0020_Price": Max_price,
    "price_spread": price_spread,
    "day": day, "month": month, "year": year,
    "State": State, "District": District, "Market": Market,
    "Commodity": Commodity, "Variety": Variety, "Grade": Grade
}])

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"💰 Predicted Modal Price: **₹ {prediction:.2f}**")
