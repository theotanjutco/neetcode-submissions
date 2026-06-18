class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        for num in nums:
            if counts[num] > 1:
                return True
        
        return False