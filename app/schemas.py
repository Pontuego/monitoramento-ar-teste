from pydantic import BaseModel

class Location(BaseModel):
    latitude: float
    longitude: float

class AirQualityResponse(BaseModel):
    aqi: int
    status: str
    recommendation: str
    pm2_5: float
    pm10: float
    co: float
    no2: float
    so2: float