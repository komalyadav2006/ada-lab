def knapsack_01(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):

        for w in range(capacity + 1):

            # Current item's weight
            current_weight = weights[i - 1]

            # Current item's value
            current_value = values[i - 1]

            # If item can be included
            if current_weight <= w:

                dp[i][w] = max(
                    dp[i - 1][w],
                    current_value + dp[i - 1][w - current_weight]
                )

            else:
                # Cannot include item
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# -----Main Program-----

print("0/1 Knapsack Problem")
print("--------------------")

n = int(input("Enter number of items: "))

weights = []
values = []

print("\nEnter weights:")
for i in range(n):
    weight = int(input(f"Weight of item {i + 1}: "))
    weights.append(weight)

print("\nEnter values:")
for i in range(n):
    value = int(input(f"Value of item {i + 1}: "))
    values.append(value)

capacity = int(input("\nEnter knapsack capacity: "))

# Calculate maximum value
result = knapsack_01(weights, values, capacity)

print("\nWeights:", weights)
print("Values:", values)
print("Capacity:", capacity)
print("Maximum Value:", result)