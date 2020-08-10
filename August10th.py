"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

"""

"""
풀이법 공유:
이 문제는 26진수를 어떻게 풀것인가 생각해보면된다. 
진수적인 문제로 접근했다. 
"""
#  65 -> 1
#  90 -> 26
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.s = s[::-1]
        self.result = 0
        for i in range(0, len(self.s)):
            self.result += (26**i)*(ord(self.s[i])-64) 

        return self.result

first = "A"
Second = "AB"
Thrid = "ZY"
A = Solution()
print(A.titleToNumber(first))
print(A.titleToNumber(Second))
print(A.titleToNumber(Thrid))
