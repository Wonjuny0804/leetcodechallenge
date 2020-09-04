class Solution:
    def repeatSubstringPattern(self, s):
        return s in (s + s)[1:-1]