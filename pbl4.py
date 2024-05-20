import numpy as np
import matplotlib.pyplot as plt

# Matriz de transição
P = np.array([
    [0.8, 0.25, 0.4],
    [0.15, 0.6, 0.3],
    [0.05, 0.15, 0.3]
])

# Vetor de estado inicial (estoque inicial)
estado_inicial = np.array([96, 48, 48])

# Função para calcular os estados semanais
def calcular_estados_semanas(P, estado_inicial, semanas):
    estados = [estado_inicial]
    for _ in range(semanas):
        novo_estado = P @ estados[-1]
        estados.append(novo_estado)
    return np.array(estados)

# Calcular os estados para 4 semanas
semanas = 4
estados = calcular_estados_semanas(P, estado_inicial, semanas)

# Preparar dados para tabela e gráfico
marcas = ['Tio Jorge', 'Camil', 'Prato Fino']
semana_labels = ['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4', 'Semana 5']

# Criar a figura e os subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Criar a tabela no primeiro subplot
ax1.axis('tight')
ax1.axis('off')
tabela = ax1.table(
    cellText=np.round(estados, 2),
    rowLabels=semana_labels,
    colLabels=marcas,
    cellLoc='center',
    loc='center'
)
tabela.auto_set_font_size(False)
tabela.set_fontsize(10)
tabela.scale(1.2, 1.2)

# Criar o gráfico no segundo subplot
for i in range(estados.shape[1]):
    ax2.plot(semana_labels, estados[:, i], marker='o', label=marcas[i])
ax2.set_xlabel('Semanas')
ax2.set_ylabel('Unidades Consumidas')
ax2.set_title('Consumo de Arroz por Semana')
ax2.legend()
ax2.grid(True)

# Ajustar o layout para que não haja sobreposição
plt.tight_layout()
plt.show()
