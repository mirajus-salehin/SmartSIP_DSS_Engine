import streamlit as st
from sidebar import show_sidebar

from services.pv_selector import *

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
    page_title="Nearest Panels",
    layout="wide"
)

show_sidebar()


if "selected_location" not in st.session_state:

    st.warning(
        "Please select a location first."
    )

    st.stop()

lat, lon = st.session_state.selected_location


nearest = find_nearest_panels(
    lat,
    lon,
    n=10
)

quartiles = capacity_quartiles(
    nearest
)


st.title("Probable Panel Capacity")

stats = capacity_range(nearest)

st.write(f"Min capacity: {stats['min_capacity']:.2f}")

st.write(f"Max capacity: {stats['max_capacity']:.2f}")

st.write(f"Max Pump capacity: {stats['max_capacity'] / 2:.2f}")