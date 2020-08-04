"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
"""
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hset = []

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hset.append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        while key in self.hset:
            self.hset.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.hset:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
obj = MyHashSet()
print(obj.add(1))
print(obj.add(2))
print(obj.contains(1))
print(obj.contains(3))
print(obj.add(2))
print(obj.contains(2))
print(obj.remove(2))
print(obj.contains(2))
print(obj.hset)