import streamlit as st

# Especifica o nome do arquivo PDF no mesmo diretório do script
pdf_file = "curriculo_linkedin.pdf"

# CSS para tornar o iframe responsivo
css = """
<style>
iframe {
    width: 100vw; /* Ajusta a largura para 100% da largura da tela */
    height: 100vh; /* Ajusta a altura para 100% da altura da tela */
    border: none; /* Remove a borda do iframe */
}
</style>
"""

# Exibe o PDF usando um iframe
pdf_display = f'<iframe src="{pdf_file}" type="application/pdf"></iframe>'

# Aplica o CSS e exibe o PDF
st.markdown(css + pdf_display, unsafe_allow_html=True)
