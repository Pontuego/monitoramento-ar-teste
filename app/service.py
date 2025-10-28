import httpx
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

async def get_air_quality(lat: float, lon: float):
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    main = data['list'][0]['main']
    components = data['list'][0]['components']

    pm2_5 = components['pm2_5']
    
    # Calcular AQI, status e recomendação baseado no PM2.5
    if pm2_5 is None:
        aqi, status, recommendation = None, "Erro", "Não há dados de PM2.5 disponíveis."
    elif pm2_5 <= 12:
        aqi, status, recommendation = 1, "Bom", "Excelente para atividades ao ar livre!"
    elif pm2_5 <= 35:
        aqi, status, recommendation = 2, "Moderado", "Seguro, mas evite esforço físico intenso."
    elif pm2_5 <= 55:
        aqi, status, recommendation = 3, "Ruim", "Pessoas sensíveis devem evitar sair."
    elif pm2_5 <= 150:
        aqi, status, recommendation = 4, "Muito Ruim", "Evite sair de casa, o ar está poluído."
    else:
        aqi, status, recommendation = 5, "Perigoso", "Permaneça em casa — risco grave à saúde."

    return {
        "aqi": aqi,
        "status": status,
        "recommendation": recommendation,
        "pm2_5": pm2_5,
        "pm10": components['pm10'],
        "co": components['co'],
        "no2": components['no2'],
        "so2": components['so2']
    }