"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        self.s = s
        self.alphabet = []
        self.dic = {}
        for letter in self.s:
            if letter not in self.alphabet:
                self.alphabet.append(letter)
                self.dic[letter] = 0
        
        for letter in self.alphabet:
            for things in self.s:
                if things == letter:
                    self.dic[letter] += 1
        

        print(self.dic)
        self.maxlength = 0
        for items in self.dic.values():
            if items % 2 == 0:
                self.maxlength += int(items)
        if 1 in self.dic.values():
            for items in self.dic.values()


        return self.maxlength

s ="abccccdd"
A = Solution()
A.longestPalindrome(s)