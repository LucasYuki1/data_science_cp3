import streamlit as st
from streamlit_option_menu import option_menu

def sidebar_menu():
    # garante que o menu não volte pro "Home" a cada reload
    if "menu_choice" not in st.session_state:
        st.session_state.menu_choice = "Home"

    with st.sidebar:
        st.image(r"assets/logo.png", use_container_width=True)

        selected = option_menu(
            menu_title=None,
            options=["Home", "Certificados", "Minhas Skills", "Análise de Dados", "Dashboard"],
            icons=["house", "award", "bar-chart", "graph-up", "grid"],
            default_index=[
                "Home", "Certificados", "Minhas Skills", "Análise de Dados", "Dashboard"
            ].index(st.session_state.menu_choice),
            styles={
                "container": {"padding": "5px", "background-color": "#0e1117"},
                "icon": {"color": "red", "font-size": "22px"},
                "nav-link": {
                    "font-size": "16px",
                    "margin": "5px",
                    "--hover-color": "#262730",
                },
                "nav-link-selected": {"background-color": "#ff0000"},
            }
        )

    st.session_state.menu_choice = selected
    return selected
