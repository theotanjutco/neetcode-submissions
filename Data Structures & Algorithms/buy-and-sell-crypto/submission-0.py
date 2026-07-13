class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # To find the maximum profit you need the lowest and maximum price
        # Least price must come before the maximum

        left, right = 0, 1
        maxProfit = 0
        while right <= len(prices) - 1:
            if prices[right] > prices[left]:
                maxProfit = max(maxProfit, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1
            
        return maxProfit
        
        
        