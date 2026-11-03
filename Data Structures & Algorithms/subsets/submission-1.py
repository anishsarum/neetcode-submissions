class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []

        def backtrack(start):
            result.append(curr[:])
            
            for i in range(start, len(nums)):
                curr.append(nums[i])
                backtrack(i + 1)
                curr.pop()

        backtrack(0)

        return result