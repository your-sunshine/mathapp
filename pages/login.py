import streamlit as st

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


email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if st.button("Create Account", use_container_width=True):
    if not email or not password or not confirm_password:
        st.error("Please fill in all fields.")
    elif password != confirm_password:
        st.error("Passwords do not match.")
    else:
        st.session_state.logged_in = True
        st.session_state.current_user = email
        st.success("Registration successful!")
