# Sistema de Monitoreo Agronómico con LoRa y Antenas Yagi

Proyecto de diseño, simulación, construcción y prueba en campo de una estación agrometeorológica de bajo costo basada en LoRa (433 MHz) y antenas Yagi de 7 elementos.

## Descripción general

El sistema mide temperatura ambiente, humedad relativa del aire y humedad del suelo mediante sensores DHT11 y un sensor capacitivo de humedad, y transmite los datos usando módulos LoRa SX1278 (Ra-02) operando en 433 MHz.  
Para cumplir con el requerimiento de enlace estable a más de 1 km, se diseñaron, simularon y fabricaron antenas Yagi-Uda personalizadas, logrando comunicación confiable hasta 1,2 km en pruebas de campo con línea de vista.

## Objetivos del proyecto

- Diseñar y comparar dos opciones de antena (Yagi vs monopolo λ/4) para un enlace LoRa a 433 MHz.
- Obtener un diseño de antena con impedancia cercana a 50 Ω y ganancia suficiente (≈ 9,7 dBi) para cubrir 1 km o más.
- Integrar sensores ambientales con módulos LoRa y Arduino para monitoreo remoto.
- Validar la antena y el enlace mediante caracterización con VNA y pruebas de campo reales.
- Verificar cumplimiento con la normativa colombiana (ANE) para la banda ISM de 433 MHz.

## Diseño y simulación de la antena Yagi

- Se eligió la antena Yagi frente al monopolo λ/4: aunque el monopolo ofrece adaptación fácil a 50 Ω, su ganancia (~2,1 dBi) es insuficiente para el alcance deseado; la Yagi permite ganancias entre 7 y 13 dBi.
- Configuración seleccionada: Yagi-Uda de 7 elementos:
  - 1 reflector
  - 1 dipolo alimentado
  - 5 directores
- Resultados de simulación:
  - Impedancia de resonancia ≈ 36 Ω.
  - Directividad ≈ 9,77 dB.
  - Lóbulo principal en 0° (alta directividad).
  - Ancho de banda en S11 suficiente para cubrir la banda de operación, aunque no centrado exactamente en la frecuencia de diseño.

Medidas físicas (≈ 433 MHz):

| Elemento   | Longitud (cm) | Espaciado (cm) |
|-----------|---------------|----------------|
| Reflector | 34,64         | 12,47          |
| Dipolo    | 33,02         | 6,24           |
| Dir. 1    | 31,87         | 12,47          |
| Dir. 2    | 30,02         | 12,47          |
| Dir. 3    | 29,79         | 12,47          |
| Dir. 4    | 29,09         | 12,47          |
| Dir. 5    | 29,09         | 12,47          |

## Construcción y hardware

- Estructura mecánica:
  - Boom de balso cuadrado de 3 cm de lado y 1 m de largo.
  - Elementos en alambre de cobre esmaltado calibre 14 (≈ 1,64 mm de diámetro).
  - Montaje con silicona sobre el boom.
  - Conector SMA soldado al dipolo.
  - Soportes adicionales en balso y cartón para fijar antenas y electrónica.
- Electrónica:
  - 2 módulos LoRa Ra-02 (SX1278) como Tx/Rx.
  - 2 placas Arduino UNO para adquisición y transmisión/recepción.
  - Sensor DHT11 para temperatura y humedad relativa.
  - Sensor capacitivo de humedad de suelo (0–3 V ~ seco–saturado).

## Sistema de comunicación

- Tecnología LoRa:
  - Modulación CSS (Chirp Spread Spectrum), ancho de banda típico 125 kHz.
  - Alta inmunidad a interferencias y bajo consumo de energía.
  - Frecuencia de operación: 433 MHz.
  - Sensibilidad del chip SX1278 hasta ≈ −148 dBm; potencia Tx configurable hasta +20 dBm (en el proyecto se usó ≈ 2 dBm).
- Sensores:
  - DHT11: HR 20–90 % (±5 %), temperatura 0–50 °C (±2 °C), protocolo 1-Wire (40 bits).
  - Sensor capacitivo: 0–100 % de humedad volumétrica con precisión ≈ ±0,3 %, mapea humedad a tensión (0–3 V).

## Resultados de caracterización de antenas

Ensayos con analizador vectorial de redes (VNA) entre 200 y 600 MHz:

- Antena receptora (Rx):
  - Mínimo de |S11| ≈ −26,7 dB a 428,57 MHz.
  - Impedancia en resonancia: Z ≈ 54,10 + j2,53 Ω (cercana a 50 Ω, casi resistiva).
  - Reflejo de potencia < 0,2 %, buena adaptación y baja pérdida por desadaptación.
- Antena transmisora (Tx):
  - Mínimo de |S11| ≈ −21,5 dB a 428,57 MHz.
  - Impedancia: Z ≈ 57,11 − j5,57 Ω (levemente inductiva, predominantemente resistiva).
  - Reflejo de potencia < 0,8 %, adecuada para transmisión.

## Pruebas de campo y desempeño del enlace

- Distancias probadas: 350 m, 700 m y 1200 m, con línea de vista y correcta alineación de las Yagi.
- Se transmitieron paquetes LoRa con:
  - Temperatura (T) y humedad relativa (H) del DHT11.
  - Humedad de suelo (S) del sensor capacitivo.
- En todas las distancias se mantuvo la comunicación estable cuando las antenas estaban bien alineadas.
- El receptor muestra T, H, S, junto con RSSI y SNR para evaluar la calidad del enlace.
- Se utilizaron intervalos de medición de ≈ 1 segundo entre paquetes.

Errores observados:
- En general, los mensajes se recibieron íntegros.
- Ocasionalmente aparecieron caracteres extraños o corruptos, asociados a:
  - Ruido/interferencias en el canal.
  - Desalineación momentánea de antenas.
  - Mayor distancia y condiciones de entorno.

## Potencia radiada y normativa

Cálculo de potencia efectiva radiada:

- Potencia de salida del módulo LoRa: 2 dBm.
- Ganancia antena Yagi (simulación): 9,77 dBi.
- Pérdidas en cables y conectores: 1,2 dB.
- Pérdida por desadaptación (reflexión): ≈ 0,014 dB.

\[
P_{\text{radiada}} = P_{\text{Tx}} + G_{\text{antena}} - L_{\text{cables}} - L_{\text{reflexión}} 
\approx 10,56\ \text{dBm}
\]

Las pérdidas reales hacen que la potencia efectiva quede cerca pero por debajo del límite de 10 mW (10 dBm) exigido para transmisores no licenciados en la banda ISM de 433 MHz, cumpliendo la Resolución 105 de 2020 (y su actualización 737 de 2022) de la ANE para uso libre de esta banda.

## Costos estimados

- Componentes principales (LoRa, Arduinos, sensores, cobre, conectores, soporte, materiales varios): ≈ 204.500 COP.
- Tiempo de ingeniería (4 personas, 15 h totales a 5.000 COP/h): ≈ 300.000 COP.
- Costo total aproximado del proyecto: ≈ 604.500 COP.

## Conclusiones clave

- Se logró un sistema de monitoreo agro-meteorológico de bajo costo con enlace LoRa robusto y confiable hasta 1,2 km, superando el requisito inicial de 500 m.
- Las antenas Yagi de 7 elementos mostraron excelente adaptación (|S11| < −20 dB) y alto rendimiento pese a su construcción artesanal.
- El diseño respeta el marco normativo colombiano para la banda ISM de 433 MHz, demostrando que es posible combinar alta ganancia y cumplimiento regulatorio.
- Para mejorar aún más:
  - Incorporar corrección de errores (CRC/FEC) y mecanismos de reintento.
  - Afinar el diseño de la Yagi para centrar la resonancia en 433 MHz y reducir errores esporádicos de datos.