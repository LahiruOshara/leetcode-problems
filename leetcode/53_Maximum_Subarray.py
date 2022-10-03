class Solution(object):
    def maxSubArray(self, nums):
        ans = -1 * 10**5
        a = 0
        for i in nums:
            a += i # 4 3 5 6 1 -4 4
            ans = max(ans, a) # 4 4 5 6 6 6 6
            a = max(a, 0) # 4 3 5 6 1 0 4
            
        return ans
        