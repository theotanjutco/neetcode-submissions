class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for letter in s:
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1
        
        for letter in t:
            if letter in seen:
                seen[letter] -= 1
            else:
                return False
        
        for count in seen.values():
            if count != 0:
                return False
        return True