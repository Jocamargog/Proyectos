from machine import SoftI2C, Pin
from mpu6050 import MPU6050
import time

i2c = SoftI2C(scl=Pin(9), sda=Pin(8))  # ESP32-C3: SCL = 9, SDA = 8

mpu = MPU6050(i2c)

while True:
    accel = mpu.get_accel_data()
    gyro = mpu.get_gyro_data()

    print('Acelerómetro:', accel)
    print('Giroscopio:', gyro)
    print('')  # Línea en blanco para separar las lecturas
    time.sleep(0.5)