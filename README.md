# Monitoramento da Qualidade do Ar 🌿🌎

Um sistema web para monitoramento da qualidade do ar em tempo real, utilizando a API de poluição atmosférica da OpenWeatherMap.  
O usuário pode obter os dados de sua localização e visualizar parâmetros como AQI, PM2.5, PM10, CO, NO2, SO2, além de recomendações de saúde baseadas no AQI.

---

## Tecnologias Utilizadas

- [Python 3.13](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [HTTPX](https://www.python-httpx.org/)
- [JavaScript / HTML / CSS](https://developer.mozilla.org/)
- [OpenWeatherMap Air Pollution API](https://openweathermap.org/api/air-pollution)

---

## Como Rodar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/Pontuego/monitoramento-ar-teste.git
cd monitoramento-ar-teste

Crie um ambiente virtual e instale dependências:
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
Crie um arquivo .env na raiz do projeto com sua chave da API do OpenWeatherMap:

API_KEY=SUA_CHAVE_AQUI

Execute o backend:
python -m uvicorn app.main:app --reload

Abra no navegador:
http://127.0.0.1:8000/static/index.html

Funcionalidades
Obter dados da qualidade do ar da localização do usuário.

Exibir os principais poluentes: PM2.5, PM10, CO, NO2, SO2.

Mostrar AQI (Índice de Qualidade do Ar) com status e recomendações.

Interface interativa, responsiva e visualmente agradável.

Gráfico radar (teia) para comparação rápida dos poluentes.

Estrutura do Projeto

monitoramento-ar-teste/
│
├─ app/
│  ├─ main.py           # Inicialização do FastAPI
│  ├─ service.py        # Lógica de requisição da API e cálculo do AQI
│  ├─ schemas.py        # Modelos de dados
│  └─ static/
│      ├─ index.html
│      ├─ style.css
│      └─ chart.js      # Código do gráfico radar
│
├─ .env                 # Chave da API
├─ requirements.txt     # Dependências do projeto
└─ README.md

Futuras Melhorias
Transformar em aplicativo mobile (Android/iOS).

Melhorar gráficos e visualizações.

Adicionar alertas por poluentes críticos.
