from collections import deque

graph = {
    0: [7, 9, 11],
    1: [],
    2: [12],
    3: [2, 4],
    4: [],
    5: [],
    6: [5],
    7: [6, 3, 11],
    8: [1, 12],
    9: [8, 10, 0],
    10: [1],
    11: [],
    12: [2]
}

first_node = int(input("Enter the first node: "))

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.append(node)
            queue.extend(neighbour for neighbour in graph[node] if neighbour not in visited)

print("BFS traversal starting from your input node:")
bfs(graph, first_node)