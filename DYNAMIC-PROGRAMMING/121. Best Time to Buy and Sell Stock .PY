class Solution:
    def maxProfit(self, prices):
        n=len(prices)
        MinValue=prices[0]
        Profit=0
        for i in range(1,n):
            cost=prices[i]-MinValue
            Profit=max(Profit,cost)
            MinValue=min(MinValue,prices[i])
        return Profit