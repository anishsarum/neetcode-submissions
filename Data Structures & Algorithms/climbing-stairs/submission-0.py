class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1

        for i in range(n):
            temp = b
            b = a + b
            a = temp
        
        return b