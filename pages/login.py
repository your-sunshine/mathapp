import streamlit as st
import time

st.set_page_config(
    page_title="Login - My Math App",
    page_icon="🔐",
    layout="centered"
)

if st.session_state.logged_in:
    st.switch_page("pages/math-app.py")

st.title("🧮 My Math App")
st.write("Please login to access the feature!")
st.divider()

with st.form("login"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    submitted = st.form_submit_button("Create Account")
    
    if submitted:
        if not (name and email and password and confirm_password) :
            st.error("Please fill all fields")
        elif password != confirm_password:
            st.error("Password and confirm password must be same")
        else:
            st.session_state.logged_in = True
            st.session_state.current_user = name
            st.success("Registration successful!")
            time.sleep(5)
            st.switch_page("pages/math-app.py")
