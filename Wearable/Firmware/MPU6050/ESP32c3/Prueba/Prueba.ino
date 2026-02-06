#include <Wire.h>
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>

Adafruit_MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  delay(1000); // Breve espera para asegurar apertura del puerto serie
  Serial.println("Inicio de programa");

  // Inicializa I2C en pines por defecto del ESP32-C3 (SDA=8, SCL=9)
  Wire.begin(8, 9);

  // Mensaje BEFORE intentar iniciar el sensor
  Serial.println("Intentando iniciar MPU6050...");

  if (!mpu.begin()) {
    Serial.println("No se detectó MPU6050");
    while (1) { delay(10); }
  }
  Serial.println("MPU6050 conectado!");

  mpu.setAccelerometerRange(MPU6050_RANGE_8_G);
  mpu.setGyroRange(MPU6050_RANGE_500_DEG);
  mpu.setFilterBandwidth(MPU6050_BAND_21_HZ);
  delay(100);
}

void loop() {
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);

  Serial.print("Aceleración X: ");
  Serial.print(a.acceleration.x);
  Serial.print(", Y: ");
  Serial.print(a.acceleration.y);
  Serial.print(", Z: ");
  Serial.print(a.acceleration.z);
  Serial.println(" m/s^2");

  Serial.print("Giro X: ");
  Serial.print(g.gyro.x);
  Serial.print(", Y: ");
  Serial.print(g.gyro.y);
  Serial.print(", Z: ");
  Serial.print(g.gyro.z);
  Serial.println(" rad/s");

  Serial.println(""); // separación visual
  delay(500);
}
