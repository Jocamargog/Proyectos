# Proyecto Balanza con Galga Extensiométrica

Diseño, implementación y calibración de una balanza electrónica basada en una celda de carga de 1 kg y un amplificador de instrumentación AD620, con lectura mediante Arduino y visualización en MATLAB.

## Descripción general

En este proyecto se implementa un sistema de medición de peso que utiliza una celda de carga con galgas extensiométricas conectadas en puente de Wheatstone y un amplificador de instrumentación AD620 como etapa única de acondicionamiento. La señal diferencial de milivoltios se amplifica al rango 0–5 V, compatible con el ADC de 10 bits del Arduino Uno, y se visualiza en tiempo real mediante una interfaz gráfica en MATLAB.

## Objetivos

- Diseñar e implementar el acondicionamiento de señal para una celda de carga de 1 kg usando solo un AD620.
- Ajustar cero (offset) y ganancia (escala máxima) para mapear 0–1000 g en aproximadamente 0–5 V.
- Caracterizar estáticamente el sistema (sensibilidad, linealidad, resolución, histéresis, exactitud) y estimar incertidumbres tipo A y B.
- Analizar la respuesta dinámica y modelar el sistema como un sistema de primer orden.

## Características técnicas

- Sensor: celda de carga de 1 kg con galgas extensiométricas en puente de Wheatstone, alimentada a 5 V.
- Acondicionamiento:
  - AD620 con resistencia de ganancia \(R_G ≈ 60\ \Omega\), ganancia teórica ≈ 824.
  - Ajuste de offset mediante potenciómetro en pin REF para salida ≈ 0 V sin carga.
- Electrónica y adquisición:
  - Alimentación del AD620 ±10/12 V según montaje.
  - Arduino Uno como ADC de 10 bits (0–5 V, resolución ≈ 4,88 mV/LSB).
- Software:
  - Lectura continua del canal analógico del Arduino.
  - Envío por puerto serie a MATLAB.
  - GUI en MATLAB para mostrar peso y evolución temporal.

## Resultados de calibración

- Rango de medición: 0–1000 g.
- Rango de salida: ~0–5 V, con margen para evitar saturación.
- Sensibilidad experimental: ~5 mV/g (5 V/kg).
- Recta de calibración (mínimos cuadrados): pendiente ≈ 0,005 V/g, offset ≈ 0,013 V.
- Linealidad: coeficiente de correlación \(R^2 ≈ 0,9996\), indicando comportamiento casi perfectamente lineal.

## Incertidumbre y desempeño

- Incertidumbre tipo A: obtenida a partir de la desviación estándar de 20 mediciones por punto.
- Incertidumbre tipo B: asociada a la resolución del ADC (~4,88 mV), estimada ≈ 2,82 mV.
- Incertidumbre combinada típica: ≈ 3,88 mV, inferior a la sensibilidad del sistema, lo que respalda la confiabilidad de las mediciones.
- El modelo de calibración es apto para determinar masas desconocidas dentro del rango de 0–1000 g con precisión adecuada para aplicaciones de instrumentación.

## Respuesta dinámica

- Ensayo de carga abrupta (≈ 400 g) para analizar la respuesta transitoria.
- Comportamiento similar a sistema de primer orden con:
  - Valor final ≈ 2,1 V.
  - Constante de tiempo \(\tau ≈ 0,6\) s (≈ 63,2 % del cambio total).
  - Tiempo de establecimiento: ≈ 2–3 s para entrar en ±2 % del valor final.
- Modelo temporal aproximado: \(y(t) = 2,1 \cdot (1 - e^{-t/0,6})\).

## Ventajas del diseño

- Uso exclusivo de un AD620 como etapa de acondicionamiento, reduciendo componentes adicionales.
- Alta estabilidad, baja deriva y offset ajustable con precisión mediante REF.
- Salida directamente compatible con el ADC del Arduino y flujo sencillo hacia MATLAB.
- Arquitectura adecuada para aplicaciones de pesaje estático, con buena linealidad y baja incertidumbre.