import streamlit as st

pages = {
    "Início": [
        st.Page("Apresentação.py", title="Sobre mim"),
        st.Page("Currículo.py", title="Thiago Medeiros"),
    ],
    "Projetos": [
        st.Page("Análise de Dados.py", title="Projeto de Análise"),
        st.Page("Portifolio", title="Outro projeto"),
    ],
}

