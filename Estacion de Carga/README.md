# Estación de Carga Basada en Resonancia RLC

Proyecto de laboratorio para diseñar, simular, construir y analizar una estación de carga de baja potencia basada en un circuito RLC resonante, orientada a transferencia de energía (alámbrica/inalámbrica) mediante acoplamiento magnético.

## Descripción general

El proyecto desarrolla una fuente resonante utilizando un circuito RLC en serie con una bobina construida a medida, optimizada en frecuencia y factor de calidad para maximizar la transferencia de energía en resonancia.  
Se realiza análisis teórico (transitorio, frecuencia y estado estacionario), mediciones experimentales (osciloscopio, VNA básico con métodos indirectos) y comparación con simulaciones para validar el comportamiento del circuito.

## Objetivos

- Diseñar una fuente resonante mediante un circuito RLC.
- Caracterizar:
  - Respuesta transitoria.
  - Respuesta en frecuencia (diagramas de Bode).
  - Relaciones tensión–corriente en estado estacionario.
- Diseñar, construir y caracterizar la bobina principal (inductancia y resistencia serie).
- Evaluar el desempeño de la fuente resonante, con énfasis en el factor de calidad \(Q\) y su impacto en la transferencia de energía.

## Fundamentos teóricos clave

- Corriente alterna (AC) y su representación fasorial.
- Bobinas/inductores:
  - Almacenamiento de energía en campo magnético.
  - Cálculo práctico de inductancia mediante circuito LC resonante.
- Circuito RLC:
  - Configuraciones serie y paralelo.
  - Ecuaciones diferenciales de segundo orden (respuesta sub/sobre/criticamente amortiguada).
  - Resonancia \( \omega_0 = 1/\sqrt{LC} \).
- Transferencia de energía con bobinas acopladas:
  - Factor de acoplamiento \(k\) (0–1).
  - Factor de calidad \(Q\) como medida de selectividad/eficiencia.
- Herramientas de análisis:
  - Función de transferencia \(H(s)\).
  - Diagramas de Bode (magnitud y fase).
  - Teoremas de valor inicial y final (Laplace).
  - Análisis fasorial y en polares.

## Diseño y simulación

1. **Diseño de bobinas**
   - Se construyeron y caracterizaron dos bobinas:
     - Bobina plana (cobre calibre 12, ~10 m, L ≈ 94 µH con C = 0,1 µF, f ≈ 52 kHz).
     - Bobina solenoide (cobre calibre 22, ~20 m, L ≈ 0,7 mH con C = 47 µF, f ≈ 830 Hz).
   - Se seleccionó la bobina solenoide (L ≈ 0,7 mH) por su mayor inductancia y mejor control sobre la resonancia.

2. **Selección de capacitancia y topología**
   - Se evaluaron capacitancias típicas (10 µF … 10 pF) para observar cómo cambia la frecuencia de resonancia.
   - Se compararon configuraciones RLC en serie y en paralelo mediante diagramas de Bode:
     - Para C = 10 nF y L = 0,7 mH en serie se obtuvo:
       - Frecuencia de resonancia ≈ 60 kHz.
       - Pico de magnitud ≈ 20 dB.
       - Factor de calidad \(Q ≈ 5\).
   - Se eligió un circuito RLC en **serie** con:
     - L ≈ 0,7 mH.
     - C = 10 nF.
     - R_total ≈ 52 Ω (fuente + resistencia del inductor).

3. **Parámetros clave de diseño (teóricos)**
   - \( f_0 ≈ 60,15\ \text{kHz} \).
   - \( \omega_0 ≈ 3,78 \times 10^5\ \text{rad/s} \).
   - Constante de tiempo aproximada \( \tau ≈ 13,5\ \mu s \).
   - Factor de calidad \( Q ≈ 5,1 \).

## Análisis del circuito

### Respuesta transitoria

- Se analizó el circuito RLC serie con excitación tipo escalón/pulso.
- A partir de la ecuación diferencial de segundo orden se obtuvieron:
  - Frecuencia natural.
  - Amortiguamiento natural.
  - Constante de tiempo.
- Simulación y medición experimental mostraron buena correspondencia:
  - \(\tau\) teórico ≈ 13,46 µs; medido ≈ 13,8 µs.
  - \(Q\) teórico ≈ 5,09; medido ≈ 5,28.

### Respuesta en frecuencia

- Se obtuvo la función de transferencia \(H(s)\) con entrada el voltaje de la fuente y salida la corriente por el inductor.
- Diagramas de Bode (simulación y medición):
  - Pico de magnitud cercano a 60 kHz.
  - Fase de la corriente prácticamente 0° en resonancia (en serie, Z es casi puramente resistiva).
- Experimentalmente se midió corriente y voltaje para 30–120 kHz con osciloscopio + pinza amperimétrica y se construyó el Bode con:
  - \(20 \log_{10}(|I_{\text{out}}/V_{\text{in}}|)\) y \(20 \log_{10}(|V_L/V_{\text{in}}|)\).

### Estado estacionario

- Para una excitación senoidal \(V_{\text{in}} = 10\ \text{Vp}\) a \(f_0\) y fase 0:
  - Corriente en régimen: amplitud ≈ 0,19 A.
  - Voltaje en el inductor y el capacitor con magnitudes elevadas (por la resonancia) y desfases ±90° respecto a la corriente.
- Se verificó:
  - Relación I–V en cada elemento.
  - Diagramas fasoriales (inductor y capacitor desfasados ±90° respecto a la corriente).

## Validación experimental

- **Caracterización de L** con circuito LC paralelo y medición de la frecuencia de oscilación en el osciloscopio (C = 47 µF, f ≈ 830 Hz → L ≈ 0,7 mH).
- **Respuesta transitoria** medida con excitación cuadrada de 50 Hz y osciloscopio:
  - Se estimaron periodo de oscilación y tiempo de amortiguamiento.
- **Bode experimental**:
  - Medición de I y V_L en rango 30–120 kHz.
  - Máximo alrededor de 60 kHz, compatible con el diseño.
- **Comparación simulación vs. medición**:
  - Diferencias razonables atribuibles a:
    - Resistencias parásitas no modeladas.
    - Precisión limitada de la pinza de corriente y del osciloscopio.
    - Tolerancias de L y C.

## Conclusiones clave

- Se diseñó y construyó exitosamente una fuente resonante RLC serie con bobina en serie, adecuada como base para una estación de carga de baja potencia.
- La respuesta transitoria, en frecuencia y en estado estacionario del circuito se ajusta bien a los modelos teóricos y simulaciones.
- La bobina construida cumple con los parámetros de inductancia y resistencia previstos, permitiendo una transferencia de energía eficiente en la frecuencia de diseño.
- El factor de calidad \(Q\) obtenido fue ligeramente inferior al ideal, pero suficiente para validar el concepto y la viabilidad de la estación de carga en aplicaciones de baja potencia.
- El proyecto sienta las bases para futuros desarrollos de transferencia de energía inalámbrica mediante acoplamiento magnético (p.ej. cargadores inalámbricos simples, prototipos de WPT).