# Leetcode: Sudoku Solver     :BLOG:Hard:


---

Sudoku Solver  

---

Write a program to solve a Sudoku puzzle by filling the empty cells.  

Empty cells are indicated by the character '.'.  

You may assume that there will be only one unique solution.  

Blog link: <http://brain.dennyzhang.com/sudoku-solver>  

Github: challenges-leetcode-interesting  

Credits To: leetcode.com  

Leave me comments, if you know how to solve.  

    ## Basic Ideas: backtracking
    ##             For each '.', try with 0-9.
    ##                 If test has passed, keep moving forward
    ##                 Otherwise stop current thread
    ##
    ## Complexity: Time O(k), k is the count of '.', Space ?
    class Solution(object):
        def solveSudoku(self, board):
            """
            :type board: List[List[str]]
            :rtype: void Do not return anything, modify board in-place instead.
            """
            if len(board) != 9 or len(board[0]) != 9:
                return 0
            _can_solve = self.mySolveSudoku(board, 0, 0)
            # print("can_solve: %d" % (can_solve))
    
        def mySolveSudoku(self, board, irow, icol):
            # if irow > 6:
            #    print("irow: %d, icol: %d" % (irow, icol))
            # print board
            if irow == 9:
                return True
    
            irow2, icol2 = None, None
            if icol == 8:
                irow2, icol2 = irow+1, 0
            else:
                irow2, icol2 = irow, icol + 1
    
            if board[irow][icol] != '.':
                return self.mySolveSudoku(board, irow2, icol2)
    
            # try with all possibilities
            for i in xrange(9):
                value = chr(ord('1')+i)
                # Change contenxt: go further
                board[irow][icol] = value
                if self.isSudoku(board, irow, icol, value):
                    if self.mySolveSudoku(board, irow2, icol2):
                        return True
    
            # Restore context: only the outer-layer
            board[irow][icol] = '.'
            return False
    
        def isSudoku(self, board, irow, icol, value):
            # If we set board[irow][icol] to value, is it still a valid sudoku.
            for index in xrange(9):
                # check row
                if index == icol: continue
                if board[irow][index] == value:
                    return False
    
            for index in xrange(9):
                # check col
                if index == irow: continue
                if board[index][icol] == value:
                    return False
    
            # check section
            istart, jstart = (irow/3)*3, (icol/3)*3
            for i in range(0, 3):
                for j in range(0, 3):
                    if istart+i == irow and jstart+j == icol: continue
                    if board[istart+i][jstart+j] == value:
                        return False
            return True