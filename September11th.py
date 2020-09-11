"""
Bulls and Cows?
"""
class Solution:
    def getHint(self, secret, guess):
        g = []
        A = 0
        B = 0
        for i in guess:
            g.append(i)
        for i in range(0, len(secret)):
            if secret[i] == guess[i]:
                A += 1
                g.remove(guess[i])
            else:
                if secret[i] in g:
                    B += 1
        return str(A)+"A"+str(B)+"B"

a = Solution()
print(a.getHint("1807", "7810"))
print(a.getHint("1123", "0111"))
print(a.getHint("11", "10"))
