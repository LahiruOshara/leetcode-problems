class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """        
        buy = 10 ** 5
        sell = 0
        for i in range(len(prices)):
            buy = min(buy, prices[i])
            sell = max(sell, prices[i] - buy)
            
        return sell
                