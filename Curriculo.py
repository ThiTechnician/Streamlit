import streamlit as st

html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 40px;
            line-height: 1.6;
            color: #333;
        }
        .header {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 30px;
            color: ##000000;
        }
        .subheader {
            font-size: 24px;
            font-weight: bold;
            margin-top: 40px;
            margin-bottom: 15px;
            color: #333;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 5px;
        }
        .experience, .education, .certifications, .languages {
            margin-bottom: 25px;
        }
        .experience-title, .education-title, .certification-title, .language-title {
            font-weight: bold;
            margin-top: 10px;
            color: #333;
        }
        p {
            margin: 8px 0;
        }
        ul {
            margin-left: 20px;
            padding-left: 10px;
        }
        li {
            margin-bottom: 10px;
        }
        .experience ul, .education ul, .certifications ul {
            list-style-type: disc;
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
        <ul>
            <li>Técnico de Copiadoras e Sistemas de Impressão IV – Setor de Soluções (março de 2024 - Presente)</li>
            <li>Responsável pela implantação e suporte de soluções de impressão, digitalização e gestão de dados.</li>
            <li>Desenvolvimento de ferramentas para análise, processamento e visualização de dados.</li>
            <li>Técnico de Copiadoras e Sistemas de Impressão IV (janeiro de 2023 - março de 2024)</li>
            <li>Técnico de Copiadoras e Sistemas de Impressão III (julho de 2017 - janeiro de 2023)</li>
            <li>Técnico de Copiadoras e Sistemas de Impressão II (novembro de 2016 - julho de 2017)</li>
            <li>Técnico PB Jr. (setembro de 2012 - julho de 2017)</li>
            <li>Estagiário (abril de 2012 - setembro de 2012)</li>
        </ul>
    </div>

    <div class="experience">
        <p class="experience-title">Cientista de Dados Autônomo</p>
        <ul>
            <li>Atuando como consultor autônomo em ciência de dados (2024 - Presente)</li>
            <li>Desenvolvendo projetos para otimização de processos e estratégias empresariais usando análise de dados e machine learning.</li>
        </ul>
    </div>

    <div class="subheader">Formação Acadêmica</div>
    <div class="education">
        <ul>
            <li>
                <span class="education-title">Universidade São Judas Tadeu</span><br>
                Bacharelado em Engenharia, Engenharia de Produção (2014 - 2018)
            </li>
            <li>
                <span class="education-title">Anhanguera Educacional</span><br>
                Pós-graduação Lato Sensu - Business intelligence, Big Data e Analytics - Ciência de Dados (junho de 2022 - dezembro de 2022)
            </li>
            <li>
                <span class="education-title">ETEC Getúlio Vargas</span><br>
                Técnico, Mecatrônica (2010 - 2011)
            </li>
            <li>
                <span class="education-title">Senac São Paulo</span><br>
                Técnico, Tecnologia em Desenho Técnico e AutoCAD (2014 - 2015)
            </li>
            <li>
                <span class="education-title">ETEC Guaracy Silveira</span><br>
                Técnico, Eletrônica (2012 - 2012)
            </li>
        </ul>
    </div>

    <div class="subheader">Certificações</div>
    <div class="certifications">
        <ul>
            <li>
                <span class="certification-title">Stanford University</span><br>
                Introdução à Estatística (Emitido em dezembro de 2023)
            </li>
            <li>
                <span class="certification-title">Fundação Getúlio Vargas (FGV)</span><br>
                Introdução à Ciência de Dados (Emitido em outubro de 2023)
            </li>
            <li>
                <span class="certification-title">Alura</span><br>
                Formação Python (Emitido em 2021)
            </li>
        </ul>
    </div>

    <div class="subheader">Idiomas</div>
    <div class="languages">
        <ul>
            <li>
                <span class="language-title">Inglês</span><br>
                Avançado / Fluente
            </li>
        </ul>
    </div>
</body>
</html>
"""
st.components.v1.html(html_content, height=1000, scrolling=True)
