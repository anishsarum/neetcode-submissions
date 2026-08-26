class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        L = len(temperatures)
        res = []
        for i in range(L):
            for j in range(i, L + 1):
                if j == L:
                    res.append(0)
                elif temperatures[j] > temperatures[i]:
                    res.append(j - i)
                    break
        return res