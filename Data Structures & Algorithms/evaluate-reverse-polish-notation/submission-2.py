class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #Have a current result 
        #the first two indexes are always numbers
        result = 0
        operands = ["+", "-", "*", "/"]
        stack = []

        for i in range(len(tokens)):
            if tokens[i] not in operands:
                stack.append(int(tokens[i]))
            else:
                b = stack.pop()
                a = stack.pop()

                if tokens[i] == '+':
                    result = a + b
                elif tokens[i] == '-':
                    result = a - b
                elif tokens[i] == '*':
                    result = a * b
                else:
                    result = a / b
                
                stack.append(int(result))
        
        return stack[-1]
                    
        