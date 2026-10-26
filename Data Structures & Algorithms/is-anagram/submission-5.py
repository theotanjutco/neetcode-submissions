class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)

        if len(s) != len(t):
            return False
            
        for letter in s:
            seen[letter] += 1
        
        for letter in t:
            seen[letter] -= 1
        
        for i in seen.values():
            if i != 0:
                return False
        
        return True