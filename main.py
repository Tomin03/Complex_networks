import networkx as nx
from algoritms import dijkstra, create_subgraph, czy_spojny, even_conncections, visualise_graph

network = nx.read_weighted_edgelist('bio-DM-LC.edges')

"""
# Zad 1
# UI
start = input('Podaj wierzchołek startowy (0-657) do znalezienia najkrótszej ścieżki: ')
end = input('Podaj wierzchołek końcowy (0-657) do znalezienia najkrótszej ścieżku: ')
shortest_path = dijkstra(network, start, end)
print('Najkrótsza ścieżka pomiędzy danymi wierzchołkami wynosi: ', shortest_path)
"""

"""
# Zad 2
start = input('Podaj wierzchołek startowy do stworzenia podgrafu: ')
end = input('Podaj wierzchołek końcowy do stworzenia podgrafu: ')
podgraf = create_subgraph(network, start, end)

# Sprawdzenie czy wybrany podgraf jest spójny
if czy_spojny(podgraf):
    print('Wybrany podgraf jest spójny')
else:
    print('Wybrany podgraf nie jest spójny')

# Sprawdzenie czy w wybranym podgrafie każdy wierzchołek ma parzystą liczbę połączeń
if even_conncections(podgraf):
    print('Każdy wierchołek ma parzystą liczbę połączeń')
else:
    print('Nie każdy wierzchołek ma parzystą liczbę połączeń')

#Sprawdzenie czy podgraf jest eulerowski
if czy_spojny(podgraf) and even_conncections(podgraf):
    print('Wybrany podgraf jest eulerowski')
else:
    print('Wybrany podgraf nie jest eulerowski')

# Wizualizacja
visualise_graph(podgraf)
"""