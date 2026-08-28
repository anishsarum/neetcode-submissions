class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            k = (l + r) // 2

            print(k, nums, target)

            if nums[k] == target:
                return k
            
            elif nums[k] < target:
                l = k + 1
            
            else:
                r = k
        
        return -1