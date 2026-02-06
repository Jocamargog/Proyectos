#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>

// Configuración del LCD
LiquidCrystal_I2C lcd(0x27, 20, 4);

// Pines de sensores
#define PIN_SUELO A0
#define DHTPIN 2
#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("Sistema de monitoreo");
  delay(2000);
  lcd.clear();
}

void loop() {
  // Lectura sensor de suelo
  int lecturaSuelo = analogRead(PIN_SUELO);
  float humedadSuelo = map(lecturaSuelo, 420, 650, 100, 0);
  humedadSuelo = constrain(humedadSuelo, 0, 100);

  // Lectura sensor DHT11
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  float h_cor = h;
  float t_cor = t - 7; 

  // Validar lecturas del DHT11
  if (isnan(h) || isnan(t)) {
    Serial.println("Error al leer el sensor DHT11");
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Error en DHT11");
    delay(2000);
    return;
  }

  // Mostrar por consola
  Serial.print("Humedad suelo: ");
  Serial.print(humedadSuelo);
  Serial.print("% (");
  Serial.print(lecturaSuelo);
  Serial.println(")");

  Serial.print("Temp: ");
  Serial.print(t);
  Serial.print(" °C | Humedad aire: ");
  Serial.print(h);
  Serial.println(" %");

  // Mostrar en el LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("Hum. suelo: ");
  lcd.print(humedadSuelo);
  lcd.print(" %");

  lcd.setCursor(0, 1);
  lcd.print("Lectura cruda: ");
  lcd.print(lecturaSuelo);

  lcd.setCursor(0, 2);
  lcd.print("Temp: ");
  lcd.print(t_cor);
  lcd.print(" ");
  lcd.print((char)223); // Símbolo de grado
  lcd.print("C");

  lcd.setCursor(0, 3);
  lcd.print("Hum. aire: ");
  lcd.print(h_cor);
  lcd.print(" %");

  delay(2000);
}
