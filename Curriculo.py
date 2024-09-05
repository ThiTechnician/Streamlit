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
            margin: 20px;
            line-height: 1.6;
            color: #333;
        }
        .header {
            text-align: center;
            font-size: 36px;
            font-weight: bold;
            margin-bottom: 30px;
            color: #000;
        }
        .subheader {
            font-size: 24px;
            font-weight: bold;
            margin-top: 30px;
            margin-bottom: 10px;
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
        .experience-description, .education-description, .certification-description, .language-description {
            margin-left: 20px;
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
        @media (max-width: 768px) {
            .header {
                font-size: 28px;
            }
            .subheader {
                font-size: 20px;
            }
            .experience-title, .education-title, .certification-title, .language-title {
                font-size: 18px;
            }
            .experience-description, .education-description, .certification-description, .language-description {
                margin-left: 10px;
            }
        }
    </style>
</head>
<body>
    <div class="header">
        Thiago Medeiros - Cientista de Dados
    </div>

    <div class="subheader">Experiência</div>
    <div class="experience">
        <p class="experience-title">Cientista de Dados Autônomo</p>
        <p class="experience-description">Atuando como consultor autônomo em ciência de dados (2024 - Presente)</p>
        <p class="experience-description">Desenvolvendo projetos para otimização de processos e estratégias empresariais usando análise de dados e machine learning.</p>
    </div>

    <div class="experience">
        <p class="experience-title">Canon Brasil</p>
        <ul>
            <li>
                <p class="experience-title">Técnico de Copiadoras e Sistemas de Impressão IV – Setor de Soluções (março de 2024 - Presente)</p>
                <p class="experience-description">Responsável pela implantação e suporte de soluções de impressão, digitalização e gestão de dados.</p>
                <p class="experience-description">Desenvolvimento de ferramentas para análise, processamento e visualização de dados.</p>
            </li>
            <li>
                <p class="experience-title">Técnico de Copiadoras e Sistemas de Impressão IV (janeiro de 2023 - março de 2024)</p>
            </li>
            <li>
                <p class="experience-title">Técnico de Copiadoras e Sistemas de Impressão III (julho de 2017 - janeiro de 2023)</p>
            </li>
            <li>
                <p class="experience-title">Técnico de Copiadoras e Sistemas de Impressão II (novembro de 2016 - julho de 2017)</p>
            </li>
            <li>
                <p class="experience-title">Técnico PB Jr. (setembro de 2012 - julho de 2017)</p>
            </li>
            <li>
                <p class="experience-title">Estagiário (abril de 2012 - setembro de 2012)</p>
            </li>
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
                Pós-graduação Lato Sensu - Business Intelligence, Big Data e Analytics - Ciência de Dados (junho de 2022 - dezembro de 2022)
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
