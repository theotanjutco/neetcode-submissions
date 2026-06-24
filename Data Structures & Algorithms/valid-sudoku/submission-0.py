class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #board is valid if theres no duplicates in the colums, rows, or box

        #iterate thru each row, find duplicates
        for row in range(len(board)):
            seenRow = set()
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seenRow:
                    return False
                seenRow.add(board[row][col])

        #iterate thru each col, find duplicates
        for col in range(len(board)):
            seenCol = set()
            for row in range(len(board)):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seenCol:
                    return False
                seenCol.add(board[row][col]) 

        #iterate thru each box, find duplicates
        # box = (row // 3) * 3 + (col // 3)
        seenBox = defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue

                box = (row // 3) * 3 + (col // 3)

                if board[row][col] in seenBox[box]:
                    return False
                seenBox[box].add(board[row][col])
        
        return True



        