import heapq

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
