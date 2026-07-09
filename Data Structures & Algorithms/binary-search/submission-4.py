class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #you have a left and right pointer, then a mid pointer, move left and right based on the relation of the target and the mid pointer
        l, r = 0, len(nums) - 1
        

        while l <= r:
            mid = l + ((r - l) // 2)

            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid
        return -1

        