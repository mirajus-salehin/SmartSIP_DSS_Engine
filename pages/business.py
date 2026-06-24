import streamlit as st
from sidebar import show_sidebar


st.markdown(
    """
    <style>
    div[data-testid="stSidebarNav"] {
        display: none !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(
    page_title="Business Model",
    layout="wide"
)

show_sidebar()

st.title("Bussiness Model")