# BFS CODE
def bfs(graph, start):
    visited = set()
    queue = []

    visited.add(start)
    queue.append(start)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

# DFS CODE
def dfs(graph, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)

# Initialize an empty graph
graph = {}

# Input the graph nodes and edges interactively
num_nodes = int(input("Enter the number of nodes: "))

for i in range(num_nodes):
    node = input(f"Enter the name of node {i + 1}: ")
    neighbors_input = input(f"Enter neighbors of {node} (comma-separated): ")
    neighbors = neighbors_input.split(',')
    graph[node] = [n.strip() for n in neighbors if n.strip()]

start_node = input("Enter the starting node: ")

print("Breadth-First Search (BFS):")
bfs(graph, start_node)
print("\n")

print("Depth-First Search (DFS):")
visited = set()
dfs(graph, start_node, visited)

