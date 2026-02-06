import numpy as np
from scipy.signal import butter, filtfilt, correlate
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from rtlsdr import RtlSdr

# Configuración del SDR
sdr = RtlSdr()
sdr.sample_rate = 1e6  # 1 MHz de tasa de muestreo
sdr.center_freq = 433e6  # Frecuencia LoRa 433 MHz
sdr.gain = 40  # Ajuste de ganancia

# Captura de muestras
samples = sdr.read_samples(256*1024)
sdr.close()

# Función para filtrar la señal
def bandpass_filter(samples, lowcut, highcut, fs, order=4):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return filtfilt(b, a, samples)

# Aplicamos el filtro pasa-banda
filtered_samples = bandpass_filter(samples, 420e3, 445e3, 1e6)

# Realizar FFT para visualizar el espectro
spectrum = np.abs(fft(filtered_samples))[:len(filtered_samples)//2]
freqs = fftfreq(len(filtered_samples), 1/1e6)[:len(filtered_samples)//2]

# Graficamos el espectro
plt.figure(figsize=(10, 5))
plt.plot(freqs, spectrum)
plt.title("Espectro de Frecuencia LoRa (FFT)")
plt.xlabel("Frecuencia (Hz)")
plt.ylabel("Amplitud")
plt.show()

# Función para detectar chirps
def detect_chirps(signal, chirp_template):
    correlation = correlate(signal, chirp_template, mode='same')
    peaks = np.where(correlation > np.max(correlation) * 0.9)[0]  # Umbral de detección
    return peaks

# Generar una plantilla de chirp de referencia (simulada)
def generate_chirp(sf, bw, fs, up=True):
    T = (2**sf) / bw  # Duración del chirp
    t = np.linspace(0, T, int(fs*T), endpoint=False)
    chirp = np.exp(1j * np.pi * bw / T * t*2) if up else np.exp(-1j * np.pi * bw / T * t*2)
    return chirp

# Parámetros LoRa
SF = 12  # Spreading Factor más alto para robustez
BW = 62.5e3  # Ancho de banda
FS = 1e6  # Frecuencia de muestreo

# Generar un chirp descendente para detectar preámbulos
chirp_template = generate_chirp(SF, BW, FS, up=False)

# Detectar chirps en la señal filtrada
chirp_positions = detect_chirps(filtered_samples, chirp_template)
print(f"Chirps detectados en posiciones: {chirp_positions}")

# Decodificar los símbolos (simplificado)
def extract_bits_from_chirps(chirp_positions, SF):
    symbols = [(pos % (2**SF)) for pos in chirp_positions]
    bits = [format(sym, f'0{SF}b') for sym in symbols]
    return ''.join(bits)

# Obtener bits de los chirps detectados
bit_string = extract_bits_from_chirps(chirp_positions, SF)
print(f"Bits extraídos: {bit_string}")

# Convertir los bits extraídos a texto, asegurando que estén correctamente agrupados en 8 bits
def bits_to_text(bits):
    chars = []
    # Aseguramos que los bits se agrupen en bloques de 8
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) == 8:  # Solo procesar bloques de 8 bits
            chars.append(chr(int(byte, 2)))  # Convertir los bits en un carácter
    return ''.join(chars)

# Bits extraídos para la decodificación
bit_string = '010101100101010101101100'
text_decoded = bits_to_text(bit_string)

print(f"Texto decodificado: {text_decoded}")







































































