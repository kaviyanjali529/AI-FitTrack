import streamlit as st


def authenticate_user(username, password):
    if username == "admin" and password == "1234":
        return True
    return False


def login_page():
    st.title("🔐 AI FIT TRACK Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate_user(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password")