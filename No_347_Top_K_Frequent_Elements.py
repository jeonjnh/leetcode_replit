"""
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
"""


class Solution:

  def topKFrequent(self, nums: list[int], k: int) -> list[int]:
    d = {}
    for num in nums:
      if not num in d:
        d[num] = 1
      else:
        d[num] += 1

    return sorted(d, key=d.get, reverse=True)[:k]

# Test Case
nums = [1,1,1,2,2,3]
k = 2
ans = Solution().topKFrequent(nums, k)
print("expected: [1,2], ouput:",ans)