class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # You take an element from list count how many elements it takes to get a higher number
        results = []

        for i in range(len(temperatures)):
            count = 0
            found = False
            for j in range(i+1, len(temperatures)):
                count += 1

                if temperatures[j] > temperatures[i]:
                    results.append(count)
                    found = True
                    break
            
            if not found:
                results.append(0)
        
        return results
