class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        low,res = prices[0],0
        for i in range(1,len(prices)):
            low = min(low,prices[i])
            res = max(res, prices[i] - low)
        return res