'''Question- Write a program to detect whether a cycle exists in a directed graph using Depth First Search (DFS).

             Represent the graph using an adjacency list.
             Use recursion and a recursion stack to detect back edges.
             Print "Cycle Exists" if a cycle is found, otherwise print "No Cycle".'''

def detect_cycle_dfs(node, adj_list, visited, recursion_stack):
    # Mark current node as visited and add to recursion stack
    visited[node] = True
    recursion_stack[node] = True

    # Explore all adjacent nodes
    for neighbor in adj_list[node]:
        # If not visited, recurse
        if not visited[neighbor]:
            if detect_cycle_dfs(neighbor, adj_list, visited, recursion_stack):
                return True
        
        # If neighbor is in recursion stack → cycle found
        elif recursion_stack[neighbor]:
            return True

    # Remove node from recursion stack before returning
    recursion_stack[node] = False
    return False


def has_cycle(vertices, adj_list):
    visited = [False] * vertices
    recursion_stack = [False] * vertices

    # Check each component of graph
    for node in range(vertices):
        if not visited[node]:
            if detect_cycle_dfs(node, adj_list, visited, recursion_stack):
                return True

    return False


# -------- Driver Code --------
def main():
    V = int(input("Enter number of vertices: "))
    E = int(input("Enter number of edges: "))

    adj_list = [[] for _ in range(V)]

    print("Enter directed edges (u v):")
    for _ in range(E):
        u, v = map(int, input().split())
        adj_list[u].append(v)

    if has_cycle(V, adj_list):
        print("Cycle Exists")
    else:
        print("No Cycle")


if __name__ == "__main__":
    main()