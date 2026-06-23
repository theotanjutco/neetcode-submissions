class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # We need to find the product of every number in the array except itself
        # multiplying everything on the left and right of num[i]

        length = len(nums)

        #prefix product?
        results = [1] * length

        prefixProduct = 1
        for i in range(length):
            results[i] = prefixProduct
            prefixProduct *= nums[i]

        backwardProduct = 1
        for i in range(length - 1, -1, -1):
            results[i] *= backwardProduct
            backwardProduct *= nums[i]
        
        return results
            

        