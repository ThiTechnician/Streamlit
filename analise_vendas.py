import streamlit as st
import pandas as pd
import plotly.express as px

# Título da página
st.title("Análise de Dados de Vendas")

# Upload de arquivo CSV
uploaded_file = st.file_uploader("Carregar arquivo de dados de vendas (CSV)", type=["csv"])

if uploaded_file is not None:
    # Ler o arquivo CSV
    df = pd.read_csv(uploaded_file)

    # Exibir os dados carregados
    st.write("Visualização dos dados de vendas:")
    st.dataframe(df.head())

    # Converter a coluna de datas
    df['Data'] = pd.to_datetime(df['Data'])

    # Filtros interativos
    produto_selecionado = st.selectbox("Selecione o produto", df['Produto'].unique())
    regiao_selecionada = st.selectbox("Selecione a região", df['Região'].unique())
    data_inicio = st.date_input("Data inicial", df['Data'].min())
    data_fim = st.date_input("Data final", df['Data'].max())

    # Filtrar dados com base nos filtros selecionados
    df_filtrado = df[(df['Produto'] == produto_selecionado) & 
                     (df['Região'] == regiao_selecionada) & 
                     (df['Data'] >= pd.to_datetime(data_inicio)) & 
                     (df['Data'] <= pd.to_datetime(data_fim))]

    # Exibir métricas
    receita_total = df_filtrado['Receita'].sum()
    quantidade_total = df_filtrado['Quantidade'].sum()
    st.metric("Receita Total", f"R${receita_total:,.2f}")
    st.metric("Quantidade Total Vendida", quantidade_total)

    # Gráficos interativos
    st.subheader("Gráficos de Vendas")

    # Gráfico de barras - Receita por produto
    fig_produto = px.bar(df_filtrado, x='Produto', y='Receita', color='Produto', title="Receita por Produto")
    st.plotly_chart(fig_produto)

    # Gráfico de linha - Receita ao longo do tempo
    fig_tempo = px.line(df_filtrado, x='Data', y='Receita', title="Receita ao Longo do Tempo")
    st.plotly_chart(fig_tempo)

    # Gráfico de pizza - Receita por região
    fig_regiao = px.pie(df_filtrado, names='Região', values='Receita', title="Receita por Região")
    st.plotly_chart(fig_regiao)

else:
    st.write("Por favor, carregue um arquivo CSV para análise.")
