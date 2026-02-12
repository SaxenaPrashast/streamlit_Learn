import streamlit as st
st.title("Hello World!")
st.subheader("Welcome to Streamlit")
st.text("This is a simple web application built with Streamlit.")
st.write("You can use Streamlit to create interactive web apps easily.")


language = st.selectbox("Choose a programming languages:", ["C++", "Java", "Python"])


st.write(f"You selected {language}. It's a flavorful blend of spices and tea.")
