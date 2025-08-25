import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy import stats
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

@st.cache_data
def load_data():
    df = pd.read_csv(r"data/airlines_flights_data.csv")
    return df

def data_analysis_page(df):
    st.title("📊 Análise de Dados de Voos")
    st.markdown("---")
    
    # Criar abas dentro da análise de dados
    tab1, tab2, tab3, tab4 = st.tabs([
        "📋 Apresentação dos Dados", 
        "📈 Análise Estatística", 
        "🔍 Análise por Categorias",
        "📊 Visualizações Interativas"
    ])
    
    with tab1:
        st.header("1. Apresentação dos Dados e Tipos de Variáveis")
        
        # Informações gerais do dataset
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total de Registros", f"{len(df):,}")
        with col2:
            st.metric("Número de Variáveis", df.shape[1])
        with col3:
            st.metric("Período de Análise", f"{df['days_left'].min()} a {df['days_left'].max()} dias")
        
        st.markdown("---")
        
        # Explicação sobre o conjunto de dados
        st.subheader("📖 Sobre o Conjunto de Dados")
        st.write("""
        Este dataset contém informações detalhadas sobre **300.153 voos** de companhias aéreas indianas, 
        incluindo dados sobre preços, duração, rotas, classes e antecedência de compra. 
        
        **Fonte dos dados:** Dados de voos coletados de múltiplas companhias aéreas indianas
        **Período:** Voos com antecedência de 1 a 49 dias
        **Escopo geográfico:** Principais cidades da Índia (Delhi, Mumbai, Bangalore, Kolkata, Hyderabad, Chennai)
        """)
        
        # Identificação dos tipos de variáveis
        st.subheader("🔍 Identificação dos Tipos de Variáveis")
        
        # Criar DataFrame com informações das variáveis
        var_info = []
        for col in df.columns:
            dtype = df[col].dtype
            unique_count = df[col].nunique()
            
            if dtype == 'object':
                var_type = "Categórica Nominal"
                if col in ['departure_time', 'arrival_time']:
                    var_type = "Categórica Ordinal"
            elif dtype in ['int64', 'float64']:
                if unique_count < 10:
                    var_type = "Numérica Discreta"
                else:
                    var_type = "Numérica Contínua"
            else:
                var_type = "Outro"
            
            var_info.append({
                'Variável': col,
                'Tipo': var_type,
                'Tipo de Dados': str(dtype),
                'Valores Únicos': unique_count,
                'Valores Ausentes': df[col].isnull().sum()
            })
        
        var_df = pd.DataFrame(var_info)
        st.dataframe(var_df, use_container_width=True)
        
        # Principais perguntas de análise
        st.subheader("❓ Principais Perguntas de Análise")
        st.write("""
        Com base na estrutura dos dados, as principais perguntas que podem ser respondidas são:
        
        1. **Qual companhia aérea oferece os melhores preços?**
        2. **Como o preço varia com a antecedência da compra?**
        3. **Voos diretos são mais caros que voos com paradas?**
        4. **Qual é o melhor horário para viajar considerando preço e duração?**
        5. **Como a classe do voo impacta no preço?**
        6. **Existe diferença significativa de preços entre as rotas?**
        7. **Qual é a distribuição de preços e como ela se comporta?**
        """)
    
    with tab2:
        st.header("2. Medidas Centrais, Dispersão e Correlação")
        
        # Análise das variáveis numéricas
        numeric_cols = ['duration', 'days_left', 'price']
        
        st.subheader("📊 Estatísticas Descritivas")
        st.dataframe(df[numeric_cols].describe(), use_container_width=True)
        
        # Medidas de tendência central
        st.subheader("📍 Medidas de Tendência Central")
        
        for col in numeric_cols:
            with st.expander(f"Análise de {col.upper()}", expanded=False):
                col1, col2 = st.columns(2)
                
                with col1:
                    mean_val = df[col].mean()
                    median_val = df[col].median()
                    mode_val = df[col].mode().iloc[0] if len(df[col].mode()) > 0 else "N/A"
                    
                    st.write(f"**Média:** {mean_val:.2f}")
                    st.write(f"**Mediana:** {median_val:.2f}")
                    st.write(f"**Moda:** {mode_val}")
                
                with col2:
                    # Análise da distribuição
                    skewness = stats.skew(df[col])
                    kurtosis = stats.kurtosis(df[col])
                    
                    st.write(f"**Assimetria:** {skewness:.3f}")
                    if skewness > 0.5:
                        st.write("→ Distribuição assimétrica à direita")
                    elif skewness < -0.5:
                        st.write("→ Distribuição assimétrica à esquerda")
                    else:
                        st.write("→ Distribuição aproximadamente simétrica")
                    
                    st.write(f"**Curtose:** {kurtosis:.3f}")
                    if kurtosis > 0:
                        st.write("→ Mais pontiaguda que a normal")
                    else:
                        st.write("→ Mais achatada que a normal")
        
        # Medidas de dispersão
        st.subheader("📏 Medidas de Dispersão")
        
        disp_data = []
        for col in numeric_cols:
            std_val = df[col].std()
            var_val = df[col].var()
            cv = (std_val / df[col].mean()) * 100
            
            disp_data.append({
                'Variável': col,
                'Desvio Padrão': f"{std_val:.2f}",
                'Variância': f"{var_val:.2f}",
                'Coef. Variação (%)': f"{cv:.2f}%",
                'Interpretação': "Alta variabilidade" if cv > 30 else "Variabilidade moderada" if cv > 15 else "Baixa variabilidade"
            })
        
        disp_df = pd.DataFrame(disp_data)
        st.dataframe(disp_df, use_container_width=True)
        
        # Matriz de correlação
        st.subheader("🔗 Matriz de Correlação")
        
        col1, col2 = st.columns([1, 1])
        
        with col1:
            correlation_matrix = df[numeric_cols].corr()
            st.dataframe(correlation_matrix.round(3), use_container_width=True)
        
        with col2:
            st.write("**Interpretação das Correlações:**")
            for i in range(len(numeric_cols)):
                for j in range(i+1, len(numeric_cols)):
                    corr_val = correlation_matrix.iloc[i, j]
                    var1, var2 = numeric_cols[i], numeric_cols[j]
                    
                    if abs(corr_val) > 0.7:
                        strength = "forte"
                    elif abs(corr_val) > 0.3:
                        strength = "moderada"
                    else:
                        strength = "fraca"
                    
                    direction = "positiva" if corr_val > 0 else "negativa"
                    st.write(f"• **{var1} vs {var2}:** {corr_val:.3f} - Correlação {strength} {direction}")
    
    with tab3:
        st.header("3. Análise por Categorias")
        
        # Análise por companhia aérea
        st.subheader("✈️ Análise por Companhia Aérea")
        airline_stats = df.groupby('airline').agg({
            'price': ['mean', 'median', 'std', 'count'],
            'duration': ['mean', 'median'],
            'days_left': 'mean'
        }).round(2)
        
        airline_stats.columns = ['Preço Médio', 'Preço Mediano', 'Preço DP', 'Qtd Voos', 
                                'Duração Média', 'Duração Mediana', 'Dias Antecedência']
        st.dataframe(airline_stats, use_container_width=True)
        
        # Análise por classe
        st.subheader("🎫 Análise por Classe")
        class_stats = df.groupby('class').agg({
            'price': ['mean', 'median', 'std', 'count'],
            'duration': ['mean', 'median']
        }).round(2)
        
        class_stats.columns = ['Preço Médio', 'Preço Mediano', 'Preço DP', 'Qtd Voos', 
                              'Duração Média', 'Duração Mediana']
        st.dataframe(class_stats, use_container_width=True)
        
        # Análise por número de paradas
        st.subheader("🛑 Análise por Número de Paradas")
        stops_stats = df.groupby('stops').agg({
            'price': ['mean', 'median', 'std', 'count'],
            'duration': ['mean', 'median']
        }).round(2)
        
        stops_stats.columns = ['Preço Médio', 'Preço Mediano', 'Preço DP', 'Qtd Voos', 
                              'Duração Média', 'Duração Mediana']
        st.dataframe(stops_stats, use_container_width=True)
        
        # Identificação de outliers
        st.subheader("🎯 Identificação de Outliers")
        
        outlier_data = []
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            outlier_percentage = (len(outliers) / len(df)) * 100
            
            outlier_data.append({
                'Variável': col,
                'Q1': f"{Q1:.2f}",
                'Q3': f"{Q3:.2f}",
                'IQR': f"{IQR:.2f}",
                'Limite Inferior': f"{lower_bound:.2f}",
                'Limite Superior': f"{upper_bound:.2f}",
                'Outliers': len(outliers),
                'Percentual': f"{outlier_percentage:.2f}%"
            })
        
        outlier_df = pd.DataFrame(outlier_data)
        st.dataframe(outlier_df, use_container_width=True)
    
    with tab4:
        st.header("4. Visualizações Interativas")
        
        # Sidebar para filtros (mantido do projeto original)
        st.sidebar.header("🔍 Filtros")

        # Filtro por companhia aérea
        airlines = st.sidebar.multiselect(
            "Selecione as Companhias Aéreas:",
            options=df['airline'].unique(),
            default=df['airline'].unique()
        )

        # Filtro por cidade de origem
        source_cities = st.sidebar.multiselect(
            "Selecione as Cidades de Origem:",
            options=df['source_city'].unique(),
            default=df['source_city'].unique()
        )

        # Filtro por cidade de destino
        destination_cities = st.sidebar.multiselect(
            "Selecione as Cidades de Destino:",
            options=df['destination_city'].unique(),
            default=df['destination_city'].unique()
        )

        # Filtro por classe
        classes = st.sidebar.multiselect(
            "Selecione as Classes:",
            options=df['class'].unique(),
            default=df['class'].unique()
        )

        # Filtro por número de paradas
        stops = st.sidebar.multiselect(
            "Selecione o Número de Paradas:",
            options=df['stops'].unique(),
            default=df['stops'].unique()
        )

        # Filtro por faixa de preço
        price_range = st.sidebar.slider(
            "Faixa de Preço:",
            min_value=int(df['price'].min()),
            max_value=int(df['price'].max()),
            value=(int(df['price'].min()), int(df['price'].max()))
        )

        # Filtro por duração do voo
        duration_range = st.sidebar.slider(
            "Duração do Voo (horas):",
            min_value=float(df['duration'].min()),
            max_value=float(df['duration'].max()),
            value=(float(df['duration'].min()), float(df['duration'].max()))
        )

        # Aplicar filtros
        filtered_df = df[
            (df['airline'].isin(airlines)) &
            (df['source_city'].isin(source_cities)) &
            (df['destination_city'].isin(destination_cities)) &
            (df['class'].isin(classes)) &
            (df['stops'].isin(stops)) &
            (df['price'] >= price_range[0]) &
            (df['price'] <= price_range[1]) &
            (df['duration'] >= duration_range[0]) &
            (df['duration'] <= duration_range[1])
        ]

        # Exibir métricas principais
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total de Voos", len(filtered_df))
        with col2:
            st.metric("Preço Médio", f"R$ {filtered_df['price'].mean():.2f}")
        with col3:
            st.metric("Duração Média", f"{filtered_df['duration'].mean():.2f}h")
        with col4:
            st.metric("Companhias Aéreas", filtered_df['airline'].nunique())
        st.markdown("---")

        # Gráficos (mantidos do projeto original)
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📊 Distribuição de Preços por Companhia Aérea")
            fig_price = px.box(
                filtered_df, 
                x='airline', 
                y='price',
                title="Distribuição de Preços por Companhia Aérea",
                color='airline'
            )
            fig_price.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_price, use_container_width=True)

        with col2:
            st.subheader("⏱️ Duração Média por Rota")
            route_duration = filtered_df.groupby(['source_city', 'destination_city'])['duration'].mean().reset_index()
            route_duration['route'] = route_duration['source_city'] + ' → ' + route_duration['destination_city']
            
            fig_duration = px.bar(
                route_duration.head(10), 
                x='route', 
                y='duration',
                title="Top 10 Rotas por Duração Média",
                color='duration',
                color_continuous_scale='viridis'
            )
            fig_duration.update_layout(xaxis_tickangle=-45)
            st.plotly_chart(fig_duration, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("🕐 Voos por Horário de Partida")
            departure_counts = filtered_df['departure_time'].value_counts()
            
            fig_departure = px.pie(
                values=departure_counts.values,
                names=departure_counts.index,
                title="Distribuição de Voos por Horário de Partida"
            )
            st.plotly_chart(fig_departure, use_container_width=True)

        with col2:
            st.subheader("💰 Relação Preço vs Duração")
            fig_scatter = px.scatter(
                filtered_df.sample(min(1000, len(filtered_df))), 
                x='duration', 
                y='price',
                color='airline',
                size='days_left',
                title="Relação entre Preço e Duração do Voo",
                hover_data=['source_city', 'destination_city']
            )
            st.plotly_chart(fig_scatter, use_container_width=True)

        col1, col2 = st.columns(2)
        with col1:
            st.subheader("📈 Preço Médio por Dias Restantes")
            price_by_days = filtered_df.groupby('days_left')['price'].mean().reset_index()
            
            fig_days = px.line(
                price_by_days, 
                x='days_left', 
                y='price',
                title="Variação do Preço Médio por Dias Restantes para o Voo",
                markers=True
            )
            st.plotly_chart(fig_days, use_container_width=True)

        with col2:
            st.subheader("🛑 Análise de Paradas")
            stops_analysis = filtered_df.groupby('stops').agg({
                'price': 'mean',
                'duration': 'mean',
                'flight': 'count'
            }).reset_index()
            stops_analysis.columns = ['stops', 'preço_médio', 'duração_média', 'quantidade_voos']
            
            fig_stops = make_subplots(
                rows=1, cols=2,
                subplot_titles=('Preço Médio por Paradas', 'Duração Média por Paradas'),
                specs=[[{'secondary_y': False}, {'secondary_y': False}]]
            )
            
            fig_stops.add_trace(
                go.Bar(x=stops_analysis['stops'], y=stops_analysis['preço_médio'], name='Preço Médio'),
                row=1, col=1
            )
            
            fig_stops.add_trace(
                go.Bar(x=stops_analysis['stops'], y=stops_analysis['duração_média'], name='Duração Média'),
                row=1, col=2
            )
            
            fig_stops.update_layout(showlegend=False)
            st.plotly_chart(fig_stops, use_container_width=True)

        st.subheader("🗺️ Mapa de Rotas")

        st.markdown("---")
        st.subheader("🔍 Insights dos Dados")

        insights_col1, insights_col2 = st.columns(2)
        with insights_col1:
            st.markdown("### 📊 Estatísticas Gerais")
            most_expensive_airline = filtered_df.groupby('airline')['price'].mean().idxmax()
            most_expensive_price = filtered_df.groupby('airline')['price'].mean().max()
            most_popular_route = filtered_df.groupby(['source_city', 'destination_city']).size().idxmax()
            st.write(f"**Companhia aérea mais cara:** {most_expensive_airline} (R$ {most_expensive_price:.2f})")
            st.write(f"**Rota mais popular:** {most_popular_route[0]} → {most_popular_route[1]}")
            best_time = filtered_df.groupby('departure_time')['price'].mean().idxmin()
            best_price = filtered_df.groupby('departure_time')['price'].mean().min()
            st.write(f"**Melhor horário (menor preço):** {best_time} (R$ {best_price:.2f})")

        with insights_col2:
            st.markdown("### 💡 Recomendações")
            correlation = filtered_df['days_left'].corr(filtered_df['price'])
            if correlation > 0.1:
                st.write("📈 **Compre com antecedência:** Preços tendem a aumentar próximo à data do voo")
            elif correlation < -0.1:
                st.write("📉 **Compre próximo à data:** Preços tendem a diminuir próximo à data do voo")
            else:
                st.write("📊 **Preços estáveis:** Não há correlação forte entre antecedência e preço")
            
            zero_stops_avg = filtered_df[filtered_df['stops'] == 'zero']['price'].mean()
            one_stop_avg = filtered_df[filtered_df['stops'] == 'one']['price'].mean() if 'one' in filtered_df['stops'].values else 0
            
            if zero_stops_avg < one_stop_avg:
                st.write("✈️ **Voos diretos são mais baratos** em média")
            else:
                st.write("🔄 **Voos com paradas podem ser mais econômicos**")

        # Tabela de dados filtrados (mantida do projeto original)
        st.markdown("---")
        st.subheader("📋 Dados Filtrados")
        st.dataframe(filtered_df.head(100), use_container_width=True)

        # Opção para download dos dados filtrados (mantida do projeto original)
        csv = filtered_df.to_csv(index=False)
        st.download_button(
            label="📥 Baixar dados filtrados (CSV)",
            data=csv,
            file_name='dados_voos_filtrados.csv',
            mime='text/csv'
        )

df = load_data()
data_analysis_page(df)

if menu_choice == "Home":
    st.switch_page("Home.py")
elif menu_choice == "Certificados":
    st.switch_page("pages/2_Formacao_e_experiencia.py")
elif menu_choice == "Minhas Skills":
    st.switch_page("pages/3_Skills.py")
elif menu_choice == "Dashboard":
    st.switch_page("pages/5_Analise_Estatistica.py")
       
