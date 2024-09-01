import streamlit as st

html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .header {
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }
        .subheader {
            font-size: 18px;
            font-weight: bold;
            margin-top: 20px;
        }
        .contact, .skills, .experience, .education {
            margin-bottom: 20px;
        }
        .contact p, .skills p, .experience p, .education p {
            margin: 5px 0;
        }
        .experience-title, .education-title {
            font-weight: bold;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="header">
        Thiago Medeiros<br>
        Engenheiro de Produção | Pós-graduado em Ciência de Dados
    </div>
    <div class="subheader">Experiência</div>
    <div class="experience">
        <p class="experience-title">Canon Brasil</p>
        <p>Técnico de Copiadoras e Sistemas de Impressão IV (janeiro de 2023 - Presente)</p>
        <p>Técnico de Copiadoras e Sistemas de Impressão III (julho de 2017 - janeiro de 2023)</p>
        <p>Técnico de Copiadoras e Sistemas de Impressão II (novembro de 2016 - julho de 2017)</p>
        <p>Técnico PB Jr. (setembro de 2012 - julho de 2017)</p>
        <p>Estagiário (abril de 2012 - setembro de 2012)</p>
    </div>

    <div class="subheader">Formação Acadêmica</div>
    <div class="education">
        <p class="education-title">Universidade São Judas Tadeu</p>
        <p>Bacharelado em Engenharia, Engenharia de Produção (2014 - 2018)</p>

        <p class="education-title">Anhanguera Educacional</p>
        <p>Pós-graduação Lato Sensu - Especialização, Business intelligence, big data e analytics - ciência de dados (junho de 2022 - dezembro de 2022)</p>

        <p class="education-title">ETEC Getúlio Vargas</p>
        <p>Técnico, Mecatrônica (2010 - 2011)</p>

        <p class="education-title">Senac São Paulo</p>
        <p>Técnico, Tecnologia em Desenho Técnico e AutoCAD (2014 - 2015)</p>

        <p class="education-title">ETEC Guaracy Silveira</p>
        <p>Técnico, Eletrônica (2012 - 2012)</p>
    </div>
</body>
</html>

"""
st.components.v1.html(html_content, height=800, scrolling=True)
