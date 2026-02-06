# Guante Traductor de Lengua de Señas

Guante con sensores resistivos variables en cada dedo que reconoce letras del alfabeto en lengua de señas y las traduce a texto mediante un Arduino.

## Descripción general

El sistema utiliza resistencias variables (por ejemplo, flex sensors o resistencias conductivas deformables) cosidas o fijadas en cada dedo de un guante.  
Al hacer una seña, la deformación de los dedos cambia el valor de estas resistencias, generando un patrón analógico característico por letra. Un Arduino lee estos valores, los compara contra una tabla de referencia y muestra o envía la letra reconocida.

## Objetivos del proyecto

- Capturar la postura de la mano para letras individuales de lengua de señas mediante resistencias variables en cada dedo.
- Leer y digitalizar los valores de resistencia con un Arduino.
- Comparar las lecturas con una tabla de calibración para identificar qué letra se está formando.
- Mostrar o transmitir la letra reconocida (por monitor serie, LCD, PC, etc.).

## Hardware

- Guante (base textil).
- 5 sensores resistivos variables (uno por dedo), por ejemplo:
  - Flex sensors.
  - Resistencias conductivas impresas o hiladas.
- Arduino (Uno / Nano / similar) con entradas analógicas suficientes.
- Resistencias fijas (por ejemplo, 10 kΩ) para formar divisores de tensión con cada sensor.
- Cables, protoboard o PCB simple.
- (Opcional) Módulo de visualización:
  - LCD 16x2 / OLED.
  - Comunicación serial a PC.
  - Módulo Bluetooth para enviar la letra a una app.

## Principio de funcionamiento

1. **Sensado de dedos**
   - Cada dedo lleva un sensor resistivo que cambia de valor al doblarse.
   - Cada sensor se conecta en un divisor de tensión:
     - Un extremo del sensor a Vcc.
     - El otro extremo al punto de lectura y a una resistencia fija a GND.
   - El punto medio del divisor se conecta a una entrada analógica del Arduino.

2. **Adquisición de datos**
   - El Arduino lee periódicamente las entradas analógicas (A0–A4) correspondientes a cada dedo.
   - Se obtiene un vector de lecturas, por ejemplo: `[Dedo_meñique, anular, medio, índice, pulgar]`.

3. **Tabla de calibración**
   - Para cada letra soportada (A, B, C, …), se capturan varias muestras de los cinco valores.
   - Se construye una tabla o rango por dedo (mín–máx o valor promedio ± tolerancia) para cada letra.
   - Ejemplo simplificado:
     - Letra “A”: dedo índice muy doblado, otros casi rectos.
     - Letra “B”: todos rectos, etc.

4. **Reconocimiento de letra**
   - En tiempo real, el Arduino compara el vector de lecturas actual con la tabla de calibración.
   - Aplica una regla de decisión (por ejemplo:
     - “si el valor de cada dedo está dentro del rango definido para la letra X, entonces salida = X”).
   - Se envía la letra reconocida por el puerto serie o se muestra en pantalla.

5. **Salida**
   - El resultado puede verse en:
     - Monitor serie de Arduino IDE.
     - Display LCD/OLED.
     - Aplicación en PC/móvil (si se usa Bluetooth/USB).

## Flujo de uso

1. El usuario se coloca el guante.
2. Coloca la mano en la posición de una letra específica.
3. El Arduino lee los valores de las resistencias y calcula qué letra corresponde.
4. La letra se muestra o envía, permitiendo “escribir” letra por letra mediante señas.

## Limitaciones y posibles mejoras

- El sistema básico reconoce letras estáticas; no reconoce palabras completas ni gestos dinámicos.
- La precisión depende de:
  - Buena calibración para cada usuario.
  - Ajuste físico del guante para que los sensores se deformen de forma consistente.
- Mejoras posibles:
  - Usar promedios móviles para reducir ruido.
  - Añadir más sensores (IMU/MPU6050) para diferenciar gestos que dependen de la orientación de la mano.
  - Implementar reconocimiento con algoritmos de clasificación (k-NN, SVM, redes neuronales).