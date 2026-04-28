'''Question - Given an undirected graph, design and implement an algorithm using Breadth First Search (BFS) to check whether
              the graph is bipartite or not.'''


from collections import deque

def check_bipartite(vertices, adj_list):
    color = [-1] * vertices  # -1 → uncolored

    for start in range(vertices):
        if color[start] == -1:
            queue = deque([start])
            color[start] = 0

            while queue:
                node = queue.popleft()

                for neighbor in adj_list[node]:
                    # If not colored → assign opposite color
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)

                    # If same color → not bipartite
                    elif color[neighbor] == color[node]:
                        return False

    return True


# -------- Driver Code --------
def main():
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    adj_list = [[] for _ in range(V)]

    print("Enter edges (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)
        adj_list[v].append(u)  # undirected graph

    if check_bipartite(V, adj_list):
        print("Yes Bipartite")
    else:
        print("Not Bipartite")


if __name__ == "__main__":
    main()