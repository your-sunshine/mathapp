import streamlit as st

st.set_page_config(
    page_title="My Math App",
    page_icon="🧮",
    layout="centered"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.switch_page("pages/math-app.py")
else:
    st.switch_page("pages/login.py")
