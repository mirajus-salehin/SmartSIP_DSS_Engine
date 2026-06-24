import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.image("./assets/LOGO_smart_sip.png", width=120)
        

        st.markdown(
            """
            <h2 style='text-align:center'>
            SmartSIP DSS Engine
            </h2>
            """,
            unsafe_allow_html=True
        )

        st.divider()

        st.page_link(
            "app.py",
            label="Main Menu"
        )

        st.page_link(
            "pages/solar.py",
            label="Solar Output"
        )
        st.page_link(
            "pages/irrigation.py",
            label="Irrigation Calculation"
        )
        st.page_link(
            "pages/climate.py",
            label="Climate data"
        )
        st.page_link(
            "pages/business.py",
            label="Business Model"
        )