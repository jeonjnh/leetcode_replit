"""
1310. XOR Queries of a Subarray

You are given an array arr of positive integers. You are also given the array queries where queries[i] = [lefti, righti].

For each query i compute the XOR of elements from lefti to righti (that is, arr[lefti] XOR arr[lefti + 1] XOR ... XOR arr[righti] ).

Return an array answer where answer[i] is the answer to the ith query.



Example 1:

Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8] 
Explanation: 
The binary representation of the elements in the array are:
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
The XOR values for queries are:
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8

Example 2:

Input: arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
Output: [8,0,4,4]
"""
from typing import List

# Time Limit Exceeded
"""

class Solution:

  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
    ans = []

    for left, right in queries:
      xor = self.xorCal(arr, left, right)
      ans.append(xor)

    return ans

  def xorCal(self, arr, start, end):
    res = arr[start]
    if start == end:
      return res
    else:
      for i in range(start + 1, end + 1):
        res ^= arr[i]

    return res
"""


class Solution:

  def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:

    pre_XOR = [0] * (len(arr) + 1)

    for i in range(len(arr)):
      pre_XOR[i + 1] = pre_XOR[i] ^ arr[i]

    res = []
    for left, right in queries:
      xor_res = pre_XOR[right + 1] ^ pre_XOR[left]
      res.append(xor_res)

    return res

# Example 1
arr = [1,3,4,8]
queries = [[0,1],[1,2],[0,3],[3,3]]
Output = [2,7,14,8] 
ans = Solution().xorQueries(arr, queries)
print("ans = ", ans, " Output = ", Output)
