#include <DHT.h>

// Pines de los sensores (no modificar)
const int dhtPin = 7;             // Pin de datos del DHT11
const int sensorSueloPin = 8;     // Pin digital para humedad del suelo

#define DHTTYPE DHT11             // Tipo de sensor
DHT dht(dhtPin, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(sensorSueloPin, INPUT);
  Serial.println("Iniciando sensores...");
}

void loop() {
  float temperatura = dht.readTemperature();
  float humedad = dht.readHumidity();
  int humedadSuelo = digitalRead(sensorSueloPin); // 0 = mojado, 1 = seco

  Serial.println("===============================");
  Serial.println("Lecturas:");

  if (isnan(temperatura) || isnan(humedad)) {
    Serial.println("Error al leer el DHT11");
  } else {
    Serial.print("Temperatura: ");
    Serial.print(temperatura);
    Serial.println(" °C");

    Serial.print("Humedad: ");
    Serial.print(humedad);
    Serial.println(" %");
  }

  Serial.print("Humedad del suelo: ");
  Serial.println(humedadSuelo == 0 ? "Mojado" : "Seco");

  delay(2000); // Esperar 2 segundos
}
