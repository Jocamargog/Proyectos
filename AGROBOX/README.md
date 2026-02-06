# AgroBox

Proyecto de desarrollo de un dispositivo autónomo y modular de bajo costo para el monitoreo inteligente de cultivos de fresa y lechuga en contextos rurales con baja conectividad.

## Descripción general

AgroBox es un sistema portátil que mide en tiempo real temperatura y humedad del aire y del suelo mediante sensores DHT11 y sensores capacitivos, procesando los datos con una red neuronal embebida para generar recomendaciones visuales (regar, ventilar, sombrear) sin requerir conexión a Internet. Está orientado a pequeños y medianos agricultores de Boyacá y Cundinamarca, así como a docentes e investigadores interesados en aplicar inteligencia artificial en la agricultura de precisión.

## Características principales

- Monitoreo de variables ambientales: temperatura y humedad del aire, humedad del suelo.
- Sensores de bajo costo (DHT11 y sensor capacitivo de humedad de suelo) integrados en un prototipo compacto.
- Procesamiento local mediante red neuronal simple entrenada en Python y embebida en un microcontrolador tipo Arduino/ESP32.
- Recomendaciones agronómicas visuales para riego, ventilación y sombreo, pensadas para usuarios sin conocimientos técnicos avanzados.
- Funcionamiento autónomo con batería recargable y diseño pensado para invernaderos y pequeñas parcelas.
- Enfoque en sostenibilidad: uso de baterías recargables, carcasas plásticas reciclables y plan de devolución de componentes electrónicos al final de su vida útil.

## Contexto y motivación

En Colombia, la productividad agrícola se mantiene rezagada frente a economías como Brasil debido a baja inversión en innovación, limitada conectividad rural y escaso acceso a datos técnicos, lo que afecta especialmente a pequeños productores. Un análisis PESTAL evidenció barreras políticas, económicas, ambientales, tecnológicas, sociales y legales que dificultan la tecnificación del campo y la adopción de soluciones digitales. AgroBox busca cerrar parte de esta brecha mediante una herramienta accesible que traduzca datos ambientales en acciones concretas para el agricultor.

## Objetivos del proyecto

- Incrementar la productividad de cultivos de fresa y lechuga mediante monitoreo en tiempo real de variables críticas y apoyo a la toma de decisiones de riego y manejo ambiental.
- Diseñar y construir un prototipo funcional de bajo costo, autónomo y fácil de usar, adecuado para zonas rurales con baja conectividad.
- Integrar hardware, software e inteligencia artificial en un sistema embebido que genere recomendaciones claras e intuitivas para pequeños agricultores.
- Validar el dispositivo en invernaderos de la Universidad Nacional de Colombia y con usuarios rurales, recogiendo retroalimentación para iterar el diseño.

## Alcance

El proyecto contempla el desarrollo de un prototipo que:

- Mide en tiempo real temperatura, humedad relativa del aire y humedad del suelo.
- Procesa los datos localmente con una red neuronal para generar recomendaciones agronómicas.
- Muestra resultados en una pantalla LCD 20x4 con interfaz I2C u otro medio visual simple.
- Opera con batería recargable y está pensado para uso en interiores o invernaderos.

No incluye producción en masa, análisis de nutrientes del suelo, conectividad remota (nube o apps móviles), integración con maquinaria agrícola pesada ni un análisis económico-financiero detallado de impacto a largo plazo.

## Arquitectura del sistema

Principales subsistemas:

- **Sensado:** DHT11 para temperatura y humedad del aire, sensor capacitivo para humedad del suelo.
- **Procesamiento:** microcontrolador (Arduino/ESP32) que ejecuta la lógica de la red neuronal y las reglas de decisión.
- **Interfaz:** pantalla LCD 20x4 (I2C) y elementos visuales para mostrar estados y recomendaciones.
- **Energía:** batería recargable, con posible integración futura de energía solar.
- **Carcasa:** estructura diseñada e impresa en 3D (PLA u otros plásticos reciclables) para protección y ergonomía.

## Tecnologías y conceptos clave

- Microcontrolador Arduino/ESP32 y desarrollo en C/C++ con soporte para librerías de IA embebida (por ejemplo, TensorFlow Lite).
- Redes neuronales simples entrenadas en Python (scikit-learn, TensorFlow o Keras) y optimizadas para ejecución en dispositivos de recursos limitados.
- Procesamiento básico de señales: filtrado, promedio móvil, normalización y umbrales para interpretación de datos de sensores.
- Conceptos de agronomía para definir rangos de temperatura y humedad apropiados para fresa y lechuga, y relacionarlos con riesgos de enfermedades fúngicas.

## Viabilidad y mercado

- Viabilidad técnica: el sistema se enfoca en variables ambientales esenciales para productividad de fresa y lechuga, usando sensores y tecnologías disponibles en el mercado colombiano.
- Mercado objetivo: pequeños y medianos productores de fresa y lechuga en Boyacá y Cundinamarca que enfrentan barreras económicas, educativas y de conectividad para adoptar tecnologías avanzadas.
- Propuesta de valor: dispositivo compacto, económico y con interfaz visual clara que interpreta datos mediante inteligencia artificial para reducir pérdidas y mejorar prácticas de riego.
- Costos estimados del prototipo: alrededor de 167 000 COP considerando batería, sensores, almacenamiento y componentes electrónicos básicos.
- Punto de equilibrio estimado: venta aproximada de 80 unidades, con un costo por unidad de alrededor de 250 000 COP.

## Normativa y sostenibilidad

El diseño tiene en cuenta normativas como RETIE, NTC 2050, resolución ICA 30021, lineamientos de Buenas Prácticas Agrícolas y otras regulaciones relacionadas con seguridad eléctrica, uso de agua y buenas prácticas agrícolas. Asimismo, incorpora medidas para reducir impacto ambiental mediante reciclaje de plásticos, uso de baterías recargables y gestión responsable de residuos electrónicos.

## Estado actual del proyecto

Al cierre del informe se cuenta con:

- Prototipo físico ensamblado con sensores, microcontrolador y carcasa 3D.
- Código fuente funcional para lectura de sensores y procesamiento mediante una red neuronal básica.
- Documentación técnica, informe de desarrollo y resultados de pruebas preliminares en entorno controlado.
- Retroalimentación inicial de usuarios rurales que destacan facilidad de uso y utilidad para optimizar riego.