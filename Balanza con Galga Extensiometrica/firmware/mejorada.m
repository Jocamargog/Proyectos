% === Conexión con Arduino ===
a = arduino('COM13', 'Uno');  % Cambia a tu puerto correcto

% === Crear figura de interfaz ===
fig = figure('Name', 'Monitor de Peso en Tiempo Real', 'NumberTitle', 'off', ...
             'CloseRequestFcn', @cerrarApp, 'Position', [100, 100, 800, 400]);

% === Gráfica de voltaje en tiempo real ===
subplot(1,2,1)
hLine = animatedline('Color', 'b', 'LineWidth', 2);
xlabel('Tiempo (s)');
ylabel('Voltaje (V)');
title('Lectura de Voltaje');
grid on;
axis([0 60 0 5]);  % Ajusta el eje según esperes los valores
hold on;

% === Gráfica de barra de peso ===
subplot(1,2,2)
hBar = bar(0, 'FaceColor', [0.2 0.7 0.3]);
ylabel('Masa (g)');
title('Peso Estimado');
ylim([0 1100]);  % Hasta 1000 g con margen
set(gca, 'XTick', []);

% === Texto de masa calculada ===
txt = uicontrol('Style', 'text', 'Position', [300 20 200 40], ...
                'FontSize', 14, 'String', 'Masa: 0 g');

% === Timer para actualizar cada 0.1 segundos ===
global t
t = timer('ExecutionMode','fixedRate','Period',0.1, ...
          'TimerFcn', @leerDatos);
start(t);

% === Variables globales para tiempo acumulado ===
global tiempoAcumulado startTime
tiempoAcumulado = 0;
startTime = tic;

% === Función para leer datos y actualizar GUI ===
function leerDatos(~, ~)
    global a hLine hBar txt tiempoAcumulado startTime

    V = readVoltage(a, 'A0');             % Lectura de voltaje
    masa = 0.005 * V + 0.0152;            % Cálculo de masa (revisa ecuación si usas otra)

    tActual = toc(startTime);
    tiempoAcumulado = [tiempoAcumulado, tActual];

    % Actualizar gráfica de línea
    addpoints(hLine, tActual, V);
    drawnow limitrate;

    % Actualizar barra de peso
    hBar.YData = masa * 1000;   % Convertir a gramos si masa está en kg

    % Actualizar texto
    set(txt, 'String', sprintf('Masa: %.2f g', masa * 1000));
end

% === Función para cerrar la app limpiamente ===
function cerrarApp(~, ~)
    global t fig a
    if isvalid(t)
        stop(t);
        delete(t);
    end
    clear a
    instrreset
    delete(fig);
end
