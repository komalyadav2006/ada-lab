from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# User input
nums = list(map(int, input("Enter array elements separated by spaces: ").split()))

result = lengthOfLIS(nums)

print("Length of Longest Increasing Subsequence:", result)
