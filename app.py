import streamlit as st
from sidebar import show_sidebar

st.set_page_config(
    page_title="SmartSIP DSS Engine",
    layout="wide"
)
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
show_sidebar()

st.title("Main Menu")