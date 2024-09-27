import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Função para enviar email
def send_email(subject, message, from_email):
    to_email = "seu_email@gmail.com"  # Substitua pelo seu email de destino
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Adiciona a mensagem ao corpo do email
    msg.attach(MIMEText(message, 'plain'))

    # Configuração do servidor SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, 'SUA_SENHA_DO_EMAIL')  # Substitua pela sua senha
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    server.quit()

# Interface do formulário de contato
st.title("Entre em Contato")

st.write("Preencha o formulário abaixo para entrar em contato.")

with st.form("contact_form"):
    name = st.text_input("Nome", max_chars=100)
    email = st.text_input("E-mail", max_chars=100)
    contact_reason = st.selectbox("Selecione o motivo do contato", 
                                  ["Orçamento de projeto de ciência de dados", "Oferecendo posição de trabalho"])
    details = st.text_area("Descreva mais detalhes aqui", height=200)
    submit = st.form_submit_button("Enviar")

if submit:
    if not name or not email or not details:
        st.error("Por favor, preencha todos os campos antes de enviar.")
    else:
        # Estrutura da mensagem de e-mail
        subject = f"Contato via portfólio: {contact_reason}"
        message = f"Nome: {name}\nE-mail: {email}\nMotivo: {contact_reason}\n\nDetalhes:\n{details}"
        
        # Enviar o e-mail
        try:
            send_email(subject, message, from_email=email)
            st.success("Sua mensagem foi enviada com sucesso!")
        except Exception as e:
            st.error(f"Houve um erro ao enviar o e-mail: {e}")
