
import streamlit as st
from PIL import Image, ImageOps
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

def home_page():
    st.title("Bem-vindo(a) ao Meu Perfil Profissional!")
    st.markdown("---")
    
    # Seção de introdução pessoal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Sobre Mim")
        st.write("""
        Olá! Sou um estudante de engenharia de software apaixonado por **DevOps** e **IoT**, 
        atualmente estudando para ser capaz de criar pipelines completos de deploy em nuvem.
        
        Tenho sólida formação em pilares de DevOps, tais como conhecimento em linux,
        CI/CD, IaC, cloud e IoT com arduino e esp32.
        """)
        
        st.subheader("🎯 Objetivo Profissional")
        st.write("""
        Busco oportunidades desafiadoras na área de **DevOps** e **Infraestrutura**, contribuindo 
        com soluções inovadoras e baseadas em dados para impulsionar o crescimento e a eficiência 
        de negócios. Meu foco está em:
        
        - Desenvolvimento de pipelines completos para automatização
        - Criação de dashboards interativos e visualizações impactantes
        - Implementação de soluções escaláveis e automatizadas
        """)
    
    with col2:
        img = Image.open(r"assets/perfil.jpg")
        img = ImageOps.exif_transpose(img)
        st.image(img, use_container_width=True)
    
    st.markdown("---")
    
    # Seção de destaques
    st.header("🌟 Destaques")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Semestre em engenharia de software",
            value="4º",
            delta="Aprendizado constante"
        )
    
    with col2:
        st.metric(
            label="Projetos concluídos e em andamento",
            value="8",
            delta="Domínio em estruturas diversas"
        )
    
    with col3:
        st.metric(
            label="Tecnologias aprendidas",
            value="10+",
            delta="Comunicação entre ferramentas"
        )
    
    st.markdown("---")
    
    # Seção de contato
    st.header("📞 Contato")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("📧 **Email:**  lucasenzoideyuki@gmail.com")
    
    with col2:
        st.write("💼 **LinkedIn:** [Lucas Yuki](https://www.linkedin.com/in/lucas-henzo-ide-yuki/)")
    
    with col3:
        st.write("🐙 **GitHub:** [LucasYuki1](https://github.com/LucasYuki1)")

home_page()

# Conteúdo dinâmico conforme o menu
if menu_choice == "Certificados":
    st.switch_page("pages/2_Formacao_e_experiencia.py")
elif menu_choice == "Minhas Skills":
    st.switch_page("pages/3_Skills.py")
elif menu_choice == "Análise de Dados":
    st.switch_page("pages/4_Analise_de_dados.py")
elif menu_choice == "Dashboard":
    st.switch_page("pages/5_Analise_Estatistica.py")
