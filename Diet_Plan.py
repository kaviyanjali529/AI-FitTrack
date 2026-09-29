import streamlit as st

st.title("🍎 Diet Plan")

goal = st.selectbox(
    "Select your fitness goal",
    [
        "Select",
        "Weight Management",
        "Muscle Building",
        "General Fitness"
    ]
)

if st.button("Get Diet Suggestions"):

    if goal == "Weight Management":
        st.subheader("🥗 Suggested Foods")
        st.write("• Vegetables and fruits")
        st.write("• Whole grains")
        st.write("• Protein-rich foods")
        st.write("• Adequate water")

    elif goal == "Muscle Building":
        st.subheader("💪 Suggested Foods")
        st.write("• Protein-rich foods")
        st.write("• Eggs / pulses")
        st.write("• Whole grains")
        st.write("• Fruits and vegetables")

    elif goal == "General Fitness":
        st.subheader("🌱 Suggested Foods")
        st.write("• Balanced meals")
        st.write("• Fruits and vegetables")
        st.write("• Whole grains")
        st.write("• Adequate water")

    else:
        st.warning("Please select a fitness goal.")