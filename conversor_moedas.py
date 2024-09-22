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
def get_exchange_history(base_currency, target_currency):
    today = datetime.today().strftime('%Y-%m-%d')
    one_month_ago = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    url = f"https://api.exchangerate.host/timeseries?start_date={one_month_ago}&end_date={today}&base={base_currency}&symbols={target_currency}"
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
            
            # Exibir histórico de câmbio
            history_data = get_exchange_history(base_currency, target_currency)
            if "rates" in history_data:
                dates = []
                rates = []
                for date, rate in history_data["rates"].items():
                    dates.append(date)
                    rates.append(rate[target_currency])
                
                # Criar DataFrame
                df_history = pd.DataFrame({
                    "Data": pd.to_datetime(dates),
                    f"Taxa de Câmbio ({base_currency} -> {target_currency})": rates
                })

                # Gráfico de variação de câmbio
                fig = px.line(df_history, x="Data", y=f"Taxa de Câmbio ({base_currency} -> {target_currency})", 
                              title=f"Variação da Taxa de Câmbio: {base_currency} para {target_currency}")
                st.plotly_chart(fig)
            else:
                st.warning("Histórico de câmbio não disponível.")
        else:
            st.error("Erro ao obter a taxa de câmbio.")
    else:
        st.warning("Por favor, insira um valor maior que 0.")
