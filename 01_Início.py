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
        st.Page("Portifolio.py", title="Dashboard Manutenção"),
        st.Page("monitor_clima.py", title="Monitor de Clima"),
        st.Page("conversor_moedas.py", title="Conversor de Moedas"),
        st.Page("analise_vendas.py", title="Análise de Vendas"),
    ],
}

pg = st.navigation(pages)
pg.run()
