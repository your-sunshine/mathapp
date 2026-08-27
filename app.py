import streamlit as st

st.set_page_config(
    page_title="My Math App",
    page_icon="🧮",
    layout="centered"
)

if not st.session_state.logged_in:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    st.switch_page("pages/app.py")
else:
    st.switch_page("pages/login.py")