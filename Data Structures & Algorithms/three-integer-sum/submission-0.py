class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                result = val + nums[l] + nums[r]
                if result > 0:
                    r -= 1
                elif result < 0:
                    l += 1
                else:
                    triplets.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l]== nums[l-1] and l < r:
                        l += 1
        
        return triplets