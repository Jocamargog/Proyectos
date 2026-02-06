# Réplica del Juego Pong en Python

Proyecto final de Programación de Computadores 1: recreación del clásico videojuego Pong usando Python, inicialmente con Turtle y luego con Pygame para una mejor interfaz gráfica.

## Descripción general

El proyecto consiste en desarrollar una réplica jugable de Pong que permita a los usuarios disfrutar de un juego simple de tenis de mesa digital en su tiempo libre.  
Se utilizaron conceptos básicos de programación vistos en el curso (estructuras de control, funciones, manejo de eventos) y librerías gráficas de Python, evolucionando desde un prototipo en Turtle hasta una versión final en Pygame con una interfaz más atractiva y opciones de juego.

## Objetivos

- Analizar el funcionamiento del Pong original.
- Implementar una copia funcional del juego usando Python 3.8.
- Mejorar la interfaz gráfica respecto al Pong original, aprovechando imágenes y colores.
- Ofrecer modos de juego de uno y dos jugadores.
- Completar el proyecto al finalizar el semestre como ejercicio de aprendizaje práctico.

## Características del juego

- Interfaz gráfica simple y entendible.
- Modos de juego:
  - Un jugador contra la computadora.
  - Dos jugadores (cada uno controla una paleta).
- Menú inicial:
  - Selección de modo de juego.
- Al finalizar la partida:
  - Opción de salir del juego.
  - Opción de volver al menú principal para jugar de nuevo.
- Elementos típicos de Pong:
  - Pelota que rebota en paredes y paletas.
  - Puntuación por jugador.
  - Reinicio de la pelota tras cada punto.

## Tecnologías y librerías

- Lenguaje: **Python 3.8**.
- Primer prototipo:
  - Librería **Turtle** para gráficos básicos (ventana, paletas, pelota).
- Versión final:
  - Librería **Pygame** para:
    - Ventana del juego.
    - Dibujado de paletas, pelota y fondo.
    - Manejo de teclado.
    - Actualización de pantalla y control de FPS.
    - Posible uso de imágenes para mejorar la estética.

## Evolución del proyecto

1. **Versión 1 – Turtle**
   - Implementación base del juego (lógica de movimiento y rebotes).
   - Mecánicamente funcional, pero con interfaz muy básica y limitada en diseño.

2. **Versión 2 – Pygame básica**
   - Migración a Pygame.
   - Estructura del juego y bucle principal en Pygame.
   - Figuras básicas (rectángulos) para paletas y pelota, sin interfaz pulida.

3. **Versión 3 – Pygame final**
   - Interfaz gráfica mejorada (colores, distribución, textos/menús).
   - Inclusión de los dos modos de juego (1P vs PC, 2P).
   - Menú inicial y pantalla de fin de partida con opciones.

## Flujo de uso

1. Ejecutar el script principal de Pygame.
2. En el menú inicial:
   - Elegir entre modo 1 jugador o 2 jugadores.
3. Jugar la partida:
   - Controlar las paletas (teclas asignadas para cada jugador).
   - La IA controla la paleta contraria en modo 1 jugador.
4. Al terminar:
   - Elegir si volver al menú o salir del juego.
