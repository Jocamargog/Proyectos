# Wearable de Asistencia para Adultos Mayores

Dispositivo vestible de bajo costo para monitoreo y asistencia de personas mayores, con detección de caídas, localización por GPS, envío de alertas por SMS/WiFi e interacción por voz, basado en ESP32.

## Descripción general

El wearable está pensado como un clip/dije cómodo y discreto que la persona mayor puede llevar colgado o sujeto a la ropa.  
Incluye sensores de movimiento para detectar caídas, un micrófono para comandos de voz simples, un botón único de emergencia y módulos de comunicación (SMS y WiFi) para avisar a cuidadores y familiares incluso cuando no hay conexión a Internet.

## Objetivos del proyecto

- Detectar caídas y eventos de inmovilidad sospechosa y generar alertas automáticas.
- Enviar la ubicación GPS y estado del usuario a contactos de emergencia vía SMS cuando no haya WiFi.
- Usar WiFi, cuando esté disponible, para enviar notificaciones a través de Telegram, correo u otros servicios.
- Permitir al usuario pedir ayuda mediante un único botón y comandos de voz sencillos (“ayuda”, “emergencia”, etc.).
- Mantener el dispositivo ligero, cómodo, intuitivo y con autonomía mínima de 24 horas.

## Hardware previsto

- Microcontrolador: ESP32 (mini o estándar), con WiFi y Bluetooth.
- Sensores inerciales: acelerómetro + giroscopio (ej. MPU6050) para detección de caídas y análisis de movimiento.
- Audio:
  - Micrófono (electret o MEMS) para reconocimiento de palabras clave.
  - Buzzer para alertas sonoras y feedback de estado.
- Comunicación:
  - Módulo SMS/3G de bajo costo para envío de mensajes de texto con coordenadas y estado.
  - Módulo GPS para obtener posición (latitud, longitud, precisión).
- Alimentación:
  - Batería Li-Ion / Li-Po 3,7 V.
  - Regulador de voltaje (step-up/step-down) para alimentar ESP32 y periféricos.
  - Circuito de carga (idealmente por USB).
- Interfaz de usuario:
  - Un único botón grande para SOS/confirmaciones.
  - LEDs (y opcionalmente vibrador) para indicar estados (encendido, alerta enviada, error, batería baja).

## Funcionalidades principales

1. **Detección de caídas**
   - Lectura continua de aceleración y giroscopio.
   - Lógica de detección (umbral + algoritmo/IA) para diferenciar caídas de movimientos normales.
   - En caso de caída:
     - Alerta sonora y visual.
     - Periodo breve para que el usuario cancele si se encuentra bien.
     - Envío de SMS y/o notificación por Internet a los contactos configurados con hora y ubicación.

2. **Alertas de emergencia**
   - Pulsación larga del botón SOS envía una alerta inmediata a los contactos.
   - El mensaje incluye: tipo de alerta, posible caída, nivel de batería y posición GPS si está disponible.

3. **Localización y seguimiento básico**
   - Obtención periódica de coordenadas GPS.
   - Envío de ubicación en cada alerta.
   - Posible consulta puntual de posición (por ejemplo, al recibir un SMS comando o vía API cuando haya WiFi).

4. **Interacción por voz**
   - Detección de palabras clave simples (por ejemplo “ayuda”, “cancelar”).
   - Permite disparar una alerta o cancelar una falsa alarma sin necesidad de usar el botón.

5. **Gestión de energía**
   - Modo de bajo consumo cuando no haya movimiento significativo.
   - Activación de sensores y comunicaciones solo cuando sea necesario (evento de caída, botón, consulta).

## Requerimientos y restricciones clave

- Autonomía mínima: 24 h de uso normal.
- Peso máximo aproximado: ≤ 50 g.
- Dimensiones aproximadas: ≤ 5 × 5 × 2 cm (orientado a clip/dije).
- Presupuesto de componentes: ≤ 50 USD (aprox.), priorizando módulos económicos.
- Consumo promedio: < 100 mA.
- Diseño robusto y seguro (sin bordes filosos, materiales amigables con la piel).

## Flujo básico de funcionamiento

1. El usuario se coloca el wearable (clip o dije) al inicio del día.
2. El dispositivo entra en modo monitoreo:
   - Lee sensores inerciales.
   - Mantiene GPS en modo eficiente o activo según la estrategia.
3. Si se detecta una caída:
   - Activa buzzer/LED, espera confirmación/cancelación.
   - Si no hay cancelación, envía SMS (y notificación por WiFi si está disponible).
4. Si el usuario presiona el botón SOS o dice la palabra clave:
   - Envía alerta inmediata con la última ubicación válida.
5. El sistema gestiona el consumo para mantener la batería durante el día completo.
