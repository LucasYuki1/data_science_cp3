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

def skills_page():
    st.title("🛠️ Habilidades e Competências")
    st.markdown("---")
    
    # Seção de Habilidades Técnicas
    st.header("💻 Habilidades Técnicas")
    
    # Linguagens de Programação
    st.subheader("🐍 Hard Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**Git/Github** - Avançado")
        st.progress(0.95)
        st.write("**Python** - Avançado")
        st.progress(0.9)
        st.write("**Blender** - Avançado")
        st.progress(0.85)
        st.write("**Java** - Avançado")
        st.progress(0.8)
        st.write("**Docker** - Intermediário")
        st.progress(0.75)
        st.write("**Linux** - Intermediário")
        st.progress(0.7)
        
        
    with col2:
        st.write("**Shell script** - Intermediário")
        st.progress(0.7)
        st.write("**Pacote Office** - Intermediário")
        st.progress(0.7)
        st.write("**JavaScript** - Intermediário")
        st.progress(0.6)
        st.write("**C++** - Intermediário")
        st.progress(0.55)
        st.write("**SQL** - Básico")
        st.progress(0.4)
        st.write("**Terraform** - Básico")
        st.progress(0.3)
    
    st.markdown("---")
    
    # Ferramentas e Tecnologias
    st.subheader("🔧 Ferramentas e Tecnologias")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Bancos de Dados:**")
        st.write("• MySQL")
        st.write("• PostgreSQL")
        st.write("• MongoDB")
    
    with col2:
        st.write("**Cloud Computing:**")
        st.write("• AWS (S3, EC2, RDS)")
        st.write("• Docker")
    
    with col3:
        st.write("**Monitoramento e gráficos:**")
        st.write("• Fiware")
        st.write("• Prometheus")
        st.write("• Grafana")
    
    st.markdown("---")
    
    # Soft Skills
    st.header("🧠 Soft Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🎯 Competências Analíticas")
        st.write("• **Pensamento Crítico** - Capacidade de questionar dados e resultados")
        st.write("• **Resolução de Problemas** - Abordagem estruturada para desafios complexos")
    
    with col2:
        st.subheader("🤝 Competências Interpessoais")
        st.write("• **Leitura e análise de perfis** - Capaz de analisar pessoas para extrair potencial e criar um ambiente seguro")
        st.write("• **Colaboração** - Trabalho eficiente em equipes")
        st.write("• **Adaptabilidade** - Flexibilidade para aprender novas tecnologias")
    
    st.markdown("---")
    
    # Metodologias e Práticas
    st.header("⚙️ Metodologias e Práticas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🛠️ Engenharia e Arquitetura de Sistemas")
        st.write("• **Design Modular** – Estruturação de código para escalabilidade e manutenção")
        st.write("• **Integração de Sistemas** – APIs, MQTT, FIWARE, e arquiteturas distribuídas")
        st.write("• **Otimização de Performance** – Foco em baixo nível e eficiência de execução")
        st.write("• **Boas Práticas de Engenharia** – Clean Code, SOLID, e padrões de projeto")

    with col2:
        st.subheader("⚙️ Desenvolvimento e Operações")
        st.write("• **Controle de Versão** – Git/GitHub com fluxos profissionais de branch")
        st.write("• **Metodologias Ágeis** – Scrum/Kanban aplicados a projetos técnicos")
        st.write("• **DevOps & Cloud** – Docker, CI/CD, e automação de deploys")
        st.write("• **Documentação Técnica** – README e guias claros para onboarding rápido")

    
    st.markdown("---")
    
    # Idiomas
    st.header("🌍 Idiomas")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("**Português**")
        st.write("Nativo")
        st.progress(1.0)
    
    with col2:
        st.write("**Inglês**")
        st.write("Avançado")
        st.progress(0.75)
    
    with col3:
        st.write("**Japonês**")
        st.write("Básico")
        st.progress(0.4)

skills_page()

if menu_choice == "Home":
    st.switch_page("Home.py")
elif menu_choice == "Certificados":
    st.switch_page("pages/2_Formacao_e_experiencia.py")
elif menu_choice == "Análise de Dados":
    st.switch_page("pages/4_Analise_de_dados.py")
elif menu_choice == "Dashboard":
    st.switch_page("pages/5_Analise_Estatistica.py")
