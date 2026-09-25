from dataclasses import dataclass
from typing import List


@dataclass
class Edge:
    u: int
    v: int
    weight: int


class Graph:

    def __init__(self, vertices: int):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u: int, v: int, weight: int):
        self.edges.append(Edge(u, v, weight))

    # Kruskal's Algorithm

    def kruskal_mst(self) -> List[Edge]:

        parent = list(range(self.vertices))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                parent[root_b] = root_a
                return True

            return False

        # Sort edges by weight
        sorted_edges = sorted(self.edges, key=lambda edge: edge.weight)

        mst = []

        for edge in sorted_edges:
            if union(edge.u, edge.v):
                mst.append(edge)

            if len(mst) == self.vertices - 1:
                break

        return mst

    # Prim's Algorithm

    def prim_mst(self) -> List[Edge]:

        visited = [False] * self.vertices
        mst = []

        visited[0] = True

        for _ in range(self.vertices - 1):

            minimum_edge = None

            for edge in self.edges:

                if (visited[edge.u] and not visited[edge.v]) or \
                   (visited[edge.v] and not visited[edge.u]):

                    if minimum_edge is None or edge.weight < minimum_edge.weight:
                        minimum_edge = edge

            if minimum_edge is None:
                break

            mst.append(minimum_edge)

            visited[minimum_edge.u] = True
            visited[minimum_edge.v] = True

        return mst


# Create Graph

g = Graph(5)

g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)


# Kruskal Output

print("Kruskal MST:")

kruskal_result = g.kruskal_mst()

total = 0

for edge in kruskal_result:
    print(edge.u, "--", edge.v, "Weight =", edge.weight)
    total += edge.weight

print("Total MST Weight =", total)


# Prim Output

print("\nPrim MST:")

prim_result = g.prim_mst()

total = 0

for edge in prim_result:
    print(edge.u, "--", edge.v, "Weight =", edge.weight)
    total += edge.weight

print("Total MST Weight =", total)