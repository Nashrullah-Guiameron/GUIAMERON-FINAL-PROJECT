def print_board(board):
    """Prints the current state of the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    """Checks if the player has won the game."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    return all(all(cell != " " for cell in row) for row in board)

def main():
    print("Welcome to Tic-Tac-Toe!")
    player1 = input("Enter name for Player 1 (X): ")
    player2 = input("Enter name for Player 2 (O): ")

    current_player = player1
    symbol = 'X'
    board = [[" " for _ in range(3)] for _ in range(3)]

    while True:
        print("\nCurrent board:")
        print_board(board)
        row = int(input(f"{current_player}, enter row (0, 1, 2): "))
        col = int(input(f"{current_player}, enter column (0, 1, 2): "))

        if board[row][col] != " ":
            print("That position is already taken. Try again.")
            continue

        board[row][col] = symbol

        if check_win(board, symbol):
            print("\nCurrent board:")
            print_board(board)
            print(f"Congratulations, {current_player} wins!")
            break
        elif is_board_full(board):
            print("\nCurrent board:")
            print_board(board)
            print("It's a tie!")
            break

        # Switch players
        if current_player == player1:
            current_player = player2
            symbol = 'O'
        else:
            current_player = player1
            symbol = 'X'

if __name__ == "__main__":
    main()
