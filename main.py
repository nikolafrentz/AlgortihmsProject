from game2dboard import Board
import random

# Create a board of size 10x10
board = Board(10, 10)
board.title = "Simple Board Game"

# Player starts at position (0, 0)
player_position = [0, 0]

# Function to draw the board
def draw_board():
    board.clear()
    
    # Draw grid and player
    for row in range(10):
        for col in range(10):
            # Mark the player's current position
            if player_position == [row, col]:
                board[row][col] = "P"  # P represents Player
            else:
                board[row][col] = "."  # Empty space

# Function to roll the dice and move the player
def roll_dice():
    return random.randint(1, 6)

# Function to handle player movement
def move_player():
    global player_position
    dice_roll = roll_dice()
    print(f"You rolled a {dice_roll}!")

    # Calculate new position
    new_row = player_position[0] + dice_roll
    if new_row >= 10:  # Keep within bounds
        new_row = 9

    player_position = [new_row, player_position[1]]  # Move vertically

# Main game loop
def game_loop():
    while True:
        draw_board()
        board.show()
        
        move_player()  # Move player after each board draw
        
        # Wait for user input to continue
        input("Press Enter to roll the dice...")

# Start the game
game_loop()
