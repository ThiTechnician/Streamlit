import streamlit as st
import pandas as pd

pages = {
    "Início": [
        st.Page("Início.py", title="Apresentação"),
        st.Page("Apresentação.py", title="Sobre mim"),
        st.Page("Curriculo.py", title="Currículo"),
        st.Page("Contato.py", title="Contato"),
    ],
    "Projetos": [
        st.Page("Análise de Dados.py", title="Projeto de Análise"),
        st.Page("Portifolio.py", title="Dashboard Manutenção"),
        st.Page("monitor_clima.py", title="Monitor de Clima"),
        st.Page("conversor_moedas.py", title="Conversor de Moedas"),
    ],
}

pg = st.navigation(pages)
pg.run()
