import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Definindo o sinal original
t = np.linspace(0, 20, 20000)  # Tempo de 0 a 20 segundos com 1 kHz de taxa de amostragem
y = 10 * np.sin(600 * np.pi * t) + 2 * np.sin(100 * np.pi * t) + 6 * np.cos(500 * np.pi * t)

# Definindo os parâmetros do filtro passa-baixa
f_corte = 650  # Frequência de corte em rad/s
w_corte = f_corte / (2 * np.pi)  # Frequência de corte em Hz

# Projetando o filtro passa-baixa digital
b, a = signal.butter(4, w_corte, btype='low', analog=False, fs=1000)

# Aplicando o filtro ao sinal
y_filtrado = signal.lfilter(b, a, y)

# Calculando a Transformada de Fourier do sinal filtrado
fft_y_filtrado = np.fft.fft(y_filtrado)
freq = np.fft.fftfreq(len(y_filtrado), d=1/1000)  # Frequências correspondentes à FFT

# Espectro de magnitude do sinal filtrado
magnitude_filtrado = np.abs(fft_y_filtrado)
magnitude_db_filtrado = 20 * np.log10(magnitude_filtrado)  # Convertendo para dB

# Espectro de fase do sinal filtrado
phase_filtrado = np.angle(fft_y_filtrado)

# Plotando o espectro de magnitude do sinal filtrado
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(freq, magnitude_db_filtrado)
plt.title('Espectro de Magnitude do Sinal Filtrado')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid()

# Plotando o espectro de fase do sinal filtrado
plt.subplot(2, 1, 2)
plt.plot(freq, phase_filtrado)
plt.title('Espectro de Fase do Sinal Filtrado')
plt.xlabel('Frequência (Hz)')
plt.ylabel('Fase (rad)')
plt.grid()

plt.tight_layout()
plt.show()