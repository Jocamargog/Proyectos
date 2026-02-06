#include <SPI.h>
#include <LoRa.h>

// Pines para SX1278 en Arduino UNO
const int csPin = 10;
const int resetPin = 9;
const int irqPin = 2;

void setup() {
  Serial.begin(9600);
  while (!Serial);

  // Configurar pines LoRa
  LoRa.setPins(csPin, resetPin, irqPin);

  // Iniciar LoRa en 433 MHz
  if (!LoRa.begin(433E6)) {
    Serial.println("Error al iniciar LoRa");
    while (true);
  }

  // Configuración para máxima potencia y alcance
  LoRa.setTxPower(5);              // Máxima potencia con PA_BOOST
  LoRa.setSpreadingFactor(12);      // Mayor alcance, menor velocidad
  LoRa.setSignalBandwidth(62500);   // Ancho de banda bajo (más alcance)
  LoRa.setCodingRate4(8);           // Mayor robustez (CR 4/8)

  Serial.println("Transmisor LoRa listo con máxima potencia");
}

void loop() {
  Serial.println("Transmitiendo...");

  LoRa.beginPacket();
  LoRa.print("Hola 80 metros");
  LoRa.endPacket();

  delay(1000); // espera 1 segundo entre paquetes
}
