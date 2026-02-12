import streamlit as st

st.title("Chai maker App")
if st.button("Make Chai"):
    st.success("Chai is being made...")

st.checkbox("Add sugar")
st.checkbox("Add milk")


st.radio("Select tea type", ("Green Tea", "Black Tea", "Masala Tea"))
st.selectbox("Select tea flavor", ("Cardamom", "Ginger", "Lemon"))
st.slider("Select tea strength", 1, 5, 3)

st.number_input("Enter tea quantity (in cups)", min_value=1, max_value=10, value=1)

st.text_area("Additional instructions", "E.g., less sugar, more milk...")

st.text_input("Your name")