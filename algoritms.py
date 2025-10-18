import heapq
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

def dijkstra(graph, source, target=None):

    distances = {node: float('inf') for node in graph.nodes()}
    distances[source] = 0
    previous = {node: None for node in graph.nodes()}
    queue = [(0, source)]

    while queue:
        # Ustalamy kopiec jako kolejke priorytetową, która bedzie zwracała najmniejszą wartość
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        if target is not None and current_node == target:
            break

        for neighbor, data in graph[current_node].items():
            weight = data.get('weight')
            distance = current_distance + weight
            # Relaksacja
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    if target is not None:
        path = []
        current = target
        while current is not None:
            path.insert(0, current)
            current = previous[current]
        if distances[target] == float('inf'):
            return None
        return path, distances[target]

    return distances, previous

def create_subgraph(graph, start, end):
    list_of_nodes = [str(i) for i in range(int(start), int(end)+1)]
    subgraph = nx.subgraph(graph, list_of_nodes).copy()
    return subgraph

def czy_spojny(graph):
    return nx.is_connected(graph)

def even_conncections(graph):
    all_even = all(d % 2 == 0 for n, d in graph.degree())
    return all_even

def visualise_graph(graph):
    np.random.seed(20)
    pos_3d = {node: np.random.rand(3) for node in graph.nodes()}

    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    xs = [pos_3d[n][0] for n in graph.nodes()]
    ys = [pos_3d[n][1] for n in graph.nodes()]
    zs = [pos_3d[n][2] for n in graph.nodes()]
    ax.scatter(xs, ys, zs, s=100, c='skyblue')

    for u, v in graph.edges():
        x = [pos_3d[u][0], pos_3d[v][0]]
        y = [pos_3d[u][1], pos_3d[v][1]]
        z = [pos_3d[u][2], pos_3d[v][2]]
        ax.plot(x, y, z, c='gray', alpha=0.9)

    for node, (x, y, z) in pos_3d.items():
        ax.text(x, y, z, str(node), fontsize=9, color='black')

    plt.title("Podgraf w 3D")
    plt.show()



def find_augmenting_path(G, source, sink):
    parent = {node: None for node in G.nodes}
    visited = {node: False for node in G.nodes}
    visited[source] = True
    changed = True

    while changed:
        changed = False
        for u in G.nodes:
            if visited[u]:
                for v in G.successors(u):
                    capacity = G[u][v].get('weight', 0)
                    if capacity > 0 and not visited[v]:
                        visited[v] = True
                        parent[v] = u
                        changed = True
                        if v == sink:
                            # Odtworzenie ścieżki
                            path = []
                            current = sink
                            while current != source:
                                path.insert(0, (parent[current], current))
                                current = parent[current]
                            return path
    return None

def ford_fulkerson(G, source, sink):
    # Tworzymy kopię grafu jako graf resztkowy
    residual = nx.DiGraph()
    for u, v, data in G.edges(data=True):
        residual.add_edge(u, v, weight=data.get('weight', 0))
        if not residual.has_edge(v, u):
            residual.add_edge(v, u, weight=0)
    max_flow = 0
    while True:
        path = find_augmenting_path(residual, source, sink)
        if not path:
            break
        # Znajdź minimalną pojemność w ścieżce
        path_flow = min(residual[u][v]['weight'] for u, v in path)
        # Zaktualizuj graf resztkowy
        for u, v in path:
            residual[u][v]['weight'] -= path_flow
            residual[v][u]['weight'] += path_flow
        max_flow += path_flow

    return max_flow