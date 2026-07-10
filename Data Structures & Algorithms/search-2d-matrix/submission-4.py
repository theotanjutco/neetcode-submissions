class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        left, right = 0, len(matrix) - 1
        while (left <= right):
            mid = left + ((right - left) // 2)
            
            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][-1]:
                left = mid + 1
            else:
                row = matrix[mid]
                break
            
        else:
            return False
            
        l, r = 0, len(row) - 1
        while (l <= r):
            mid = l + ((r - l) // 2)

            if target > row[mid]:
                l = mid + 1
            elif target < row[mid]:
                r = mid - 1
            else:
                return True
            
        return False
        