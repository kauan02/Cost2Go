# 🌍 Cost of Living Scraper (com Selenium + Firefox)

Este projeto realiza web scraping automatizado no site Numbeo para extrair os custos médios de vida em qualquer cidade do mundo, incluindo preços de aluguel, restaurantes, internet, academia, transporte e muito mais.

A aplicação foi desenvolvida em Python utilizando o Selenium com o navegador Firefox (via GeckoDriver).

---

## 🚀 Funcionalidades

- Consulta automatizada de custo de vida por cidade
- Extração de dados em tempo real do site Numbeo
- Compatível com modo headless (sem abrir o navegador)
- Preparado para integração futura com banco de dados ou API

---

## 🧱 Estrutura do Projeto

cost_of_living_scraper/
├── scraper.py         # Código principal com Selenium + Firefox
├── requirements.txt   # Dependências do projeto
└── README.md          # Este documento

---

## 📦 Requisitos

- Python 3.8+
- GeckoDriver instalado (https://github.com/mozilla/geckodriver/releases)
- Navegador Firefox instalado

---

## 🔧 Instalação

1. Clone o repositório:

   git clone https://github.com/kauan02/Cost2Go.git
   cd cost-of-living-scraper

2. Crie um ambiente virtual (opcional, mas recomendado):

   python -m venv venv
   source venv/bin/activate   (Linux/macOS)
   venv\Scripts\activate      (Windows)

3. Instale as dependências:

   pip install -r requirements.txt

4. Ajuste o caminho do GeckoDriver:

   No arquivo scraper.py, altere a variável GECKODRIVER_PATH com o caminho correto do seu geckodriver.

---

## 🖥️ Como usar

Execute o script passando o nome da cidade que deseja consultar:

   python scraper.py

Depois de alguns segundos, ele exibirá os custos médios da cidade.

---

## ✅ Exemplo de saída

Custo de vida em Madrid:
Apartment (1 bedroom) in City Centre: € 1,100.00
Meal, Inexpensive Restaurant: € 13.00
Internet (60 Mbps or more): € 30.00
...

---

## 🛠️ Para futuras versões

- Salvamento em banco PostgreSQL
- Previsão de aumento de preços
- Comparação entre cidades
- API REST para integração com frontend

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Abra um issue ou envie um pull request com melhorias, sugestões ou correções.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

---

## 👤 Autor

Desenvolvido por Kauan Barbosa Rezende  
📧 kauanbrezende82@gmail.com  
🔗 https://www.linkedin.com/in/kauan-barbosa-5b8133268/  
🔗 https://github.com/kauan02
