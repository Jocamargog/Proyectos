#include <SPI.h>
#include <LoRa.h>

// Pines para LoRa SX1278 en Arduino UNO
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

  // Configuración para que coincida con el transmisor
  LoRa.setSpreadingFactor(12);      // Mismo SF que el emisor
  LoRa.setSignalBandwidth(62500);   // Mismo BW
  LoRa.setCodingRate4(8);           // Mismo Coding Rate

  Serial.println("Receptor LoRa listo");
}

void loop() {
  int packetSize = LoRa.parsePacket();
  if (packetSize) {
    Serial.print("Mensaje recibido: ");

    while (LoRa.available()) {
      String message = LoRa.readString();
      Serial.print(message);
    }

    // Mostrar información adicional
    Serial.print("  RSSI: ");
    Serial.print(LoRa.packetRssi());
    Serial.print(" dBm | SNR: ");
    Serial.println(LoRa.packetSnr());
  }
  delay(100);
}
