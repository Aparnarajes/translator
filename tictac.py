import random

board = [[' ' for _ in range(3)] for _ in range(3)]
PLAYER = 'X'
computer = 'O'

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

def is_board_full(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def is_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def evaluate(board):
    if is_winner(board, computer):
        return 1
    if is_winner(board, PLAYER):
        return -1
    return 0

def minimax(board, depth, maximizing_player, alpha, beta):
    if is_winner(board, computer):
        return 1
    if is_winner(board, PLAYER):
        return -1
    if is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = computer
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = PLAYER
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def best_move(board):
    best_eval = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = computer
                eval = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

while True:
    print_board(board)

    while True:
        row, col = map(int, input("Enter your move (row[0-2] and column[0-2] separated by space): ").split())
        if board[row][col] == ' ':
            board[row][col] = PLAYER
            break
        else:
            print("Invalid move. Try again.")

    if is_winner(board, PLAYER):
        print_board(board)
        print("Congratulations! You win!")
        break

    if is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break

    print("Computer's turn:")
    row, col = best_move(board)
    board[row][col] = computer

    if is_winner(board, computer):
        print_board(board)
        print("Computer wins! Better luck next time.")
        break

    if is_board_full(board):
        print_board(board)
        print("It's a draw!")
        break
