from typing import List

# Binary Search
def search(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Fast Power (Binary Exponentiation)
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0

    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0

    while n > 0:
        if n % 2 == 1:
            result *= x

        x *= x
        n //= 2

    return result
print(search([-1, 0, 3, 5, 9, 12], 9))
# Output: 4

print(search([-1, 0, 3, 5, 9, 12], 2))
# Output: -1

print(myPow(2.0, 10))
# Output: 1024.0

print(myPow(2.0, -2))
# Output: 0.25