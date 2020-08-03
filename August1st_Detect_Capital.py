"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:
            return True
        else:
            if word[0].isupper():
                if word[1].islower():
                    if word[1:].islower():
                        return True
                    else:
                        return False
                else:
                    if word[1:].isupper():
                        return True
                    else:
                        return False
            else:
                if word.islower():
                    return True
                else:
                    return False
txt = 'THe Apple'

A = Solution()
print(A.detectCapitalUse(txt))