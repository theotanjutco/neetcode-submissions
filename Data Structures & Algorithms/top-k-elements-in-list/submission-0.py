class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Find a way to go thru each element in the list
        #store the frequencies of each number
        frequencies = defaultdict(int)

        for num in nums:
            frequencies[num] += 1

        heap = []

        #Get all the pairs in the dictionary
        for num, i in frequencies.items():
            heapq.heappush(heap, (i, num))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        #get the nums in the heap
        for i, num in heap:
            result.append(num)

        return result

