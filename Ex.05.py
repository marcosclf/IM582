import numpy as np
import matplotlib.pyplot as plt

# Dados fornecidos
V = 24  # Tensão em volts
correntes_mA = np.array([9.0, 9.0, 8.8, 8.9, 8.8])  # Corrente em mA
correntes_A = correntes_mA / 1000  # Convertendo corrente para amperes

# Calculando resistências individuais
resistencias = V / correntes_A

# Média das resistências
R_medio = np.mean(resistencias)

# Incerteza na tensão
u_V = 0.01  # Incerteza na tensão em volts

# Incerteza na corrente
u_I = np.sqrt((0.001)**2 + (0.02 * correntes_A)**2)

# Incerteza combinada na resistência usando a propagação de incertezas
u_R = resistencias * np.sqrt((u_V/V)**2 + (u_I/correntes_A)**2)

# Média das incertezas das resistências para uma estimativa mais geral
u_R_medio = np.mean(u_R)

# Incerteza expandida (95% de confiança, fator de cobertura k ≈ 2)
U_R = 2 * u_R_medio

# Criando gráficos
plt.figure(figsize=(10, 5))

# Gráfico das resistências individuais com barras de erro
plt.errorbar(range(len(resistencias)), resistencias, yerr=u_R, fmt='o', capsize=5, label='Resistência com Incerteza')
plt.axhline(R_medio, color='r', linestyle='--', label=f'Resistência Média = {R_medio:.2f} Ω')
plt.title('Resistências Calculadas com Incertezas')
plt.xlabel('Medições')
plt.ylabel('Resistência (Ω)')
plt.legend()
plt.grid(True)

plt.show()