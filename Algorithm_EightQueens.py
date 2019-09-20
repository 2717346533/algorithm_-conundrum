def noConflicts(board,current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if(current - i == abs(board[current] - board[i])):
            return False
    return True

def EightQueens(n=8):
    board = [-1] * n
    for i in range(n):
        board[0] = i
        for j in range(n):
            board[1] = j
            if not noConflicts(board,1):
                continue
            for k in range(n):
                board[2] = k
                if not noConflicts(board,2):
                    continue
                for l in range(n):
                    board[3] = l
                    if not noConflicts(board, 3):
                        continue
                    for m in range(n):
                        board[4] = m
                        if not noConflicts(board, 4):
                            continue
                        for o in range(n):
                            board[5] = o
                            if not noConflicts(board, 5):
                                continue
                            for p in range(n):
                                board[6] = p
                                if not noConflicts(board, 6):
                                    continue
                                for q in range(n):
                                    board[7] = q
                                    if noConflicts(board,7):
                                        print(board)
    return

EightQueens(n=8)