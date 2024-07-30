"""
78. Subsets

Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
"""


class Solution:

  def subsets(self, nums: list[int]) -> list[list[int]]:

    ans = [[]]
    for num in nums:
      ans += [subset + [num] for subset in ans]

    return ans

# Example 1:
nums = [1,2,3]
Output = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
ans = Solution().subsets(nums)
print("Output= ", Output)
print("ans= ", ans)