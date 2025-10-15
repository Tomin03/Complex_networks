import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

network = nx.read_weighted_edgelist('bio-DM-LC.edges')

"""
#Wizualizacja sieci
np.random.seed(21)
pos_3d = {node: np.random.rand(3) for node in network.nodes()}

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

xs = [pos_3d[n][0] for n in network.nodes()]
ys = [pos_3d[n][1] for n in network.nodes()]
zs = [pos_3d[n][2] for n in network.nodes()]
ax.scatter(xs, ys, zs, s=100, c='skyblue', depthshade=True)

for u, v in network.edges():
    x = [pos_3d[u][0], pos_3d[v][0]]
    y = [pos_3d[u][1], pos_3d[v][1]]
    z = [pos_3d[u][2], pos_3d[v][2]]
    ax.plot(x, y, z, c='gray', alpha=0.7)

for node, (x, y, z) in pos_3d.items():
    ax.text(x, y, z, str(node), fontsize=9, color='black')
plt.show()
"""

# UI





