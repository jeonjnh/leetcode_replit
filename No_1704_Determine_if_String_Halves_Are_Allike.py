"""
1704. Determine if String Halves Are Alike

You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: a = "bo" and b = "ok". a has 1 vowel and b has 1 vowel. Therefore, they are alike.

Example 2:
Input: s = "textbook"
Output: false
Explanation: a = "text" and b = "book". a has 1 vowel whereas b has 2. Therefore, they are not alike.
Notice that the vowel o is counted twice.
"""


class Solution:

  def halvesAreAlike(self, s: str) -> bool:

    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    n = len(s)
    a = 0
    b = 0
    for i, c in enumerate(s):
      if i < n / 2:
        if c in vowels:
          a += 1
      else:
        if c in vowels:
          b += 1

    return a == b

#Example 1
s = "book"
ans = Solution().halvesAreAlike(s)
print(ans)

#Example 2
s = "textbook"
ans = Solution().halvesAreAlike(s)
print(ans)