import streamlit as st


st.markdown("""
<style>

/* Label */
.stTextInput label {
    font-size:18px;
    font-weight:600;
    color:#1f4e79;
}

/* Input box */
.stTextInput input {
    background-color:#f5f7fa;
    color:#222222;
    border:2px solid #4CAF50;
    border-radius:10px;
    padding:10px;
    font-size:16px;
}

/* Focus effect */
.stTextInput input:focus {
    border-color:#2196F3;
    box-shadow:0 0 8px rgba(33,150,243,0.5);
}

/* Placeholder text */
.stTextInput input::placeholder {
    color:#888888;
    font-style:italic;
}

</style>
""", unsafe_allow_html=True)
