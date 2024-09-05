import streamlit as st
import plotly.express as px

# Exemplo de DataFrame
import pandas as pd
data = {'Categoria': ['A', 'B', 'C', 'D'], 
        'Valor': [10, 20, 15, 30]}
df = pd.DataFrame(data)

# Plotando o gráfico com Plotly Express
fig = px.bar(df, x='Categoria', y='Valor', color='Categoria')

# Exibindo o gráfico no Streamlit
st.plotly_chart(fig)
