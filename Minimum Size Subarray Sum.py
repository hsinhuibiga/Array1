#Minimum Size Subarray Sum

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        l, r = 0, 0
        csum = 0
        res = float('inf')
        while r < N:
            csum += nums[r]
            while csum >= s:
                res = min(res, r - l + 1)
                csum -= nums[l]
                l += 1
            r += 1
        return res if res != float('inf') else 0