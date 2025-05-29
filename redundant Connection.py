from collections import deque

def find_redundant_edge(connections):
    size = len(connections)
    adj_list = [[] for _ in range(size + 1)]
    degree = [0] * (size + 1)

    for a, b in connections:
        adj_list[a].append(b)
        adj_list[b].append(a)
        degree[a] += 1
        degree[b] += 1

    q = deque(i for i in range(1, size + 1) if degree[i] == 1)

    while q:
        node = q.popleft()
        degree[node] = 0
        for neighbor in adj_list[node]:
            if degree[neighbor] > 0:
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    q.append(neighbor)

    for a, b in connections:
        if degree[a] > 0 and degree[b] > 0:
            return [a, b]


connections = [[10, 20], [20, 30], [30, 40], [10, 40], [10, 50]]
print(find_redundant_edge(connections)) 
