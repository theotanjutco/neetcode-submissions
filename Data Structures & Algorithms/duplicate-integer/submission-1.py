class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        # counts = {}

        # for num in nums:
        #     if num in counts:
        #         counts[num] += 1
        #     else:
        #         counts[num] = 1
        
        # for num in nums:
        #     if counts[num] > 1:
        #         return True
        
        # return False