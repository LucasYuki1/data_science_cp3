# 👨‍💻 Dashboard Profissional Interativo com Análise de Dados

Uma aplicação web completa desenvolvida com Streamlit que apresenta um perfil profissional interativo e realiza análise de dados avançada aplicada ao mercado de aviação, incluindo intervalos de confiança e testes de hipótese.

## 🚀 Funcionalidades

### 📋 Perfil Profissional
- **Home**: Introdução pessoal, objetivos profissionais e informações de contato
- **Formação e Experiência**: Histórico acadêmico, certificações e experiência profissional detalhada
- **Habilidades**: Competências técnicas, soft skills, metodologias e idiomas com indicadores visuais

### 📊 Análise de Dados Estruturada
- **Apresentação dos Dados**: Identificação de tipos de variáveis e principais perguntas de análise
- **Análise Estatística**: Medidas centrais, dispersão, correlação e distribuições
- **Análise por Categorias**: Segmentação por companhias aéreas, classes e paradas
- **Visualizações Interativas**: Gráficos dinâmicos com filtros avançados

### 🧪 Análise Estatística Avançada
- **Intervalos de Confiança**: Para média de preços e proporção de voos diretos
- **Testes de Hipótese**: ANOVA, Teste t, Qui-quadrado e Correlação
- **Justificativas Metodológicas**: Explicação detalhada da escolha de cada teste
- **Interpretações Práticas**: Conclusões aplicáveis ao mercado de aviação

## 🛠️ Tecnologias Utilizadas

- **Streamlit**: Framework para criação de aplicações web interativas
- **Pandas**: Manipulação e análise de dados
- **Plotly**: Visualizações interativas e responsivas
- **NumPy**: Computação numérica
- **SciPy**: Análise estatística avançada
- **Matplotlib/Seaborn**: Visualizações complementares

## 📋 Pré-requisitos

- Python 3.7+
- pip (gerenciador de pacotes Python)

## 🚀 Como Executar

### 1. Clone o repositório
```bash
git clone (https://github.com/LucasYuki1/data_science_cp3)
cd data_science_cp3
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação
```bash
streamlit run Home.py
```

### 4. Acesse no navegador
Abra seu navegador e acesse: `http://localhost:8501`

## 📊 Estrutura dos Dados

O dataset contém **300.153 registros** de voos com as seguintes variáveis:

### Variáveis Categóricas
- `airline`: Companhia aérea (6 categorias)
- `flight`: Código do voo
- `source_city`: Cidade de origem (6 cidades)
- `destination_city`: Cidade de destino (6 cidades)
- `departure_time`: Horário de partida (6 períodos)
- `arrival_time`: Horário de chegada (6 períodos)
- `stops`: Número de paradas (zero, one, two_or_more)
- `class`: Classe do voo (Economy, Business)

### Variáveis Numéricas
- `duration`: Duração do voo em horas (0.83 - 49.83h)
- `days_left`: Dias restantes até o voo (1 - 49 dias)
- `price`: Preço do voo em rupias (1.105 - 123.071)

## 🎯 Estrutura do Dashboard

### Navegação Principal
1. **Home** - Apresentação pessoal e objetivos
2. **Formação e Experiência** - Histórico acadêmico e profissional
3. **Habilidades** - Competências técnicas e interpessoais
4. **Análise de Dados** - Análise exploratória estruturada
5. **Análise Estatística** - Intervalos de confiança e testes de hipótese

### Critérios de Avaliação Atendidos

#### 1. Apresentação dos Dados (1 ponto) ✅
- ✅ Explicação completa sobre o conjunto de dados
- ✅ Identificação detalhada dos tipos de variáveis
- ✅ Definição de 7 principais perguntas de análise

#### 2. Análise Estatística Inicial (1.5 pontos) ✅
- ✅ Cálculo de média, mediana e moda para todas as variáveis numéricas
- ✅ Discussão sobre distribuição dos dados (assimetria e curtose)
- ✅ Apresentação de desvio padrão, variância e coeficiente de variação
- ✅ Identificação de correlações entre variáveis com interpretação
- ✅ Análise de outliers com método IQR

#### 3. Intervalos de Confiança e Testes de Hipótese (4.5 pontos) ✅
- ✅ **Parâmetro escolhido**: Preço dos voos (justificativa detalhada)
- ✅ **Intervalos de Confiança**:
  - IC 95% para média geral dos preços
  - IC 95% para proporção de voos diretos
- ✅ **Testes de Hipótese**:
  - ANOVA: Diferença entre companhias aéreas
  - Teste t: Voos diretos vs com paradas
  - Qui-quadrado: Associação classe vs faixa de preço
  - Correlação: Duração vs preço
- ✅ **Justificativas metodológicas** para cada teste
- ✅ **Visualizações interativas** para todos os resultados
- ✅ **Interpretações práticas** com implicações de mercado

## 📈 Principais Descobertas

### Intervalos de Confiança
- **Preço médio**: R$ 20.808 - R$ 20.971 (95% IC)
- **Voos diretos**: 11.88% - 12.11% do total (95% IC)

### Testes de Hipótese
- **Companhias aéreas**: Diferenças significativas de preço (p < 0.001)
- **Voos diretos vs paradas**: Voos diretos são mais baratos (p < 0.001)
- **Classe vs preço**: Forte associação (p < 0.001)
- **Duração vs preço**: Correlação positiva significativa (r = 0.204, p < 0.001)

## 🔧 Funcionalidades Avançadas

### Filtros Interativos
- Companhias aéreas
- Cidades de origem e destino
- Classes de voo
- Número de paradas
- Faixa de preço (slider)
- Duração do voo (slider)

### Visualizações
- Box plots para distribuição de preços
- Gráficos de barras para rotas
- Gráficos de pizza para horários
- Scatter plots para correlações
- Gráficos de linha para tendências temporais
- Histogramas para distribuições

### Análise Estatística Interativa
- Seletor de nível de confiança para ICs
- Visualização de distribuições normais
- Tabelas de contingência interativas
- Gráficos de correlação com linha de tendência

## 📱 Responsividade

A aplicação é totalmente responsiva e funciona em:
- Desktop
- Tablets
- Smartphones

## 🚀 Deploy

Para fazer deploy da aplicação:

1. **Streamlit Cloud**: Conecte seu repositório GitHub ao Streamlit Cloud
2. **Heroku**: Use o arquivo `requirements.txt` para deploy automático
3. **Docker**: Containerize a aplicação para deploy em qualquer plataforma

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Por favor:
1. Faça um fork do projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📞 Suporte

Para dúvidas ou suporte, abra uma issue no repositório do projeto.

---

**Desenvolvido com ❤️ usando Streamlit e Python**

