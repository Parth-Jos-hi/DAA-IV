'''Question:- Implement the previous road construction problem using Kruskal's Algorithm to find the minimum spanning weight.'''

def find(parent, i):

    if parent[i] == i:
        return i

    return find(parent, parent[i])


def union(parent, x, y):

    parent[find(parent, x)] = find(parent, y)


def kruskal(graph, V):

    edges = []

    for i in range(V):

        for j in range(i + 1, V):

            if graph[i][j] != 0:
                edges.append((graph[i][j], i, j))

    edges.sort()

    parent = [i for i in range(V)]

    mst_weight = 0

    for weight, u, v in edges:

        if find(parent, u) != find(parent, v):

            union(parent, u, v)

            mst_weight += weight

    print("Minimum Spanning Weight:", mst_weight)


# DRIVER
V = int(input())

graph = []

for _ in range(V):
    graph.append(list(map(int, input().split())))

kruskal(graph, V) 