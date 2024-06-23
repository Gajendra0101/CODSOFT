def print_board(board):
    for row in board:
        print(" | ".join(row))
        if row != board[-1]:
            print("-----------")

def check_win(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True

    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def play_game():
    print("Welcome to Tic Tac Toe!")
    print("Here is the board with positions:")
    print_board([["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]])
    print("Player 1 is X. Player 2 is O.")
    print("Let's start!\n")

    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        while True:
            try:
                position = int(input("Choose your position (1-9): "))
                if 1 <= position <= 9:
                    row = (position - 1) // 3
                    col = (position - 1) % 3

                    if board[row][col] == " ":
                        board[row][col] = current_player
                        break
                    else:
                        print("That position is already taken. Please try again.")
                else:
                    print("Please enter a number between 1 and 9.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

play_game()
