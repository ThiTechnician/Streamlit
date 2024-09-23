import streamlit as st

# URL pública do notebook do Google Colab
colab_url = "https://colab.research.google.com/drive/1hUdU3XB8FsPLW1QybYYuhF5cl64llmuw?usp=sharing"  # Substitua pelo link gerado

# Exibe o notebook usando um iframe
st.components.v1.iframe(colab_url, width=800, height=600)
