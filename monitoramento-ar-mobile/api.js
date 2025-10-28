// Substitua pelo IP da sua máquina na rede local
export const BASE_URL = "http://172.22.115.174:8000"; 

export async function getAirQuality(lat, lon) {
  try {
    const response = await fetch(`${BASE_URL}/air-quality?lat=${lat}&lon=${lon}`);
    if (!response.ok) throw new Error("Erro ao buscar dados do backend");
    const data = await response.json();
    return data;
  } catch (error) {
    console.error(error);
    return null;
  }
}