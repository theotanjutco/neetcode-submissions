class Solution:
    def isValid(self, s: str) -> bool:
        valid = {'(':')', '[':']', '{':'}'}
        stack = []

        for i in s:
            if i in valid:
                stack.append(valid[i])
            else:
                if not stack or stack[-1] != i:
                    return False
                stack.pop()
        if not stack:
            return True
        else:
            return False        