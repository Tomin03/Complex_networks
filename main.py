import networkx as nx

network = nx.read_weighted_edgelist('bio-DM-LC.edges')

nodes = list(network.nodes())
# print(nodes)
edges = list(network.edges())
# print(edges)




