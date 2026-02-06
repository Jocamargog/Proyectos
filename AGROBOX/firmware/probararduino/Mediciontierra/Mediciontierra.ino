int pinHumedad = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int lectura = analogRead(pinHumedad);

  // Calibración real:
  // 470 → 100% humedad
  // 547 → 0% humedad
  float humedad = map(lectura, 420, 650, 100, 0);

  // Limita el valor de humedad entre 0% y 100%
  humedad = constrain(humedad, 0, 100);

  Serial.print("Lectura cruda: ");
  Serial.print(lectura);
  Serial.print(" → Humedad: ");
  Serial.print(humedad);
  Serial.println(" %");

  delay(1000);
}
