import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

structure = [4, 10, 1]

fig, ax = plt.subplots()

for i, layer in enumerate(structure):
    for j in range(layer):
        ax.add_artist(plt.Circle((i, j), radius=0.35, fc='w'))
        ax.text(i, j, f'{i}, {j}', ha='center', va='center')

for i, layer in enumerate(structure[:-1]):
    for j in range(layer):
        for k in range(structure[i+1]):
            ax.add_line(Line2D([i+0.5, i+1.5], [j, k]))

ax.set_xlim(-0.5, len(structure)-0.5)
ax.set_ylim(-0.5, max(structure)-0.5)
ax.set_xticks(range(len(structure)))
ax.set_yticks(range(max(structure)))
ax.set_xlabel('Layer')
ax.set_ylabel('Node')
plt.show()
