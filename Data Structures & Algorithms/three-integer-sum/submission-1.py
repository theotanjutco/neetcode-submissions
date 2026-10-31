class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = set()
        result = []

        for i, num in enumerate(nums):
            target = -1 * num
            seen = set()
            for c in nums[i + 1::]:
                diff = target - c
                if diff in seen:
                    triplets.add(tuple(sorted([num, diff, c])))
                seen.add(c)
        
        for triplet in triplets:
            result.append(list(triplet))

        return result