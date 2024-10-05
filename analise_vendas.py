import streamlit as st
import pandas as pd
import plotly.express as px

# Título da página
st.title("Análise de Dados de Vendas")

# Botão de download do template
st.download_button(
    label="Baixar planilha para preencher",
    data=csv,
    file_name="planilha_de_vendas.csv",
    mime="text/csv",
)

# Upload de arquivo CSV
uploaded_file = st.file_uploader("Carregar arquivo de dados de vendas (CSV)", type=["csv"])

if uploaded_file is not None:
    try:
        # Tentar ler o arquivo CSV com codificação ISO-8859-1
        df = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
    except UnicodeDecodeError:
        st.error("Erro ao ler o arquivo. Tente usar um arquivo com codificação UTF-8 ou ISO-8859-1.")

    # Exibir os dados carregados
    st.write("Visualização dos dados de vendas:")
    st.dataframe(df.head())

    # Converter a coluna de datas
    df['Data'] = pd.to_datetime(df['Data'])

    # Adicionar opção "Todos" nos filtros
    produtos_unicos = df['Produto'].unique().tolist()
    produtos_unicos.insert(0, "Todos")
    
    regioes_unicas = df['Região'].unique().tolist()
    regioes_unicas.insert(0, "Todos")

    # Filtros interativos com "Todos" como uma opção
    produto_selecionado = st.selectbox("Selecione o produto", produtos_unicos)
    regiao_selecionada = st.selectbox("Selecione a região", regioes_unicas)
    data_inicio = st.date_input("Data inicial", df['Data'].min())
    data_fim = st.date_input("Data final", df['Data'].max())

    # Filtrar dados com base nos filtros selecionados, ignorando "Todos" quando selecionado
    df_filtrado = df.copy()
    
    if produto_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado['Produto'] == produto_selecionado]
    
    if regiao_selecionada != "Todos":
        df_filtrado = df_filtrado[df_filtrado['Região'] == regiao_selecionada]

    df_filtrado = df_filtrado[(df['Data'] >= pd.to_datetime(data_inicio)) & 
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
