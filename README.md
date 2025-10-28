# Monitoramento da Qualidade do Ar 🌿

Este projeto permite monitorar a qualidade do ar em tempo real com base na sua localização. Ele exibe informações como AQI, PM2.5, PM10, CO, NO2 e SO2, e fornece status e recomendações de acordo com o índice de poluição.

---

## 🔹 Funcionalidades

- Obter a qualidade do ar com base na geolocalização do usuário.
- Exibir AQI (Air Quality Index) e poluentes principais.
- Fornecer status visual e recomendações para atividades ao ar livre.
- Atualização automática a cada 5 minutos.
- Estilo responsivo e moderno, com cores indicativas do nível de poluição.

---

## 🛠 Tecnologias Utilizadas

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python, FastAPI  
- **Servidor:** Uvicorn  
- **API externa:** OpenWeatherMap Air Pollution API  
- **Docker:** Para containerizar a aplicação

---

## 🚀 Como Rodar o Projeto

### Pré-requisitos

- Python 3.11 ou superior
- Docker (opcional, mas recomendado para container)
- Conta na [OpenWeatherMap](https://openweathermap.org/api) para obter a `API_KEY`

---

### Rodando localmente

1. Clone o repositório:

```bash
git clone https://github.com/Pontuego/monitoramento-ar-teste.git
cd monitoramento-ar-teste

2. Instale dependências:



pip install -r requirements.txt

3. Configure a variável de ambiente com sua API Key:



export API_KEY="SUA_CHAVE_AQUI"   # Linux / Mac
setx API_KEY "SUA_CHAVE_AQUI"     # Windows

4. Rode o backend:



uvicorn app.main:app --reload

5. Acesse o frontend no navegador:



http://127.0.0.1:8000/static/index.html


---

Rodando com Docker

1. Build da imagem:



docker build -t monitoramento-ar .

2. Rodar o container:



docker run -p 8000:8000 -e API_KEY=SUA_CHAVE_AQUI monitoramento-ar

3. Acesse no navegador:



http://localhost:8000/static/index.html


---

📦 Estrutura do Projeto

monitoramento-ar-teste/
│
├─ app/
│   ├─ main.py           # Backend FastAPI
│   ├─ service.py        # Funções para buscar dados da API
│   ├─ api.py            # Rotas da API
│   └─ schemas.py        # Schemas de validação
│
├─ static/
│   ├─ index.html        # Frontend
│   └─ style.css         # CSS
│
├─ requirements.txt      # Dependências Python
└─ Dockerfile            # Container Docker


---

⚠️ Observações

Certifique-se de ter uma chave válida da OpenWeatherMap.

O backend precisa estar rodando para que o frontend funcione corretamente.

A aplicação usa geolocalização, portanto o navegador pedirá permissão para acessar sua localização.



---
