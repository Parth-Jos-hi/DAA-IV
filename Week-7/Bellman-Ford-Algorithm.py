'''Question- Given a weighted graph, design and implement an algorithm using Bellman-Ford Algorithm to
             find the shortest path from a source vertex to a destination vertex.
             Also check for Negative Cycle '''

INF = float('inf')

def bellman_ford(graph, V, source):

    # Step 1: Initialize distances
    dist = [INF] * V
    dist[source] = 0

    # Step 2: Relax all edges V-1 times
    for _ in range(V - 1):

        for u in range(V):

            for v in range(V):

                weight = graph[u][v]

                # Check edge exists and source reachable
                if weight != 0 and dist[u] != INF:

                    # Relaxation
                    if dist[u] + weight < dist[v]:
                        dist[v] = dist[u] + weight

    # Step 3: Check for Negative Weight Cycle
    for u in range(V):

        for v in range(V):

            weight = graph[u][v]

            if weight != 0 and dist[u] != INF:

                # If relaxation still possible
                if dist[u] + weight < dist[v]:
                    print("Negative Weight Cycle Exists")
                    return

    # Step 4: Print shortest distances
    print("Shortest distances from source:", source)

    for i in range(V):

        if dist[i] == INF:
            print(f"{source} -> {i} = No Path")

        else:
            print(f"{source} -> {i} = {dist[i]}")


# ---------------- DRIVER CODE ----------------

V = int(input("Enter number of vertices: "))

print("Enter adjacency matrix:")

graph = []

for _ in range(V):
    graph.append(list(map(int, input().split())))

source = int(input("Enter source vertex: "))

bellman_ford(graph, V, source)