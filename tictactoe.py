def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")


def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_draw(board):
    return all(cell != " " for row in board for cell in row)


def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        print(f"Player {players[current_player]}'s turn")
        while True:
            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))

                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    board[row][col] = players[current_player]
                    break
                else:
                    print("Invalid move, try again.")
            except ValueError:
                print("Please enter valid integers between 0 and 2.")

        print_board(board)

        if check_winner(board, players[current_player]):
            print(f"Player {players[current_player]} wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        current_player = 1 - current_player  # Switch player


if __name__ == "__main__":
    play_game()
