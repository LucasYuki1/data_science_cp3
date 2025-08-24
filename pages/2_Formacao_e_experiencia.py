import streamlit as st
from sidebar import sidebar_menu

# Oculta o menu padrão do Streamlit multipage
st.set_page_config(page_title="Meu Portfólio", layout="wide", initial_sidebar_state="expanded")

hide_streamlit_style = """
    <style>
    /* Esconde o menu padrão das multipages */
    .css-1d391kg, .css-h5rgaw, [data-testid="stSidebarNav"] {
        display: none;
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

menu_choice = sidebar_menu()

if menu_choice == "Home":
    st.switch_page("Home.py")
elif menu_choice == "Minhas Skills":
    st.switch_page("pages/3_Skills.py")
elif menu_choice == "Análise de Dados":
    st.switch_page("pages/4_Analise_de_dados.py")
elif menu_choice == "Dashboard":
    st.switch_page("pages/5_Analise_Estatistica.py")

def education_experience_page():
    st.title("🎓 Formação e Experiência")
    st.markdown("---")
    
    # Seção de Formação Acadêmica
    st.header("🎓 Formação Acadêmica")
    
    with st.expander("**Bacharelado em Engenharia de Software (em andamento)** - FIAP (2024 - 2028)", expanded=True):
        st.write("""
        **Principais disciplinas:**
        - Data Science
        - Algoritmos e Estruturas de Dados
        - Banco de Dados
        - Desenvolvimento Web
        - Análise de Sistemas
        - IoT
        
        **Projeto de Iniciação científica:** Sistema integrado em capacete para auxiliar motoqueiros e previnir acidentes (em andamento) (2025)

        """)
    
    st.markdown("---")

    # Seção de Certificações
    st.header("🏆 Certificados e Competências")

    st.subheader("Cursos Complementares")
    st.write("📚 **DevOps** - Alura (2025)")
    st.write("📚 **Blender 3D Modeling** - Alura/Youtube/Udemy (2025)")
    st.write("📚 **Game Design** - FIAP (2025)")
    st.write("📚 **Java DDD** - FIAP (2024)")

    st.markdown("---")

education_experience_page()
