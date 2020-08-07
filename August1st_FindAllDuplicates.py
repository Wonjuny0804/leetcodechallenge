"""

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

"""
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        self.low = []
        self.duplicate = []
        nums.sort()
        for num in nums:
            if num not in self.duplicate:
                self.duplicate.append(num)
            else:
                self.low.append(num)
        return self.low