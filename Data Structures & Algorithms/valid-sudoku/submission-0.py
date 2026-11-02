class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for i in range(0, len(board)):
            s = set()
            for j in range(0, len(board)):
                if board[i][j]=='.':
                    continue
                val = int(board[i][j])
                if val in s:
                    return False
                s.add(val)
        # check cols
        for i in range(0, len(board)):
            s = set()
            for j in range(0, len(board)):
                if board[j][i]=='.':
                    continue
                val = int(board[j][i])
                if val in s:
                    return False
                s.add(val)

        for r in range(0, len(board), 3):
            for c in range(0, len(board), 3):
                s = set()
                for i in range(3):
                    for j in range(3):
                        row = r+i
                        col = c+j
                        if board[row][col]=='.':
                            continue
                        val = int(board[row][col])
                        if val in s:
                            return False
                        s.add(val)

        return True  

