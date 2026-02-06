#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 20, 4);

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.clear();
  
  // Función para escribir centrado limpiando línea
  escribirCentrado("Feliz Navidad", 0);
  escribirCentrado("Inmundo animal", 1);
  escribirCentrado("Y prospero ano nuevo", 2);
  escribirCentrado("Att: Flia. Camargo", 3);
}

void loop() {
  // Nada, mensajes fijos
}

// Función que limpia línea y centra texto
void escribirCentrado(String texto, int fila) {
  // Limpiar toda la línea primero
  lcd.setCursor(0, fila);
  lcd.print("                    ");  // 20 espacios
  
  // Calcular posición central
  int len = texto.length();
  int pos = (20 - len) / 2;
  
  // Escribir centrado
  lcd.setCursor(pos, fila);
  lcd.print(texto);
}
