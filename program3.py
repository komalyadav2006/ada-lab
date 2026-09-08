from typing import List, Tuple

def findKthLargest(nums: List[int], k: int) -> int:
    nums.sort(reverse=True)
    return nums[k - 1]


def findMinMax(nums: List[int]) -> Tuple[int, int]:
    return min(nums), max(nums)


# Example
nums = [3, 2, 1, 5, 6, 4]
k = 2

print("Kth largest element:", findKthLargest(nums, k))
print("Min and Max:", findMinMax(nums))