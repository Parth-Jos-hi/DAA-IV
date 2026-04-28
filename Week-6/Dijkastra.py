'''Question- Given a weighted graph, design and implement an algorithm using Dijkstra’s Algorithm to find
             the shortest path from a source vertex to a destination vertex.'''


import heapq

def dijkstra(graph, source):
    # Initialize distance and parent
    distance = {node: float('inf') for node in graph}
    parent = {node: None for node in graph}

    distance[source] = 0
    min_heap = [(0, source)]  # (distance, node)

    while min_heap:
        current_dist, current_node = heapq.heappop(min_heap)

        for neighbor, weight in graph[current_node]:
            new_dist = current_dist + weight

            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                parent[neighbor] = current_node
                heapq.heappush(min_heap, (new_dist, neighbor))

    return distance, parent


def reconstruct_path(parent, destination):
    path = []
    while destination is not None:
        path.append(destination)
        destination = parent[destination]
    return path[::-1]


# -------- Driver Code --------
def main():
    graph = {}

    n = int(input("Enter number of nodes: "))
    for _ in range(n):
        node = input("Enter node name: ")
        graph[node] = []

    e = int(input("Enter number of edges: "))
    for _ in range(e):
        u = input("From: ")
        v = input("To: ")
        w = int(input("Weight: "))

        graph[u].append((v, w))
        graph[v].append((u, w))  # remove for directed graph

    source = input("Enter source node: ")
    destination = input("Enter destination node: ")

    distance, parent = dijkstra(graph, source)

    print("\nShortest Distance:", distance[destination])
    print("Shortest Path:", " -> ".join(reconstruct_path(parent, destination)))


if __name__ == "__main__":
    main()