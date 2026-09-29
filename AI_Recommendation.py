import streamlit as st

st.title("🤖 AI Fitness Recommendation")

steps = st.number_input("Daily Steps", min_value=0, value=5000)
exercise = st.number_input("Exercise Minutes", min_value=0, value=30)
water = st.number_input("Water Intake (litres)", min_value=0.0, value=2.0)

if st.button("Get AI Recommendation"):

    st.subheader("✨ Your Fitness Recommendation")

    if steps < 5000:
        st.write("🚶 Try to increase your daily walking gradually.")

    if exercise < 30:
        st.write("🏃 Add some regular physical activity to your routine.")

    if water < 2:
        st.write("💧 Make sure you drink enough fluids throughout the day.")

    if steps >= 5000 and exercise >= 30 and water >= 2:
        st.success("🎉 Good job! Keep maintaining your healthy routine.")