import numpy as np
import matplotlib.pyplot as plt

# Definindo o sinal
t = np.linspace(0, 20, 20000)  # Tempo de 0 a 20 segundos com 1 kHz de taxa de amostragem
y = 10 * np.sin(600 * np.pi * t) + 2 * np.sin(100 * np.pi * t) + 6 * np.cos(500 * np.pi * t)

# Calculando a Transformada de Fourier Discreta (FFT)
fft_y = np.fft.fft(y)
freq = np.fft.fftfreq(len(y), d=1/1000)  # Frequências correspondentes à FFT

# Espectro de magnitude
magnitude = np.abs(fft_y)
magnitude_db = 20 * np.log10(magnitude)  # Convertendo para dB

# Espectro de fase
phase = np.angle(fft_y)

# Plotando o espectro de magnitude
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(freq, magnitude_db)
plt.title('Espectro de Magnitude')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()

# Plotando o espectro de fase
plt.subplot(2, 1, 2)
plt.plot(freq, phase)
plt.title('Espectro de Fase')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (rad)')
plt.grid()

plt.tight_layout()
plt.show()

# Faixa dinâmica da FFT
dynamic_range = np.max(magnitude_db) - np.min(magnitude_db)
print("Faixa dinâmica da FFT:", dynamic_range, "dB")

# Resolução espectral da FFT
resolution = freq[1] - freq[0]
print("Resolução espectral da FFT:", resolution, "Hz")
