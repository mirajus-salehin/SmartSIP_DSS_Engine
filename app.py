import streamlit as st
from sidebar import show_sidebar
from ui.styles import load_styles
from streamlit_folium import st_folium
import folium


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
load_styles()

st.title("Main Menu")



if "selected_location" not in st.session_state:

    # Default location (Dhaka)
    st.session_state.selected_location = [23.8103, 90.4125]


left_col, right_col = st.columns([1, 2])


with left_col:

    st.subheader("User Information")

    name = st.text_input(
        "Name",
        placeholder="Enter your name"
    )

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120,
        step=1
    )

    occupation = st.text_input(
        "Occupation",
        placeholder="Enter occupation"
    )
    
    crops_options = ['Paddy', 'Potato', 'Chilli', 'Brinjal',"Wheat", "Jute", "Sugarcane", "Tobacco"]
    crop_selected_options = st.multiselect('Choose your preferred crops:', crops_options)
    
    sip_options = ["Cold storage", "BAU STR Dryer", "BAU Hybrid dryer", "Thresher", "EV charging", "Huller", "Water purifier"]
    sip_selected_options = st.multiselect('Choose you prefered SIP+ sysems', sip_options)

    st.divider()

    lat, lon = st.session_state.selected_location

    st.write(f"**Latitude:** {lat:.6f}")

    st.write(f"**Longitude:** {lon:.6f}")

with right_col:

    # Create map centered at selected location
    st.subheader("Select your location")
    m = folium.Map(
        location=st.session_state.selected_location,
        zoom_start=8,
        height="50%"
    )

    # Add marker
    folium.Marker(
        st.session_state.selected_location,
        tooltip="Selected Location"
    ).add_to(m)

    # Display map
    map_data = st_folium(
        m,
        width=None,
        height=550,
        key="map"
    )


clicked = map_data.get("last_clicked")

if clicked:

    new_location = [
        clicked["lat"],
        clicked["lng"]
    ]

    # Update only if location changed
    if new_location != st.session_state.selected_location:

        st.session_state.selected_location = new_location