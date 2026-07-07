class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #basically if a car is slow and in the front and it hasnt hit the target the faster ones in the back will eventually create a fleet

        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        
        stack = []

        for pos, speed in cars:
            distance = target - pos
            time = distance / speed

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


        