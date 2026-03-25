
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


def mark_symbol(c):
    
    while True:
        player_input = input(f'Ruch {c} (x):')
        try:
            
            x = int(player_input) - 1
            if x < 0 or x > 8 or board[x] != EMPTY:
                player_input = input('Podaj prawidłowy ruch: (x)')
                x = int(player_input) - 1
        
            board[x] = c
            break
        except:
            pass

def is_board_full():
    filled = sum(x for x in board if board != EMPTY)
    return filled == 9 # board is full

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
    print_board()
    mark_symbol(X)
    print_board()
    mark_symbol(O)
    
    if check_win(X):
        print('Wygrał X!')
        break
    
    if check_win(O):
        print('Wygrał O!')
        break
    
    if is_board_full():
        print('Remis')