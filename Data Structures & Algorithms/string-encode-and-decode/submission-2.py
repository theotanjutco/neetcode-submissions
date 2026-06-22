class Solution:

    def encode(self, strs: List[str]) -> str:
        # we want to encode the length of each item in the list
        # we want to put in this format length + # + string
        result = ""

        for i in range(len(strs)):
            result += f"{len(strs[i])}" + "#" + strs[i]
        
        return result
    
    #Set two pointers i and j
    #j moves until it hits the # to record the length
    # once it has the length we slice the string and add it
    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1

            length = int(s[i:j])
            result.append(s[j+1:j+1+length])

            i = j + 1 + length

        return result
