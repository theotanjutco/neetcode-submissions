class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # You take an element from list count how many elements it takes to get a higher number
        # have monotonic decreasing stack
        #if something is greater than previous pop previous store current
        
        results = [0] * len(temperatures) #initializes everthing to 0
        stack = [] #monotonic decreasing stack

        for i, t in enumerate(temperatures): #grab the index and the temperature
            while stack and t > stack[-1][0]: # while the stack is not empty and the current temp is greater than the top temp
                stackTemp, stackIndex = stack.pop() # remove the top temp bc u found the greater temp
                results[stackIndex] = i - stackIndex #calculate how many days it took, add to results
            
            stack.append([t, i]) # if not valid in the while loop just add it to stack
        
        return results

