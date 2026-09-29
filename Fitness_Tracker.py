import streamlit as st

st.title("🏃 Fitness Tracker")

steps = st.number_input("Daily Steps", min_value=0, value=5000)
exercise = st.number_input("Exercise Duration (minutes)", min_value=0, value=30)
water = st.number_input("Water Intake (litres)", min_value=0.0, max_value=10.0, value=2.0)

if st.button("Save Activity"):
    st.success("Today's fitness activity saved! ✅")

st.divider()

st.subheader("Today's Activity")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Steps", steps)

with col2:
    st.metric("Exercise", f"{exercise} min")

with col3:
    st.metric("Water", f"{water} L")