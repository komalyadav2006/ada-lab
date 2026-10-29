class GraphBacktracker:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)

    def graph_coloring(self, m):
        colors = [0] * self.n

        def solve(v):
            if v == self.n:
                return True

            for c in range(1, m + 1):
                safe = True

                for u in range(self.n):
                    if self.graph[v][u] and colors[u] == c:
                        safe = False
                        break

                if safe:
                    colors[v] = c
                    if solve(v + 1):
                        return True
                    colors[v] = 0

            return False

        return colors if solve(0) else []

    def hamiltonian_cycle(self):
        if self.n == 0:
            return []

        path = [0]

        def solve():
            if len(path) == self.n:
                return self.graph[path[-1]][path[0]] != 0

            for v in range(1, self.n):
                if v not in path and self.graph[path[-1]][v] != 0:
                    path.append(v)

                    if solve():
                        return True

                    path.pop()

            return False

        if solve():
            return path + [path[0]]
        return []


graph = [
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

obj = GraphBacktracker(graph)

print("Graph Coloring:", obj.graph_coloring(3))
print("Hamiltonian Cycle:", obj.hamiltonian_cycle())