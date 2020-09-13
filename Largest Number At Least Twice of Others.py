#Largest Number At Least Twice of Others

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        largest = max(nums)
        ind = nums.index(largest)
        nums.pop(ind)
        if largest >= 2 * max(nums):
            return ind
        else:
            return -1