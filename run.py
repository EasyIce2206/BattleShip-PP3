import random

"""
Battleship game
- Create a 5x5 board
- Place 5 ships on the board
- Player has 10 turns to guess the location of the ships
- If player guesses correctly, mark the board with an 'X'
- If player guesses incorrectly, mark the board with an 'M'
- If player sinks all the ships, player wins
- If player runs out of turns, game over
"""
def print_board(board):
    for row in board:
        print(" ".join(row))

def create_board(size):
    return [["O"] * size for _ in range(size)]

def place_ships(board, size):
    for _ in range(size):
        ship_row, ship_col = random.randint(0, size-1), random.randint(0, size-1)
        while board[ship_row][ship_col] == "S":
            ship_row, ship_col = random.randint(0, size-1), random.randint(0, size-1)
        board[ship_row][ship_col] = "S"

def get_player_input():
    while True:
        try:
            row = int(input("Enter row:\n"))
            col = int(input("Enter column:\n "))
            return row, col
        except ValueError:
            print("Invalid input. Please enter integers only.")

def main():
    player_name = input("Enter your name:\n ")
    size = 5
    player_board = create_board(size)
    computer_board = create_board(size)
    hidden_board = create_board(size)
    place_ships(computer_board, size)

    print(f"Welcome {player_name} to Battleship!")
    print("Here is your board:")
    print_board(player_board)

    turns = 10
    score = 0

    while turns > 0:
        print(f"\nTurns remaining: {turns}")
        row, col = get_player_input()

        if row < 0 or row >= size or col < 0 or col >= size:
            print("Out of bounds. Try again.")
            continue

        if hidden_board[row][col] == "X" or hidden_board[row][col] == "M":
            print("You already guessed that. Try again.")
            continue

        if computer_board[row][col] == "S":
            print("Hit!")
            hidden_board[row][col] = "X"
            score += 1
        else:
            print("Miss!")
            hidden_board[row][col] = "M"

        print("Current board:")
        print_board(hidden_board)
        turns -= 1

        if score == size:
            print("Congratulations! You sunk all the ships!")
            break

    print(f"Game over! Your score: {score}")

if __name__ == "__main__":
    main()

    