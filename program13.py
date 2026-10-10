class TSPSolver:
    def solve_tsp(self, dist_matrix):
        n = len(dist_matrix)
        visited = [False] * n
        visited[0] = True

        def tsp(city, count, cost):
            if count == n:
                return cost + dist_matrix[city][0]

            ans = float('inf')

            for next_city in range(n):
                if not visited[next_city]:
                    visited[next_city] = True

                    ans = min(
                        ans,
                        tsp(
                            next_city,
                            count + 1,
                            cost + dist_matrix[city][next_city]
                        )
                    )

                    visited[next_city] = False

            return ans

        return tsp(0, 1, 0)

# User input
n = int(input("Enter number of cities: "))

print("Enter the distance matrix row by row:")

dist_matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    dist_matrix.append(row)

solver = TSPSolver()
result = solver.solve_tsp(dist_matrix)

print("Minimum tour cost:", result)
