import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Temperaturas da tabela 2
leituras_temperatura = np.array([69.6, 69.8, 68.2, 71.4, 70.1, 68.7, 74.6, 65.9, 67.3, 68.1])
media_temp = np.mean(leituras_temperatura)
std_temp = np.std(leituras_temperatura, ddof=1)
n = len(leituras_temperatura)
intervalo_confianca = stats.t.interval(0.95, n-1, loc=media_temp, scale=std_temp/np.sqrt(n))

# Ajuste de cores do grafico
color_points = 'navy'  # Temperaturas
color_mean_line = 'black'  # Media
color_ci = 'lightgreen'  # Confiabilidade
color_outer_lines = 'black'  # Grade externa
color_inner_lines = 'lightgrey'  # Grade interna

# Condicoes do grafico
plt.figure(figsize=(10,5))
plt.rcParams['axes.edgecolor'] = color_outer_lines
plt.rcParams['axes.linewidth'] = 1.5
plt.rcParams['grid.color'] = color_inner_lines

# Plot dos pontos
plt.plot(leituras_temperatura, 'o', label='Temperaturas informadas', color=color_points)

# Plot da media
plt.hlines(media_temp, -1, len(leituras_temperatura), colors=color_mean_line, linewidth=2, label='Temperatura Média')

# Plot da faixa de confiabilidade em 95%
plt.fill_between([-1, len(leituras_temperatura)], intervalo_confianca[0], intervalo_confianca[1], color=color_ci, alpha=0.5, label='Faixa de Confiabilidade 95%')

# Titulos do grafico e dos eixos / inclui legenda conforme plots acima
plt.xticks(ticks=range(n), labels=range(1, n+1))
plt.xlim(-0.5, n-0.5)
plt.xlabel('Sequência da medida das temperaturas (Tabela 2)')
plt.ylim(65, 75)
plt.yticks(np.arange(65, 76, 1))  # Escala e faixa do eixo Y
plt.ylabel('Temperatura (°C)')
plt.title('Temperaturas informadas, média e intervalo de confiabilidade')
plt.legend()
plt.grid(True, linestyle='-')
plt.show()