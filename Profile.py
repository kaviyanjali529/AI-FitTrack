import streamlit as st

st.title("👤 User Profile")

name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=100, value=18)
height = st.number_input("Height (cm)", min_value=50.0, max_value=250.0)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0)

gender = st.selectbox(
    "Gender",
    ["Select", "Male", "Female", "Other"]
)

if st.button("Save Profile"):
    if name and gender != "Select" and height > 0 and weight > 0:
        st.success("Profile saved successfully! ✅")
    else:
        st.warning("Please enter all details.")