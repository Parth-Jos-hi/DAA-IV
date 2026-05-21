'''Question:-

Assume that a road construction project is given where cities are represented as vertices and roads as weighted edges.
Design and implement Prim's Algorithm to find the minimum cost required to connect all cities such that:

All cities are connected
Total cost is minimum
Only V-1 roads are used

Output the minimum spanning weight.'''

INF = float('inf')

def prim_mst(graph, V):

    selected = [False] * V
    selected[0] = True

    edge_count = 0
    total_weight = 0

    while edge_count < V - 1:

        minimum = INF
        x = 0
        y = 0

        for i in range(V):

            if selected[i]:

                for j in range(V):

                    if not selected[j] and graph[i][j] != 0:

                        if graph[i][j] < minimum:

                            minimum = graph[i][j]
                            x = i
                            y = j

        total_weight += graph[x][y]

        selected[y] = True
        edge_count += 1

    print("Minimum Spanning Weight:", total_weight)


# DRIVER
V = int(input())

graph = []

for _ in range(V):
    graph.append(list(map(int, input().split())))

prim_mst(graph, V)