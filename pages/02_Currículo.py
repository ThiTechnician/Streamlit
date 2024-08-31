import streamlit as st

# Especifica o nome do arquivo PDF no mesmo diretório do script
pdf_file = "curriculo_linkedin.pdf"

# Exibe o PDF usando um iframe
pdf_display = f'<iframe src="{pdf_file}" width="700" height="1000" type="application/pdf"></iframe>'
st.markdown(pdf_display, unsafe_allow_html=True)
