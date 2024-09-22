import streamlit as st
import requests
import plotly.express as px
import pandas as pd
from datetime import datetime

API_KEY = 'sua_chave_api_aqui'

def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data

def get_weather_forecast(city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
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
    forecast_data = get_weather_forecast(city)
    
    if weather_data.get("cod") != 200 or forecast_data.get("cod") != "200":
        st.error("Cidade não encontrada ou erro ao obter dados!")
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

        # Processar dados de previsão para o gráfico
        if 'list' in forecast_data:
            forecast_list = forecast_data['list']
            times = []
            temperatures = []
            for forecast in forecast_list:
                time = forecast['dt_txt']
                temp_forecast = forecast['main']['temp']
                times.append(datetime.strptime(time, '%Y-%m-%d %H:%M:%S'))
                temperatures.append(temp_forecast)
            
            # Criar DataFrame
            df_forecast = pd.DataFrame({
                'Horário': times,
                'Temperatura (°C)': temperatures
            })

            # Filtrar apenas o dia atual ou os próximos dias conforme necessário
            hoje = datetime.now().date()
            df_forecast['Data'] = df_forecast['Horário'].dt.date
            df_today = df_forecast[df_forecast['Data'] == hoje]

            # Gráfico de temperatura ao longo do dia
            fig = px.line(df_today, x='Horário', y='Temperatura (°C)', title='Previsão de Temperatura para Hoje')
            fig.update_xaxes(title_text='Horário')
            fig.update_yaxes(title_text='Temperatura (°C)')
            st.plotly_chart(fig)
        else:
            st.warning("Dados de previsão não disponíveis.")
