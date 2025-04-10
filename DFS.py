def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            print(node)
            visited.add(node)
            stack.extend(reversed(graph[node]))

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
print("DFS traversal (Iterative) starting from your input node:")
dfs_iterative(graph, first_node)