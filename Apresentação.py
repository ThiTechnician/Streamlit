import streamlit as st
import pandas as pd

# Exemplo de dados para o gráfico
data = {
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [23, 45, 12, 36]
}
df = pd.DataFrame(data)

# Configuração das colunas
col1, col2 = st.columns(2)

st.markdown("""
## Sobre Mim
""", unsafe_allow_html=True)

# Exibindo o gráfico na coluna col1 usando o st.bar_chart
with col1:
    st.bar_chart(df.set_index('Categoria'))


with col2:
    st.markdown("""
    <p style="text-align: justify;">
    Com mais de uma década de experiência na área de tecnologia gráfica, tenho me dedicado a expandir e aprimorar meu conhecimento em Ciência de Dados. Sou formado em Engenharia de Produção e possuo uma pós-graduação em Ciência de Dados, além de uma sólida experiência em programação com Python.
    </p>
    """, unsafe_allow_html=True)

st.markdown("""
<p style="text-align: justify;">
Minha jornada inclui o desenvolvimento de aplicativos e soluções para análise e visualização de dados, utilizando ferramentas como Streamlit e Plotly, além de trabalhar com SQL e MySQL para manipulação e análise de grandes volumes de dados.
</p>

<p style="text-align: justify;">
Recentemente, tenho me concentrado na criação de dashboards interativos e geração de relatórios em PDF para clientes, integrando gráficos avançados e insights valiosos. Também sou familiarizado com o uso de bibliotecas como Pandas para manipulação de dados e ferramentas de autenticação como Streamlit Authenticator para garantir a segurança e personalização do acesso em aplicativos web.
</p>

<p style="text-align: justify;">
Possuo habilidades em linguagens adicionais como C, HTML e CSS, e estou habituado ao uso do Git para versionamento e colaboração em projetos. Estou constantemente em busca de novas oportunidades para aplicar e expandir meu conhecimento em Ciência de Dados, aproveitando minhas habilidades técnicas e conhecimentos adquiridos ao longo da graduação e da experiência prática.
</p>
""", unsafe_allow_html=True)
