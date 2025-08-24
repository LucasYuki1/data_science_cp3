import streamlit as st
from streamlit_option_menu import option_menu

def sidebar_menu():
    with st.sidebar:
        st.image("assets/logo.png", use_container_width=True)  # logo no topo
        
        selected = option_menu(
            menu_title=None,
            options=["Home", "Certificados", "Minhas Skills", "Análise de Dados", "Dashboard"],
            icons=["house", "award", "bar-chart", "graph-up", "grid"],
            default_index=0,
            styles={
                "container": {"padding": "5px", "background-color": "#0e1117"},
                "icon": {"color": "red", "font-size": "22px"}, 
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin":"5px",
                    "--hover-color": "#262730",
                },
                "nav-link-selected": {"background-color": "#ff0000"},
            }
        )
    return selected
