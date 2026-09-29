import streamlit as st

st.title("⚖️ BMI Calculator")

weight = st.number_input("Weight (kg)", min_value=1.0)
height = st.number_input("Height (cm)", min_value=50.0)

if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.metric("Your BMI", f"{bmi:.2f}")

    if bmi < 18.5:
        st.info("BMI Category: Underweight")
    elif bmi < 25:
        st.success("BMI Category: Normal")
    elif bmi < 30:
        st.warning("BMI Category: Overweight")
    else:
        st.error("BMI Category: Obesity")