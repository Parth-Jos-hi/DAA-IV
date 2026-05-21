'''Question:- Design and implement an algorithm to find the maximum budget required to connect 
              all cities such that total spanning weight is maximum.'''

def find(parent, i):

    if parent[i] == i:
        return i

    return find(parent, parent[i])


def union(parent, x, y):

    parent[find(parent, x)] = find(parent, y)


def maximum_spanning_tree(graph, V):

    edges = []

    for i in range(V):

        for j in range(i + 1, V):

            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    # Sort in descending order
    edges.sort(reverse=True)

    parent = [i for i in range(V)]

    total_weight = 0

    for weight, u, v in edges:

        if find(parent, u) != find(parent, v):

            union(parent, u, v)

            total_weight += weight

    print("Maximum Spanning Weight:", total_weight)


# DRIVER
V = int(input())

graph = []

for _ in range(V):
    graph.append(list(map(int, input().split())))

maximum_spanning_tree(graph, V)