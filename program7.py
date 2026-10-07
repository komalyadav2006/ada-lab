class ShortestPath:

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []

    def add_edge(self, u, v, weight):
        self.graph.append((u, v, weight))

    # Dijkstra Algorithm
    def dijkstra(self, src):
        distance = [float('inf')] * self.vertices
        visited = [False] * self.vertices

        distance[src] = 0

        for _ in range(self.vertices):

            min_distance = float('inf')
            u = -1

            for i in range(self.vertices):
                if not visited[i] and distance[i] < min_distance:
                    min_distance = distance[i]
                    u = i

            if u == -1:
                break

            visited[u] = True

            for start, end, weight in self.graph:
                if start == u:
                    if distance[u] + weight < distance[end]:
                        distance[end] = distance[u] + weight

        return distance

    # Bellman-Ford Algorithm
    def bellman_ford(self, src):
        distance = [float('inf')] * self.vertices
        distance[src] = 0

        # Relax all edges V-1 times
        for _ in range(self.vertices - 1):
            for u, v, weight in self.graph:

                if distance[u] != float('inf'):
                    if distance[u] + weight < distance[v]:
                        distance[v] = distance[u] + weight

        # Check for negative weight cycle
        for u, v, weight in self.graph:

            if distance[u] != float('inf'):
                if distance[u] + weight < distance[v]:
                    return "Error: Negative weight cycle detected"

        return distance


# Main Program

print("Shortest Path Algorithms")
print("------------------------")

vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

sp = ShortestPath(vertices)

print("\nEnter edges:")
print("Format: source destination weight")

for i in range(edges):
    u, v, w = map(int, input(f"Edge {i + 1}: ").split())
    sp.add_edge(u, v, w)

src = int(input("\nEnter source vertex: "))

# Dijkstra
dijkstra_result = sp.dijkstra(src)

print("\nDijkstra Distance Array:")
print(dijkstra_result)

# Bellman-Ford
bellman_result = sp.bellman_ford(src)

print("\nBellman-Ford Distance Array:")
print(bellman_result)