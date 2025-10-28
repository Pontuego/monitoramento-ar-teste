import React, { useEffect, useState } from "react";
import { View, Text, ActivityIndicator, StyleSheet } from "react-native";
import * as Location from "expo-location";
import { getAirQuality } from "../api";

export default function Home() {
  const [location, setLocation] = useState(null);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [errorMsg, setErrorMsg] = useState(null);

  // Solicitar permissão de localização
  useEffect(() => {
    (async () => {
      let { status } = await Location.requestForegroundPermissionsAsync();
      if (status !== "granted") {
        setErrorMsg("Permissão para acessar localização negada.");
        setLoading(false);
        return;
      }
      let loc = await Location.getCurrentPositionAsync({});
      setLocation(loc.coords);
    })();
  }, []);

  // Buscar dados do backend quando a localização estiver disponível
  useEffect(() => {
    if (location) {
      (async () => {
        setLoading(true);
        const result = await getAirQuality(location.latitude, location.longitude);
        setData(result);
        setLoading(false);
      })();
    }
  }, [location]);

  if (loading) {
    return (
      <View style={styles.container}>
        <ActivityIndicator size="large" />
        <Text>Carregando dados...</Text>
      </View>
    );
  }

  if (errorMsg) {
    return (
      <View style={styles.container}>
        <Text>{errorMsg}</Text>
      </View>
    );
  }

  // Função para determinar cor do status
  const getStatusColor = (status) => {
    if (!status) return "gray";
    if (status.toLowerCase().includes("bom")) return "green";
    if (status.toLowerCase().includes("moderado")) return "orange";
    return "red";
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Qualidade do Ar</Text>
      {data ? (
        <View style={styles.dataContainer}>
          <Text>AQI: {data.aqi}</Text>
          <Text>PM2.5: {data.pm25}</Text>
          <Text>PM10: {data.pm10}</Text>
          <Text style={{ color: getStatusColor(data.status) }}>Status: {data.status}</Text>
        </View>
      ) : (
        <Text>Não foi possível carregar os dados.</Text>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: "center", alignItems: "center", padding: 20 },
  title: { fontSize: 24, fontWeight: "bold", marginBottom: 20 },
  dataContainer: { alignItems: "flex-start" },
});