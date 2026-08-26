class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Loop through k from 0 to max(piles)
        # For each pile calculate the time taken
        # If exceeds h, then increment h then try next pile
        res = 0
        
        for k in range(1, max(piles) + 1):
            t = h
            for p in piles:
                r = 1
                if k >= p:
                    t -= 1
                else:
                    t -= p // k + 1
                if t < 0:
                    break
            if t >= 0:
                return k