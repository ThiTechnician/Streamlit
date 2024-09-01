import streamlit as st

pages = {
    "Início": [
        st.Page("Apresentação.py", title="Sobre mim"),
        st.Page("Apresentação.py", title="Sobre mim"),
        st.Page("Curriculo.py", title="Currículo"),
        st.Page("Contato.py", title="Contato"),
    ],
    "Projetos": [
        st.Page("Análise de Dados.py", title="Projeto de Análise"),
        st.Page("Portifolio.py", title="Outro projeto"),
    ],
}

pg = st.navigation(pages)
pg.run()
