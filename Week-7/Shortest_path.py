'''Question- Given a directed graph with two vertices ( source and destination). 
             Design an algorithm and implement it using a program to find
             the weight of the shortest path from source to destination with exactly k edges on the path.'''

INF = float('inf')

def shortest_path_k_edges(graph, u, v, k):

    # Base cases
    if k == 0 and u == v:
        return 0

    if k == 1 and graph[u][v] != 0:
        return graph[u][v]

    if k <= 0:
        return INF

    ans = INF

    # Try all intermediate vertices
    for i in range(len(graph)):

        if graph[u][i] != 0:

            rec_ans = shortest_path_k_edges(graph, i, v, k - 1)

            if rec_ans != INF:

                ans = min(ans, graph[u][i] + rec_ans)

    return ans


# ---------------- INPUT ----------------

V = int(input())

graph = []

for _ in range(V):
    graph.append(list(map(int, input().split())))

u, v = map(int, input().split())

k = int(input())

result = shortest_path_k_edges(graph, u - 1, v - 1, k)

if result == INF:
    print("No path of length", k, "is available")
else:
    print("Weight of shortest path =", result)