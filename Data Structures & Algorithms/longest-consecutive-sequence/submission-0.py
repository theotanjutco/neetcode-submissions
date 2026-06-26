class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #store nums in a set (gets rid of duplicates)
        #iterate thru nums if num - 1 is not in set that first num
        #then check if num + 1 is in the set if it is count +=1

        numbers = set(nums)
        finalCount = 0

        for num in numbers:
            currentNum = 0
            count = 0
            if num - 1 not in numbers:
                currentNum = num
                count += 1
                while currentNum + 1 in numbers:
                    currentNum += 1
                    count +=1
            if count > finalCount:
                finalCount = count
        return finalCount