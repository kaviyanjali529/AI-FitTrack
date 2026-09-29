import streamlit as st

st.title("📊 Fitness Progress")

st.subheader("Weekly Progress")

steps = st.number_input(
    "Average Daily Steps",
    min_value=0,
    value=5000
)

exercise = st.number_input(
    "Weekly Exercise (minutes)",
    min_value=0,
    value=150
)

water = st.number_input(
    "Average Daily Water (litres)",
    min_value=0.0,
    max_value=10.0,
    value=2.0
)

if st.button("View Progress"):

    st.success("Progress updated successfully! ✅")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Daily Steps", steps)

    with col2:
        st.metric("Exercise", f"{exercise} min/week")

    with col3:
        st.metric("Water", f"{water} L/day")