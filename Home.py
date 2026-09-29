import streamlit as st

st.set_page_config(
    page_title="AI FIT TRACK",
    page_icon="🏃",
    layout="wide"
)

st.title("🏃 AI FIT TRACK")
st.subheader("AI Based Fitness Tracking System")

st.write("Welcome to AI FIT TRACK! 🎉")

st.divider()

# Create Pages
profile_page = st.Page(
    "fitness_pages/Profile.py",
    title="User Profile",
    icon="👤"
)

bmi_page = st.Page(
    "fitness_pages/BMI_Calculator.py",
    title="BMI Calculator",
    icon="⚖️"
)

tracker_page = st.Page(
    "fitness_pages/Fitness_Tracker.py",
    title="Fitness Tracker",
    icon="🏃"
)

diet_page = st.Page(
    "fitness_pages/Diet_Plan.py",
    title="Diet Plan",
    icon="🍎"
)

progress_page = st.Page(
    "fitness_pages/Progress.py",
    title="Progress",
    icon="📊"
)

ai_page = st.Page(
    "fitness_pages/AI_Recommendation.py",
    title="AI Recommendation",
    icon="🤖"
)

# Navigation
pg = st.navigation(
    [
        profile_page,
        bmi_page,
        tracker_page,
        diet_page,
        progress_page,
        ai_page
    ]
)

pg.run()