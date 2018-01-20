# Leetcode: N-Queens     :BLOG:Hard:


---

N-Queens  

---

The n-queens puzzle is the problem of placing n queens on an n X n chessboard such that no two queens attack each other.  

Given an integer n, return all distinct solutions to the n-queens puzzle.  

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.  

    For example,
    There exist two distinct solutions to the 4-queens puzzle:
    
    [
     [".Q..",  // Solution 1
      "...Q",
      "Q...",
      "..Q."],
    
     ["..Q.",  // Solution 2
      "Q...",
      "...Q",
      ".Q.."]
    ]

Blog link: <http://brain.dennyzhang.com/n-queens>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: backtracking.
    ##              Place queens row by row
    ##              Check if place in current position, examine the column and triangle
    ##
    ## Complexity: Time ?, Space ?
    class Solution(object):
        def solveNQueens(self, n):
            """
            :type n: int
            :rtype: List[List[str]]
            """
            if n <= 0:
                return None
    
            self.board = []
            for i in xrange(n):
                self.board.append(['.']*n)
    
            self.res = []
            self.mySolveNQueens(n, 0)
            return self.res
    
        def mySolveNQueens(self, n, irow):
            if irow == n:
                item = []
                for row in self.board:
                    item.append(''.join(row))
                self.res.append(item)
                return
    
            for icol in xrange(n):
                # place Q
                if self.isNQuees(n, irow, icol):
                    self.board[irow][icol] = 'Q'
                    self.mySolveNQueens(n, irow+1)
                self.board[irow][icol] = '.'
    
        def isNQuees(self, n, irow, icol):
            for index in xrange(n):
                # check column
                if index == irow: continue
                if self.board[index][icol] == 'Q': return False
    
            for i in xrange(n):
                for j in xrange(n):
                    if irow == i and icol == j: continue
                    if abs(irow-i) == abs(icol-j) and self.board[i][j] == 'Q':
                        return False
            return True
    
    s = Solution()
    print s.solveNQueens(8)