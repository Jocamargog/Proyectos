# Llave Digital para un Vehículo

Proyecto de “digital car key” basado en LoRa y SDR para abrir, cerrar y encender un vehículo a partir de comandos inalámbricos demodulados en software.

## Descripción general

El sistema transmite tres comandos (ABRIR, CERRAR, ENCENDER) desde un módulo LoRa (SX1278/Ra-02) controlado por Arduino, utilizando modulación CSS (Chirp Spread Spectrum).  
Las señales se reciben con un RTL-SDR, se procesan en Python y se conectan a una interfaz gráfica que simula el estado del vehículo (puertas y motor).

## Objetivos del proyecto

- Implementar una “llave digital” que envíe comandos simples (00, 10, 11) para controlar puertas y encendido.
- Transmitir los comandos vía LoRa usando chirps ascendentes y descendentes (CSS).
- Recibir la señal con un SDR, demodularla en Python (detección de chirps, FFT, correlación) y reconstruir los bits.
- Visualizar el estado del vehículo en una interfaz gráfica (Python, pygame/tkinter).

## Tecnologías utilizadas

- Hardware:
  - Arduino como controlador y transmisor LoRa.
  - Módulo LoRa SX1278 (Ra-02) a 433 MHz.
  - RTL-SDR como receptor RF.
- Software:
  - Librería LoRa.h (Sandeep) en Arduino.
  - Python con `numpy`, `scipy`, `matplotlib`, librería del SDR (`rtlsdr`) para captura y procesado.
  - GNU Radio / CubicSDR para visualización del espectro.
  - Pygame y Tkinter para la interfaz gráfica de estados (OPEN, ENGINE, CLOSE, INCONCLUSO).

## Metodología

Flujo de señal:

1. **Transmisión (Arduino + LoRa)**  
   - Configuración de SF, ancho de banda, tasa de codificación, syncword y potencia.  
   - Dos interruptores definen el comando:  
     - `00`: cerrar puertas  
     - `10`: abrir puertas  
     - `11`: encender motor  
   - Se arma el paquete LoRa y se envía periódicamente.

2. **Recepción (RTL-SDR + Python)**  
   - Configuración del SDR: frecuencia, ganancia, tasa de muestreo.  
   - Captura de muestras IQ y almacenamiento en un buffer o archivo `.bin`.  
   - Filtro pasa–banda alrededor de la portadora para eliminar interferencias.  
   - FFT para analizar energía en frecuencia y observar chirps.

3. **Demodulación en Python**  
   - Generación de un chirp de referencia (up-chirp/down-chirp).  
   - Detección de chirps por correlación entre señal filtrada y chirp de referencia.  
   - Conversión de posiciones de chirps → símbolos LoRa → bits.  
   - Mapeo de bits a texto y comandos (“OPEN”, “CLOSE”, “START”).

4. **Interfaz gráfica**  
   - Recepción del comando decodificado.  
   - Actualización de la GUI: estados OPEN, ENGINE, CLOSE.  
   - Estado adicional “inconcluso” (pantalla negra 0,5 s) cuando la demodulación es poco confiable.

## Resultados y observaciones

- Se logró:
  - Transmitir correctamente patrones de bits desde Arduino via LoRa.
  - Visualizar la señal en GNU Radio/CubicSDR en tiempo y frecuencia.
  - Captar los pulsos periódicos en Python y extraer bits en varios casos.
- Limitaciones:
  - Fallos frecuentes de demodulación por ruido, ganancia del SDR y sincronización.
  - Falsos bits y paquetes parcialmente capturados.
  - Bibliotecas LoRa para GNU Radio (gr-lora) desactualizadas, dificultando la decodificación directa.

## Posibles mejoras

- Ajustar mejor la ganancia del SDR y el filtrado pasa–banda para mejorar SNR.
- Implementar sincronización más robusta (detección precisa de preámbulo y syncword).
- Usar o adaptar bloques modernos de LoRa en GNU Radio para decodificación completa.
- Añadir detección de errores (CRC) y reenvío de comandos para aumentar confiabilidad.