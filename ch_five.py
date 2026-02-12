import streamlit as st
import requests 

st.title("Live currency exchange rates")
st.number_input("Enter the amount in INR", min_value=1.0, key="amount")
target_currency = st.selectbox("Convert to", ["USD", "EUR", "GBP"], key="currency")

if st.button("Convert"):
    amount = st.session_state.amount
    currency = st.session_state.currency
    url = f"https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][currency]
    converted_amount = amount * rate
    st.write(f"{amount} INR is equal to {converted_amount:.2f} {currency}")
