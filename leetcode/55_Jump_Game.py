class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxDistance = 0
        for i in range(len(nums)):
            if i > maxDistance:
                return False
            maxDistance = max(maxDistance, i + nums[i])
        return True
        