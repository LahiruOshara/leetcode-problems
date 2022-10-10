class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        ll=len(word)
        def backtrack(row,col,index):
            if index >= ll:
                return True
            if row==m or col==n or row<0 or col<0 or board[row][col]!=word[index]:
                return False
            ret=False
            board[row][col]='#'
            rowOS = [1,0,-1,0]
            colOS = [0,1,0,-1]
            
            for i in range(4):
                ret=backtrack(row+rowOS[i],col+colOS[i],index+1)
                if ret:
                    break
            # reset
            board[row][col]=word[index]
            return ret
        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True
        return False