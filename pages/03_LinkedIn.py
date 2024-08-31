import streamlit as st

# URL da página web que você deseja exibir
url = "https://www.linkedin.com/in/engenheirothiagomedeiros"

# Exibe a página web dentro de um iframe
st.components.v1.iframe(url, width=800, height=600, scrolling=True)