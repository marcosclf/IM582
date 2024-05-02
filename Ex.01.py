# Bibliotecas utilizadas no VSC
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Dados da tabela 1 dada no exercicio 01 da lista I
dados = """
0; 39.20
10; 90.80
20; 118.36
30; 168.80
40; 160.96
50; 224.64
60; 261.88
70; 272.92
80; 350.12
90; 363.88
100; 453.28
"""

# Obtendo a separacao de deslocamento e tensoes
linhas = dados.strip().split('\n')
deslocamento = np.array([float(linha.split(';')[0]) for linha in linhas])
tensao = np.array([float(linha.split(';')[1].replace(',', '.')) for linha in linhas])

# Regressão linear utilizando a biblioteca SciPy
slope, intercept, r_value, p_value, std_err = linregress(deslocamento, tensao)

# Plot da reta e pontos (Ajuste de cores da reta e pontos)
plt.scatter(deslocamento, tensao, color='navy', label='Dados')
plt.plot(deslocamento, slope * deslocamento + intercept, 'r', color='black', label='Y = m . x + b')
plt.xlabel('Deslocamento (mm)')
plt.ylabel('Tensão (mV)')
plt.title('Ensaio de calibração estática (Conforme tabela 1)')
plt.legend()
plt.grid(True)
plt.show()

# Calculo da sensibilidade e da faixa de entrada / saida
sensibilidade = slope
print(f"Sensibilidade: {sensibilidade:.2f} mV/mm")
faixa_dinamica_entrada = max(deslocamento) - min(deslocamento)
print(f"Faixa dinâmica de entrada: {faixa_dinamica_entrada} mm")
faixa_dinamica_saida = max(tensao) - min(tensao)
print(f"Faixa dinâmica de saída: {faixa_dinamica_saida} mV")

# Resolucao (unidade mV e mm)
resolucao = 1 / sensibilidade
print(f"Resolução: {resolucao:.2f} mm")