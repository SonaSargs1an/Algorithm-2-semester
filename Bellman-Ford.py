def bellman_ford(vertices, edges, source):
    dist = {v: float('inf') for v in vertices}
    dist[source] = 0

    for _ in range(len(vertices) - 1):
        updated = False
        for u, v, weight in edges:
            if dist[u] + weight < dist[v]:
                dist[v] = dist[u] + weight
                updated = True
        if not updated:
            break

    for u, v, weight in edges:
        if dist[u] + weight < dist[v]:
            print("Graph contains a negative cycle")
            return None

    return dist

edges = [
    ('A', 'B', 3),
    ('A', 'C', 6),
    ('B', 'D', 1),
    ('D', 'C', 1),
    ('D', 'E', 3),
    ('E', 'F', 4),
    ('F', 'C', 8),
    ('C', 'E', -2)
]

vertices = {u for u, v, _ in edges} | {v for u, v, _ in edges}

source = 'A'
distances = bellman_ford(vertices, edges, source)

if distances:
    print(f"Shortest distances from {source}:")
    for vertex, distance in distances.items():
        print(f"{vertex}\t\t{distance}")