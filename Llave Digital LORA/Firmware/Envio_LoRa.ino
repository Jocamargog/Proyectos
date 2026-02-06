#include <SPI.h>
#include <LoRa.h>

// Definir pines de conexión con el módulo LoRa SX1278 (Ra-02)
#define NSS 10    // Pin de selección de esclavo (CS)
#define RST 9     // Pin de reset
#define DIO0 2    // Pin de interrupción DIO0

void setup() {
    Serial.begin(9600);
    while (!Serial);
    
    Serial.println("Iniciando LoRa...");
    
    // Configurar los pines del módulo LoRa
    LoRa.setPins(NSS, RST, DIO0);
    
    // Iniciar LoRa a 433 MHz
    if (!LoRa.begin(433E6)) {
        Serial.println("Error al iniciar LoRa");
        while (1);
    }

    Serial.println("LoRa iniciado correctamente.")  ;
}

void loop() {
    Serial.println("Enviando mensaje...");
    
    // Iniciar paquete de datos
    LoRa.beginPacket();
    LoRa.print("Hola, LoRa desde Arduino Uno!");
    LoRa.endPacket();

    Serial.println("Mensaje enviado!");
    
    delay(5000); // Esperar 5 segundos antes de enviar otro mensaje
}
