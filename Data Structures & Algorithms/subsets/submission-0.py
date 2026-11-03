class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = set()

        def dfs(curr_i, curr):
            result.add(tuple(curr))
            
            if curr_i + 1 >= len(nums):
                return
            
            for i in range(curr_i + 1, len(nums)):
                dfs(i, curr + [nums[i]])

        dfs(-1, [])

        return [list(tup) for tup in list(result)]
