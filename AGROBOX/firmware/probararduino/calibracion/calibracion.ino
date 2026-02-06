int pinHumedad = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int valorCrudo = analogRead(pinHumedad);
  Serial.print("Lectura cruda: ");
  Serial.println(valorCrudo);
  delay(1000);
}
