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

# Plotando o sinal original e o sinal filtrado
plt.figure(figsize=(10, 6))
plt.plot(t, y, label='Sinal Original')
plt.plot(t, y_filtrado, label='Sinal Filtrado')
plt.title('Sinal Original e Sinal Filtrado')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
