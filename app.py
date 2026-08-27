import requests
import streamlit as st


try:
    APP_ID = st.secrets["WOLFRAM_APP_ID"]
except KeyError:
    st.error("⚠️ Error: APP_ID not found.")
    st.stop()

URL = "https://api.wolframalpha.com/v2/query"


st.set_page_config(
    page_title="My Math AI",
    page_icon="🧮",
    layout="centered"
)

st.markdown("""
<style>
/* Styling Header Card */
.header-container {
    text-align: center;
    padding: 2.5rem 1rem;
    background-color: rgba(150, 150, 150, 0.05);
    border-radius: 12px;
    margin-bottom: 2rem;
    border: 1px solid rgba(150, 150, 150, 0.2);
}
.main-title {
    font-size: 2.8rem;
    font-weight: 700;
    margin: 0;
    padding: 0;
}
.sub-title {
    font-size: 1.1rem;
    opacity: 0.7;
    margin-top: 0.5rem;
}

/* Styling Tombol Submit */
.stFormSubmitButton>button {
    width: 100%;
    background-color: #F26522;
    color: white;
    border-radius: 8px;
    border: none;
    font-size: 16px;
    font-weight: 600;
    padding: 10px;
    transition: all 0.3s ease;
}
.stFormSubmitButton>button:hover {
    background-color: #D9531E;
    box-shadow: 0 4px 12px rgba(242, 101, 34, 0.3);
    color: white;
}

/* === INPUT TEXT STYLING (Diperbesar) === */
.stTextInput input {
    border-radius: 8px;
    font-size: 20px !important; /* Ukuran font lebih besar */
    padding: 15px 20px !important; /* Kotak lebih tinggi dan luas */
}

/* Kotak Hasil (Result Box) */
.result-container {
    background-color: rgba(150, 150, 150, 0.05);
    padding: 2rem;
    border-radius: 12px;
    border: 1px solid rgba(150, 150, 150, 0.2);
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)


def solve_math(question):
    params = {
        "appid": APP_ID,
        "input": question,
        "output": "json"
    }

    try:
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan koneksi/API")
        return

    result = data.get("queryresult", {})

    if not result.get("success"):
        st.error("❌ Maaf, saya tidak dapat memahami pertanyaan tersebut.")
        return

    st.success("✅ Solusi berhasil ditemukan!")

    st.markdown("### 📖 Detail Penyelesaian")
    st.divider()

    for pod in result.get("pods", []):
        st.markdown(f"**📌 {pod['title']}**")
        
        for subpod in pod.get("subpods", []):
            if "img" in subpod:
                st.image(subpod["img"]["src"])
            elif subpod.get("plaintext"):
                st.write(subpod["plaintext"])
                
        st.write("") 



st.markdown("""
<div class="header-container">
    <h1 class="main-title">🧮 My Math AI</h1>
    <p class="sub-title">Powered by Wolfram Alpha</p>
</div>
""", unsafe_allow_html=True)

with st.form(key="math_form"):
    question = st.text_input(
        "Ketik persoalan matematika",
        placeholder="Contoh: Integrate x², Solve x²+5x+6=0"
    )
    submit_button = st.form_submit_button("🚀 Solve Now")

if submit_button:
    if question.strip():
        with st.spinner("🤖 Sedang menghitung..."):
            solve_math(question)
    else:
        st.warning("⚠️ Masukkan pertanyaan matematika.")