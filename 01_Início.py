import streamlit as st

pages = {
    "Início": [
        st.Page("Apresentação.py", title="Sobre mim"),
        st.Page("Curriculo.py", title="Thiago Medeiros"),
        st.Page("Contato.py", title="Contato"),
    ],
    "Projetos": [
        st.Page("Análise de Dados.py", title="Projeto de Análise"),
        st.Page("Portifolio", title="Outro projeto"),
    ],
}

pg = st.navigation(pages)
pg.run()
