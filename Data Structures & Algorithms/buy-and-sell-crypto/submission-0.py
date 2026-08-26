class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l = len(prices)
        r1, r2 = [100] * l, [0] * l
        r1[0] = prices[0]
        r2[-1] = prices[-1]
        for i in range(1, l):
            r1[i] = min(r1[i - 1], prices[i])
        for i in range(l - 2, -1, -1):
            r2[i] = max(r2[i + 1], prices[i])
        for i in range(l):
            res = max(res, r2[i] - r1[i])
        return res