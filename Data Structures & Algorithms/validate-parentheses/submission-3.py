class Solution:
    def isValid(self, s: str) -> bool:
        # actually we iterate thru the string
        # iterate through the list if an open bracket then i+1
        # has to be close bracket same type or another open bracket
        brackets = {'(' : ')', '{' : '}', '[' : ']' }
        stack = deque()
        for char in s:
            if char in brackets:
                stack.append(brackets[char])
            else:
                if not stack or char != stack[-1]:
                    return False
                stack.pop()

        return not stack            
        