class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #take the difference of the target - nums[i]
        #make a dictionary storing value needed and index of nums[i]

        seen = {}
        value = 0

        for i, num in enumerate(nums):
            value = target - num
            if value in seen:
                return [seen[value], i]
            
            seen[num] = i
            

        