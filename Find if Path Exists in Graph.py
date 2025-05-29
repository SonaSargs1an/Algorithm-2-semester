def find(edges, n, source, destination, visited=None):
    if visited is None:
        visited = set()

    graph = {i: [] for i in range(n)}
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    if source not in visited:
        print(source)
        visited.add(source)
        for neighbor in graph[source]:
            if neighbor == destination:
                return True
            if find(edges, n, neighbor, destination, visited):
                return True
    return False


edges = [[10, 11], [11, 12], [12, 10]]
n = 4
source = 10
destination = 12
print(f"ex 1 = {find(edges, n, source, destination)}")  


edges_2 = [[21, 22], [21, 23], [30, 32], [32, 31], [31, 30]]
n_2 = 33
source_2 = 21
destination_2 = 32
print(f"ex 2 = {find(edges_2, n_2, source_2, destination_2)}") 