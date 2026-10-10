def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist

def optimal_bst(keys, freq):
    n = len(keys)

    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')

            total = sum(freq[i:j + 1])

            for r in range(i, j + 1):
                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0

                current = left + right + total
                cost[i][j] = min(cost[i][j], current)

    return cost[0][n - 1] if n > 0 else 0

# Floyd-Warshall input
n = int(input("Enter number of vertices: "))
print("Enter the distance matrix (use 99999 for infinity):")

graph = []
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# Replace infinity with a large value
INF = 99999

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            graph[i][j] = INF

result = floyd_warshall(graph)

print("\nShortest Path Matrix:")
for row in result:
    print(*row)

# Optimal BST input
m = int(input("\nEnter number of keys: "))

keys = list(map(int, input("Enter sorted keys: ").split()))
freq = list(map(int, input("Enter frequencies: ").split()))

minimum_cost = optimal_bst(keys, freq)

print("Optimal BST Cost:", minimum_cost)