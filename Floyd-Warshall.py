def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

graph_adj = [
    [0, 7, float('inf'), 3, float('inf')],
    [7, 0, 5, 1, 2],
    [float('inf'), 5, 0, float('inf'), 3],
    [3, 1, float('inf'), 0, 6],
    [float('inf'), 2, 3, 6, 0]
]

shortest_paths = floyd_warshall(graph_adj)
for row in shortest_paths:
    print(row)