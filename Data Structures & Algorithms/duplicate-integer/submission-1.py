class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_n = set()
        for n in nums:
            if n in set_n:
                return True

            set_n.add(n)
        return False
