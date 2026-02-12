import streamlit as st
st.title("Chai taste poll")

col1, col2 = st.columns(2)
with col1:
    st.header("Which chai do you like?")
    chai_options = ["Masala Chai", "Ginger Chai", "Cardamom Chai", "Plain Chai"]
    selected_chai = st.selectbox("Select your favorite chai:", chai_options)    
    st.write(f"You selected: {selected_chai}")
with col2:
    st.header("How do you like your chai?")
    sweetness_levels = ["Less Sweet", "Medium Sweet", "Very Sweet"]
    selected_sweetness = st.selectbox("Select your preferred sweetness level:", sweetness_levels)
    st.write(f"You prefer: {selected_sweetness} chai")

st.sidebar.header("Additional Preferences")
milk_options = ["Whole Milk", "Skim Milk", "Almond Milk", "Oat Milk"]
selected_milk = st.sidebar.selectbox("Select your preferred milk type:", milk_options)
st.sidebar.write(f"You prefer: {selected_milk} in your chai")  


with st.expander("See the poll results"):
    st.write("Here are the results of the chai taste poll:")
    st.write(f"Favorite Chai: {selected_chai}")
    st.write(f"Preferred Sweetness: {selected_sweetness}")
    st.write(f"Preferred Milk Type: {selected_milk}")