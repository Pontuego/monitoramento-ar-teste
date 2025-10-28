import requests

# 1️⃣ Pegar localização aproximada via IP
try:
    response = requests.get("https://ipinfo.io/json")
    response.raise_for_status()
    location_data = response.json()
    lat, lon = map(float, location_data["loc"].split(","))
    city = location_data.get("city", "desconhecida")
    region = location_data.get("region", "")
    country = location_data.get("country", "")
except Exception as e:
    print("Erro ao obter localização:", e)
    exit(1)

print(f"Localização detectada: {city}, {region}, {country}")
print(f"Latitude: {lat}, Longitude: {lon}")

# 2️⃣ Enviar dados para o backend
try:
    backend_url = "http://127.0.0.1:8000/air-quality"  # seu backend
    payload = {"latitude": lat, "longitude": lon}
    headers = {"Content-Type": "application/json"}
    
    response = requests.post(backend_url, json=payload, headers=headers)
    response.raise_for_status()
    air_data = response.json()
except Exception as e:
    print("Erro ao consultar o backend:", e)
    exit(1)

# 3️⃣ Exibir resultados
print("\n=== Qualidade do Ar ===")
print(f"AQI: {air_data.get('aqi')}")
print(f"PM2.5: {air_data.get('pm2_5')}")
print(f"PM10: {air_data.get('pm10')}")
print(f"CO: {air_data.get('co')}")
print(f"NO2: {air_data.get('no2')}")
print(f"SO2: {air_data.get('so2')}")