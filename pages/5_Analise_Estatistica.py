
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats
from scipy.stats import t, norm, chi2_contingency
import warnings
warnings.filterwarnings("ignore")
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

# Função para carregar os dados 
@st.cache_data
def load_data():
    df = pd.read_csv(r"C:\Users\Predator\Downloads\dashboard\project_full\data\airlines_flights_data.csv")
    return df

df = load_data()

def statistical_analysis_page(df):
    """
    Aba dedicada à análise estatística com intervalos de confiança e testes de hipótese
    """
    st.header("📊 Análise Estatística Avançada")
    st.markdown("---")
    
    # Criar sub-abas
    subtab1, subtab2, subtab3, subtab4 = st.tabs([
        "🎯 Parâmetro Escolhido",
        "📏 Intervalos de Confiança", 
        "🧪 Testes de Hipótese",
        "📋 Resumo e Conclusões"
    ])
    
    with subtab1:
        st.subheader("1. Parâmetro Escolhido para Análise: PREÇO DOS VOOS")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("""
            ### 🎯 Justificativa da Escolha
            
            O **preço dos voos** foi escolhido como parâmetro principal de análise por ser:
            
            1. **Variável de interesse comercial:** O preço é o fator mais importante na decisão de compra
            2. **Variável contínua:** Permite aplicação de diversos testes estatísticos
            3. **Distribuição interessante:** Apresenta assimetria e variabilidade significativa
            4. **Relevância prática:** Insights sobre preços têm aplicação direta no mercado
            
            ### 🎯 Objetivos da Análise
            
            - Estimar o preço médio dos voos com intervalo de confiança
            - Testar se existe diferença significativa de preços entre companhias aéreas
            - Verificar se voos diretos são significativamente mais caros que voos com paradas
            - Analisar se a classe do voo impacta significativamente no preço
            """)
        
        with col2:
            # Estatísticas básicas do preço
            st.metric("Preço Médio", f"R$ {df['price'].mean():.2f}")
            st.metric("Preço Mediano", f"R$ {df['price'].median():.2f}")
            st.metric("Desvio Padrão", f"R$ {df['price'].std():.2f}")
            st.metric("Coef. Variação", f"{(df['price'].std()/df['price'].mean()*100):.1f}%")
        
        # Visualização da distribuição dos preços
        st.subheader("📊 Distribuição dos Preços")
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Histograma
            fig_hist = px.histogram(
                df, 
                x="price", 
                nbins=50,
                title="Distribuição dos Preços dos Voos",
                labels={"price": "Preço (R$)", "count": "Frequência"}
            )
            fig_hist.add_vline(x=df["price"].mean(), line_dash="dash", line_color="red", 
                              annotation_text=f"Média: R$ {df['price'].mean():.0f}")
            fig_hist.add_vline(x=df['price'].median(), line_dash="dash", line_color="green", 
                              annotation_text=f"Mediana: R$ {df['price'].median():.0f}")
            st.plotly_chart(fig_hist, use_container_width=True)
        
        with col2:
            # Box plot
            fig_box = px.box(
                df, 
                y="price",
                title="Box Plot dos Preços",
                labels={"price": "Preço (R$)"}
            )
            st.plotly_chart(fig_box, use_container_width=True)
    
    with subtab2:
        st.subheader("2. Intervalos de Confiança")
        
        # IC para a média geral dos preços
        st.markdown("### 📏 Intervalo de Confiança para a Média Geral dos Preços")
        
        n = len(df)
        mean_price = df["price"].mean()
        std_price = df["price"].std()
        se_price = std_price / np.sqrt(n)
        
        # IC 95% para a média
        confidence_level = st.slider("Nível de Confiança (%)", 90, 99, 95) / 100
        alpha = 1 - confidence_level
        z_critical = norm.ppf(1 - alpha/2)
        
        margin_error = z_critical * se_price
        ci_lower = mean_price - margin_error
        ci_upper = mean_price + margin_error
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Parâmetros da Análise:**")
            st.write(f"• Tamanho da amostra (n): {n:,}")
            st.write(f"• Média amostral: R$ {mean_price:.2f}")
            st.write(f"• Desvio padrão: R$ {std_price:.2f}")
            st.write(f"• Erro padrão: R$ {se_price:.2f}")
            st.write(f"• Valor crítico (Z): {z_critical:.3f}")
            st.write(f"• Margem de erro: R$ {margin_error:.2f}")
        
        with col2:
            st.success(f"""
            **Intervalo de Confiança {confidence_level*100:.0f}%:**
            
            [R$ {ci_lower:.2f}, R$ {ci_upper:.2f}]
            
            **Interpretação:**
            Com {confidence_level*100:.0f}% de confiança, o preço médio dos voos está entre R$ {ci_lower:.2f} e R$ {ci_upper:.2f}
            """)
        
        # Visualização do IC
        fig_ic = go.Figure()
        
        # Distribuição normal
        x = np.linspace(mean_price - 4*se_price, mean_price + 4*se_price, 1000)
        y = norm.pdf(x, mean_price, se_price)
        
        fig_ic.add_trace(go.Scatter(x=x, y=y, mode="lines", name="Distribuição da Média"))
        fig_ic.add_vline(x=ci_lower, line_dash="dash", line_color="red", annotation_text=f"IC Inferior: {ci_lower:.2f}")
        fig_ic.add_vline(x=ci_upper, line_dash="dash", line_color="red", annotation_text=f"IC Superior: {ci_upper:.2f}")
        fig_ic.add_vline(x=mean_price, line_color="blue", annotation_text=f"Média: {mean_price:.2f}")
        
        fig_ic.update_layout(
            title=f"Intervalo de Confiança {confidence_level*100:.0f}% para a Média dos Preços",
            xaxis_title="Preço (R$)",
            yaxis_title="Densidade"
        )
        
        st.plotly_chart(fig_ic, use_container_width=True)
        
        # IC para proporção de voos diretos
        st.markdown("### 📏 Intervalo de Confiança para Proporção de Voos Diretos")
        
        direct_flights = df[df["stops"] == "zero"]
        p_direct = len(direct_flights) / len(df)
        
        se_prop = np.sqrt(p_direct * (1 - p_direct) / n)
        margin_error_prop = z_critical * se_prop
        ci_prop_lower = p_direct - margin_error_prop
        ci_prop_upper = p_direct + margin_error_prop
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Parâmetros da Análise:**")
            st.write(f"• Total de voos: {n:,}")
            st.write(f"• Voos diretos: {len(direct_flights):,}")
            st.write(f"• Proporção amostral: {p_direct:.4f}")
            st.write(f"• Erro padrão: {se_prop:.4f}")
            st.write(f"• Margem de erro: {margin_error_prop:.4f}")
        
        with col2:
            st.info(f"""
            **Intervalo de Confiança {confidence_level*100:.0f}%:**
            
            [{ci_prop_lower:.4f}, {ci_prop_upper:.4f}]
            
            ou [{ci_prop_lower*100:.2f}%, {ci_prop_upper*100:.2f}%]
            
            **Interpretação:**
            Com {confidence_level*100:.0f}% de confiança, a proporção de voos diretos está entre {ci_prop_lower*100:.2f}% e {ci_prop_upper*100:.2f}%
            """)
    
    with subtab3:
        st.subheader("3. Testes de Hipótese")
        
        # Teste 1: ANOVA - Diferença entre companhias
        st.markdown("### 🧪 Teste 1: ANOVA - Diferença de Preços entre Companhias Aéreas")
        
        with st.expander("Ver detalhes do teste", expanded=True):
            st.write("""
            **Hipóteses:**
            - H₀: μ₁ = μ₂ = μ₃ = μ₄ = μ₅ = μ₆ (todas as companhias têm preço médio igual)
            - H₁: Pelo menos uma companhia tem preço médio diferente
            - Nível de significância: α = 0.05
            """)
            
            # Realizar ANOVA
            airlines = df["airline"].unique()
            price_groups = [df[df["airline"] == airline]["price"] for airline in airlines]
            f_stat, p_value_anova = stats.f_oneway(*price_groups)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Resultados do Teste:**")
                st.write(f"• Estatística F: {f_stat:.3f}")
                st.write(f"• Valor-p: {p_value_anova:.2e}")
                
                if p_value_anova < 0.05:
                    st.success("**Decisão:** Rejeitar H₀")
                    st.success("**Conclusão:** Existe diferença significativa entre os preços médios das companhias aéreas")
                else:
                    st.warning("**Decisão:** Não rejeitar H₀")
                    st.warning("**Conclusão:** Não há evidência de diferença significativa")
            
            with col2:
                # Estatísticas por companhia
                airline_stats = df.groupby("airline")["price"].agg(["count", "mean", "std"]).round(2)
                st.write("**Estatísticas por Companhia:**")
                st.dataframe(airline_stats)
        
        # Teste 2: Teste t - Voos diretos vs com paradas
        st.markdown("### 🧪 Teste 2: Teste t - Voos Diretos vs Voos com Paradas")
        
        with st.expander("Ver detalhes do teste", expanded=True):
            st.write("""
            **Hipóteses:**
            - H₀: μ_diretos = μ_com_paradas (preços médios são iguais)
            - H₁: μ_diretos ≠ μ_com_paradas (preços médios são diferentes)
            - Nível de significância: α = 0.05
            """)
            
            direct_prices = df[df["stops"] == "zero"]["price"]
            indirect_prices = df[df["stops"] != "zero"]["price"]
            
            # Teste de igualdade de variâncias
            levene_stat, levene_p = stats.levene(direct_prices, indirect_prices)
            equal_var = levene_p > 0.05
            
            # Teste t
            t_stat, p_value_t = stats.ttest_ind(direct_prices, indirect_prices, equal_var=equal_var)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Resultados do Teste:**")
                st.write(f"• Teste de Levene (variâncias): {levene_stat:.3f} (p = {levene_p:.3f})")
                st.write(f"• Variâncias iguais: {'Sim' if equal_var else 'Não'}")
                st.write(f"• Estatística t: {t_stat:.3f}")
                st.write(f"• Valor-p: {p_value_t:.2e}")
                
                if p_value_t < 0.05:
                    st.success("**Decisão:** Rejeitar H₀")
                    st.success("**Conclusão:** Existe diferença significativa entre preços de voos diretos e com paradas")
                else:
                    st.warning("**Decisão:** Não rejeitar H₀")
                    st.warning("**Conclusão:** Não há evidência de diferença significativa")
            
            with col2:
                st.write("**Estatísticas Descritivas:**")
                st.write(f"• **Voos diretos:**")
                st.write(f"  - Média: R$ {direct_prices.mean():.2f}")
                st.write(f"  - DP: R$ {direct_prices.std():.2f}")
                st.write(f"  - n: {len(direct_prices):,}")
                st.write(f"• **Voos com paradas:**")
                st.write(f"  - Média: R$ {indirect_prices.mean():.2f}")
                st.write(f"  - DP: R$ {indirect_prices.std():.2f}")
                st.write(f"  - n: {len(indirect_prices):,}")
        
        # Teste 3: Qui-quadrado - Classe vs Faixa de preço
        st.markdown("### 🧪 Teste 3: Qui-quadrado - Associação entre Classe e Faixa de Preço")
        
        with st.expander("Ver detalhes do teste", expanded=True):
            # Criar faixas de preço
            df_temp = df.copy()
            df_temp["price_range"] = pd.cut(df_temp["price"], 
                                          bins=[0, 5000, 15000, 50000, float("inf")], 
                                          labels=["Baixo", "Médio", "Alto", "Premium"])
            
            contingency_table = pd.crosstab(df_temp["class"], df_temp["price_range"])
            
            st.write("""
            **Hipóteses:**
            - H₀: Não há associação entre classe do voo e faixa de preço
            - H₁: Há associação entre classe do voo e faixa de preço
            - Nível de significância: α = 0.05
            """)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Tabela de Contingência:**")
                st.dataframe(contingency_table)
            
            with col2:
                # Teste qui-quadrado
                chi2_stat, p_value_chi2, dof, expected = chi2_contingency(contingency_table)
                
                st.write("**Resultados do Teste:**")
                st.write(f"• Estatística Qui-quadrado: {chi2_stat:.3f}")
                st.write(f"• Graus de liberdade: {dof}")
                st.write(f"• Valor-p: {p_value_chi2:.2e}")
                
                if p_value_chi2 < 0.05:
                    st.success("**Decisão:** Rejeitar H₀")
                    st.success("**Conclusão:** Existe associação significativa entre classe do voo e faixa de preço")
                else:
                    st.warning("**Decisão:** Não rejeitar H₀")
                    st.warning("**Conclusão:** Não há evidência de associação significativa")
        
        # Teste 4: Correlação
        st.markdown("### 🧪 Teste 4: Correlação - Duração vs Preço")
        
        with st.expander("Ver detalhes do teste", expanded=True):
            correlation_coef = df["duration"].corr(df["price"])
            n_corr = len(df)
            
            st.write("""
            **Hipóteses:**
            - H₀: ρ = 0 (não há correlação linear entre duração e preço)
            - H₁: ρ ≠ 0 (há correlação linear entre duração e preço)
            - Nível de significância: α = 0.05
            """)
            
            # Teste de significância da correlação
            t_corr = correlation_coef * np.sqrt((n_corr - 2) / (1 - correlation_coef**2))
            p_value_corr = 2 * (1 - stats.t.cdf(abs(t_corr), n_corr - 2))
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.write("**Resultados do Teste:**")
                st.write(f"• Coeficiente de correlação: {correlation_coef:.4f}")
                st.write(f"• Estatística t: {t_corr:.3f}")
                st.write(f"• Valor-p: {p_value_corr:.2e}")
                
                if p_value_corr < 0.05:
                    st.success("**Decisão:** Rejeitar H₀")
                    st.success("**Conclusão:** Existe correlação linear significativa")
                    if correlation_coef > 0:
                        st.info("A correlação é **POSITIVA**: quanto maior a duração, maior tende a ser o preço")
                    else:
                        st.info("A correlação é **NEGATIVA**: quanto maior a duração, menor tende a ser o preço")
                else:
                    st.warning("**Decisão:** Não rejeitar H₀")
                    st.warning("**Conclusão:** Não há evidência de correlação linear significativa")
            
            with col2:
                # Gráfico de dispersão
                fig_corr = px.scatter(
                    df.sample(1000), 
                    x="duration", 
                    y="price",
                    title=f"Correlação: Duração vs Preço (r = {correlation_coef:.4f})",
                    labels={"duration": "Duração (horas)", "price": "Preço (R$)"}
                )
                st.plotly_chart(fig_corr, use_container_width=True)
    
    with subtab4:
        st.subheader("4. Resumo dos Resultados e Interpretações")
        
        # Recalcular valores para o resumo
        n = len(df)
        mean_price = df["price"].mean()
        std_price = df["price"].std()
        se_price = std_price / np.sqrt(n)
        z_critical = norm.ppf(0.975)  # 95% IC
        margin_error = z_critical * se_price
        ci_lower = mean_price - margin_error
        ci_upper = mean_price + margin_error
        
        direct_flights = df[df["stops"] == "zero"]
        p_direct = len(direct_flights) / len(df)
        se_prop = np.sqrt(p_direct * (1 - p_direct) / n)
        margin_error_prop = z_critical * se_prop
        ci_prop_lower = p_direct - margin_error_prop
        ci_prop_upper = p_direct + margin_error_prop
        
        # ANOVA
        airlines = df["airline"].unique()
        price_groups = [df[df["airline"] == airline]["price"] for airline in airlines]
        f_stat, p_value_anova = stats.f_oneway(*price_groups)
        
        # Teste t
        direct_prices = df[df["stops"] == "zero"]["price"]
        indirect_prices = df[df["stops"] != "zero"]["price"]
        levene_stat, levene_p = stats.levene(direct_prices, indirect_prices)
        equal_var = levene_p > 0.05
        t_stat, p_value_t = stats.ttest_ind(direct_prices, indirect_prices, equal_var=equal_var)
        
        # Qui-quadrado
        df_temp = df.copy()
        df_temp["price_range"] = pd.cut(df_temp["price"], 
                                      bins=[0, 5000, 15000, 50000, float("inf")], 
                                      labels=["Baixo", "Médio", "Alto", "Premium"])
        contingency_table = pd.crosstab(df_temp["class"], df_temp["price_range"])
        chi2_stat, p_value_chi2, dof, expected = chi2_contingency(contingency_table)
        
        # Correlação
        correlation_coef = df["duration"].corr(df["price"])
        n_corr = len(df)
        t_corr = correlation_coef * np.sqrt((n_corr - 2) / (1 - correlation_coef**2))
        p_value_corr = 2 * (1 - stats.t.cdf(abs(t_corr), n_corr - 2))
        
        st.markdown("""
        A análise estatística avançada do preço dos voos revelou insights importantes:
        
        ### Intervalos de Confiança
        - **Preço Médio Geral:** Com 95% de confiança, o preço médio dos voos está entre R$ {ci_lower:.2f} e R$ {ci_upper:.2f}.
        - **Proporção de Voos Diretos:** A proporção de voos diretos está entre {ci_prop_lower*100:.2f}% e {ci_prop_upper*100:.2f}%.
        
        ### Testes de Hipótese
        - **ANOVA (Companhias Aéreas):** O valor-p ({p_value_anova:.2e}) foi menor que 0.05, indicando que **existe diferença significativa** nos preços médios entre as companhias aéreas. Isso sugere que a escolha da companhia aérea impacta o preço.
        - **Teste t (Voos Diretos vs. Paradas):** O valor-p ({p_value_t:.2e}) foi menor que 0.05, mostrando que **existe diferença significativa** entre os preços de voos diretos e voos com paradas. Geralmente, voos diretos tendem a ser mais caros, mas a análise detalhada é crucial.
        - **Qui-quadrado (Classe vs. Faixa de Preço):** O valor-p ({p_value_chi2:.2e}) foi menor que 0.05, confirmando que **existe associação significativa** entre a classe do voo e a faixa de preço. Classes superiores estão associadas a faixas de preço mais altas.
        - **Correlação (Duração vs. Preço):** O coeficiente de correlação foi de {correlation_coef:.4f} com um valor-p ({p_value_corr:.2e}) menor que 0.05. Isso indica uma **correlação linear significativa** entre duração e preço. A correlação é {'positiva' if correlation_coef > 0 else 'negativa'}, sugerindo que quanto maior a duração, {'maior' if correlation_coef > 0 else 'menor'} tende a ser o preço.
        
        ### Conclusões Finais
        Os resultados estatísticos fornecem uma base sólida para entender os fatores que influenciam o preço dos voos. A variabilidade entre companhias, o impacto das paradas e da classe, e a correlação com a duração são aspectos cruciais para a tomada de decisão de viajantes e para a otimização de estratégias de precificação por parte das companhias aéreas.
        """)

statistical_analysis_page(df)

if menu_choice == "Home":
    st.switch_page("Home.py")
elif menu_choice == "Certificados":
    st.switch_page("pages/2_Formacao_e_experiencia.py")
elif menu_choice == "Minhas Skills":
    st.switch_page("pages/3_Skills.py")
elif menu_choice == "Análise de Dados":
    st.switch_page("pages/4_Analise_de_dados.py")
