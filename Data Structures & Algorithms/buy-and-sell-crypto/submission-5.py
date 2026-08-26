class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # profit = 0

        # for i in range(len(prices)):
        #     for j in range(i + 1, len(prices)):
        #         profit = max(profit, prices[j] - prices[i])
        
        # return profit

        min_price = 100
        max_profit = 0
        
        for p in prices:
            max_profit = max(p - min_price, max_profit)
            min_price = min(p, min_price)
        
        return max_profit
