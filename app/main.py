from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.schemas import Location, AirQualityResponse
from app.service import get_air_quality

# 1️⃣ Criar o app
app = FastAPI(title="Monitoramento da Qualidade do Ar")

# 2️⃣ Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# 3️⃣ Montar pasta estática
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# 4️⃣ Rota inicial
@app.get("/")
async def root():
    return {"message": "Acesse /static/index.html para usar o monitoramento"}

# 5️⃣ Rota para qualidade do ar
@app.post("/air-quality", response_model=AirQualityResponse)
async def air_quality(location: Location):
    data = await get_air_quality(location.latitude, location.longitude)
    return data