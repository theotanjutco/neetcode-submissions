class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #cant have duplicates
        charSet = set()
        maxCount = 0
        l = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxCount = max(maxCount, len(charSet))
        
        return maxCount

            

        