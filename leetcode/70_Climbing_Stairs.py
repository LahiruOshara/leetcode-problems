class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n
        arr = [0] * n
        arr[0] = 1
        arr[1] = 2
        for i in range(2, n):
            arr[i] = arr[i - 1] + arr[i - 2]
            
        return arr[n-1]