
EMPTY = ' '
X = 'x'
O = 'o'

board = [EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY,EMPTY]

def print_board():
    print('--------')
    print(f'|{board[0]}|{board[1]}|{board[2]}|')
    print('--------')
    print(f'|{board[3]}|{board[4]}|{board[5]}|')
    print('--------')
    print(f'|{board[6]}|{board[7]}|{board[8]}|')
    print('--------')
    
def check_win(c):
    
    # rows
    
    if board[0] == c and board[1] == c and board[2] == c: return True
    if board[3] == c and board[4] == c and board[5] == c: return True
    if board[6] == c and board[7] == c and board[8] == c: return True
    
    # columns
    
    if board[0] == c and board[3] == c and board[6] == c: return True
    if board[1] == c and board[4] == c and board[7] == c: return True
    if board[2] == c and board[5] == c and board[8] == c: return True
    
    # diagonals
    
    if board[0] == c and board[4] == c and board[8] == c: return True
    if board[6] == c and board[4] == c and board[2] == c: return True

    return False
    

while True:
    pass
    # print_board()
    
    # # Add input validation
    # player1 = input(f'{X}: Ruch (x.y) (1-3):')
    
    # x1, y1 = player1.split('.')
    # x1, y1 = int(x1) - 1, int(y1) - 1
    # if board[x1][y1] == EMPTY:
    #     board[x1][y1] = O
    
    # print_board()
    
    # player2 = input(f'Ruch {O}:')
    
    # x2, y2 = player2.split('.')
    # x2, y2 = int(x2) - 1, int(y2) - 1
    # if board[x2][y2] == EMPTY:
    #     board[x2][y2] = O