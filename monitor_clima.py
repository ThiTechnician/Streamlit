@@ -0,0 +1,55 @@
import streamlit as st
import requests
import plotly.express as px
import pandas as pd
from datetime import datetime

API_KEY = 'b47721b76a25b9df1a1d8a8ad327d095'

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

# Título da aplicação
st.title("Monitor de Clima em Tempo Real")

# Escolha da cidade
city = st.text_input("Digite o nome da cidade", "São Paulo")

# Botão para buscar o clima
if st.button("Buscar Clima"):
    weather_data = get_weather_data(city)
    
    if weather_data.get("cod") != 200:
        st.error("Cidade não encontrada!")
    else:
        # Extrair dados principais
        temp = weather_data['main']['temp']
        feels_like = weather_data['main']['feels_like']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description'].capitalize()

        # Exibir informações
        st.subheader(f"Condições Climáticas em {city}")
        st.write(f"**Temperatura:** {temp}°C")
        st.write(f"**Sensação Térmica:** {feels_like}°C")
        st.write(f"**Umidade:** {humidity}%")
        st.write(f"**Velocidade do Vento:** {wind_speed} m/s")
        st.write(f"**Descrição:** {description}")

        # Ícone do clima
        icon_code = weather_data['weather'][0]['icon']
        icon_url = f"http://openweathermap.org/img/wn/{icon_code}.png"
        st.image(icon_url)

        # Exibir gráfico da temperatura
        times = [datetime.now().strftime('%H:%M')]  # Horário atual
        temperatures = [temp]

        # DataFrame para gráfico
        df = pd.DataFrame({'Horário': times, 'Temperatura': temperatures})
        fig = px.line(df, x='Horário', y='Temperatura', title='Temperatura Atual')
        st.plotly_chart(fig)
