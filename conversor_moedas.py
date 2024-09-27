import streamlit as st
import requests
import plotly.express as px
import pandas as pd
from datetime import datetime, timedelta

# Configurar a chave da API de câmbio
API_KEY = '8477f10e083fb0df2da6950b'

# Função para obter a taxa de câmbio atual
def get_exchange_rate(base_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{base_currency}/{target_currency}"
    response = requests.get(url)
    data = response.json()
    return data

# Função para obter o histórico da taxa de câmbio
def get_exchange_history(base_currency, target_currency, date):
    year = date.year
    month = date.month
    day = date.day
    url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/history/{base_currency}/{year}/{month}/{day}"
    response = requests.get(url)
    data = response.json()
    return data

# Título da aplicação
st.title("Conversor de Moedas em Tempo Real")

# Entrada do valor a ser convertido
amount = st.number_input("Digite o valor a ser convertido", min_value=0.0, format="%.2f")

# Seleção das moedas
base_currency = st.selectbox("Moeda de Origem", ["USD", "EUR", "BRL", "JPY", "GBP"])
target_currency = st.selectbox("Moeda de Destino", ["USD", "EUR", "BRL", "JPY", "GBP"])

# Botão para realizar a conversão
if st.button("Converter"):
    if amount > 0:
        rate_data = get_exchange_rate(base_currency, target_currency)
        if rate_data["result"] == "success":
            conversion_rate = rate_data["conversion_rate"]
            converted_value = amount * conversion_rate
            st.write(f"**{amount} {base_currency}** é equivalente a **{converted_value:.2f} {target_currency}**.")
            st.session_state.converted = True
        else:
            st.error("Erro ao obter a taxa de câmbio.")
    else:
        st.warning("Por favor, insira um valor maior que 0.")

# Exibir gráfico e filtro de data somente após uma conversão bem-sucedida
if st.session_state.get('converted', False):
    # Seleção do período para o histórico de câmbio
    st.write("### Selecione o intervalo de datas para visualizar o histórico de câmbio:")
    
    # Data de hoje
    today = datetime.today()
    
    # Escolher a data para visualizar o histórico
    selected_date = st.date_input("Escolha a data", today)
    
    if selected_date > today:
        st.error("A data selecionada não pode ser no futuro.")
    else:
        # Exibir histórico de câmbio
        history_data = get_exchange_history(base_currency, target_currency, selected_date)
        
        # Depurar: Mostrar a resposta da API para verificar o formato
        st.write("Resposta da API:", history_data)

        if history_data.get("result") == "success" and "conversion_rates" in history_data:
            rate = history_data["conversion_rates"].get(target_currency, None)
            if rate:
                st.write(f"Taxa de câmbio em {selected_date}: **1 {base_currency} = {rate} {target_currency}**")
            else:
                st.warning("Taxa de câmbio não disponível para o período selecionado.")
        else:
            st.warning("Histórico de câmbio não disponível ou não encontrado para a data selecionada.")
