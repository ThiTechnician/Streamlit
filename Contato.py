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

# Adiciona estilização CSS
st.markdown("""
    <style>
    .contact-form {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 700px;
        margin: 0 auto;
        font-family: Arial, sans-serif;
    }

    .contact-form input, .contact-form select, .contact-form textarea {
        width: 100%;
        padding: 10px;
        margin: 8px 0;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-size: 16px;
        font-family: Arial, sans-serif;
    }

    .contact-form button {
        background-color: #4CAF50;
        color: white;
        padding: 15px 20px;
        margin-top: 10px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 18px;
        font-family: Arial, sans-serif;
        width: 100%;
    }

    .contact-form button:hover {
        background-color: #45a049;
    }

    h1, h3 {
        text-align: center;
        color: #333;
    }

    .success-message {
        color: green;
        text-align: center;
        font-size: 20px;
        margin-top: 20px;
    }

    .error-message {
        color: red;
        text-align: center;
        font-size: 20px;
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# Título da página
st.title("Entre em Contato")

# Subtítulo
st.markdown("<h3>Preencha o formulário abaixo para entrar em contato</h3>", unsafe_allow_html=True)

# Formulário de contato estilizado
with st.form("contact_form", clear_on_submit=True):
    st.markdown('<div class="contact-form">', unsafe_allow_html=True)
    
    name = st.text_input("Nome", max_chars=100)
    email = st.text_input("E-mail", max_chars=100)
    contact_reason = st.selectbox("Selecione o motivo do contato", 
                                  ["Orçamento de projeto de ciência de dados", "Oferecendo posição de trabalho"])
    details = st.text_area("Descreva mais detalhes aqui", height=200)
    submit = st.form_submit_button("Enviar")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Processamento do formulário
if submit:
    if not name or not email or not details:
        st.markdown('<p class="error-message">Por favor, preencha todos os campos antes de enviar.</p>', unsafe_allow_html=True)
    else:
        # Estrutura da mensagem de e-mail
        subject = f"Contato via portfólio: {contact_reason}"
        message = f"Nome: {name}\nE-mail: {email}\nMotivo: {contact_reason}\n\nDetalhes:\n{details}"
        
        # Enviar o e-mail
        try:
            send_email(subject, message, from_email=email)
            st.markdown('<p class="success-message">Sua mensagem foi enviada com sucesso!</p>', unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f'<p class="error-message">Houve um erro ao enviar o e-mail: {e}</p>', unsafe_allow_html=True)
