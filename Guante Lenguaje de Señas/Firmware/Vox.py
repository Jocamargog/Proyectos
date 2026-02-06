# -- coding: utf-8 --
"""
Created on Sun Aug 29 13:59:24 2021

@author: Grupo Salud y bienestar

@Title: Lectura del guante por voz

"""
#Inportacion de libreria
import pyttsx3
import serial
import time
#Creacion del motor
motor = pyttsx3.init()
#Modificacion de propiedades
motor.setProperty("rate",100)
motor.setProperty("volume",1)

#voices = motor.getProperty('voices')

#motor.setProperty("voice", voices[2].id)

"""
for voice in voices:
    print("Voice: %s" % voice.name)
    print(" - ID: %s" % voice.id)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    print("\n")

"""
##############################################################
#Puerto Serial
COM = "COM3"
arduinoSerial = serial.Serial(COM,9600)


print ("Inicio de analisis del guante")

while True:
    Dato =  arduinoSerial.readline().strip()
    cad = Dato.decode("ascii")
    print(cad)

    if cad == "A":
        text = "A A A A"
        motor.say(text)
    elif cad == "E":
        text = "E E E E"
        motor.say(text)
    elif cad == "I":
        text = "I I I I"
        motor.say(text)
    elif cad == "O":
        text = "O O O O"
        motor.say(text)
    elif cad == "U":
        text = "U U U U"
        motor.say(text)
    elif cad == "B":
        motor.setProperty("rate", 150)
        text = "Demostracion de funcionamiento, y de posibilidad de mejorar con el uso de mejores sensores"
        motor.say(text)
        motor.setProperty("rate", 100)
    motor.runAndWait()