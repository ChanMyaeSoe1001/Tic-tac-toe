def initialize_board():
    return ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def print_board(board):
    print(f' {board[0]}  |  {board[1]}  |  {board[2]} ')
    print(f'----+-----+----')
    print(f' {board[3]}  |  {board[4]}  |  {board[5]} ')
    print(f'----+-----+----')
    print(f' {board[6]}  |  {board[7]}  |  {board[8]} ')

def check_win(board, player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]

    for combination in win_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

def check_draw(board):
    return all(board[i] in ['X', 'O'] for i in range(9))

def is_board_full(board):
    return all(board[i] in ['X', 'O'] for i in range(9))

def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return -10 + depth
    if check_win(board, 'O'):
        return 10 - depth
    if check_draw(board):
        return 0
    if is_maximizing:
        best_score = float('-inf')
        for i in range(9):
            if board[i] not in ['X', 'O']:
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = str(i + 1)
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] not in ['X', 'O']:
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = str(i + 1)
                best_score = min(best_score, score)
        return best_score

def get_computer_move(board):
    best_score = float('-inf')
    best_move = -1
    for i in range(9):
        if board[i] not in ['X', 'O']:
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = str(i + 1)
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

def tic_tac_toe():
    board = initialize_board()

    while True:

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        computer_move = get_computer_move(board)
        board[computer_move] = 'O'

        if check_win(board, 'O'):
            print_board(board)
            print("Computer wins!")
            print('Computer:  Try better next time. (>_<)')
            break

        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        print_board(board)

        player_move = int(input("Enter your move (1-9): ")) - 1

        if board[player_move] in ['X', 'O']:
            print("Position already taken. Try again.")
            continue

        board[player_move] = 'X'

        if check_win(board, 'X'):
            print_board(board)
            print("Congratulations! You win!")
            break

if __name__ == "__main__":
    tic_tac_toe()
