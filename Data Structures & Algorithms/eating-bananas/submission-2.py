class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for k in range(1, max(piles) + 1):
        #     t = h
        #     for p in piles:
        #         if k >= p:
        #             t -= 1
        #         else:
        #             t -= p // k + 1
        #         if t < 0:
        #             break
        #     if t >= 0:
        #         return k

        l, r = 1, max(piles)
        res = max(piles)
        piles.sort()
        while l <= r:
            k = (l + r) // 2
            t = h
            for p in piles:
                if k >= p:
                    t -= 1
                else:
                    t -= p // k + 1
                if t < 0:
                    break
            if t >= 0:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res