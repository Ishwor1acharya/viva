import random
import os.path
import json
random.seed()


def draw_board(board):
    """Draws the basic outline with the value of board Noughts and Crosses game"""
    print(f" {board[0][0]} | {board[0][1]} | {board[0][2]} ")
    print("---+---+---")
    print(f" {board[1][0]} | {board[1][1]} | {board[1][2]} ")
    print("---+---+---")
    print(f" {board[2][0]} | {board[2][1]} | {board[2][2]} ")

def welcome(board):
    """Displays the welcome message and the current state of the Tic Tac Toe board"""
    print("Welcome to the game!\nyou are playing  Tic Tac Toe ")
    draw_board(board)
    print()

def initialise_board(board):
    for row in range(3):
        for col in range(3):
            board[row][col] = ' '
    return board

    
def get_player_move(board):
    """Asks the user for the cell to put the X in, and returns the row and col"""
    print('users input')
    while True:
        row = int(input("Enter the row (1-3): ")) - 1
        col = int(input("Enter the column (1-3): ")) - 1

        if (row, col) not in [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]:
            print("Invalid move. Try again.\n")
        elif board[row][col] != ' ':
            print("That spot is already taken. Try again.\n")
        else:
            return row, col



def choose_computer_move(board):
    """Chooses a random cell to put a nought in, and returns the row and col"""
    print('computer choice')
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col

def check_for_win(board, mark):
    '''
    The function check_for_win check if the player has won or lose and returns Ture if player has won otherwise returns false
    '''
    for index in range(3):
         # For a row win condition
        if board[index][0] == board[index][1] == board[index][2] == mark:
            return True  
        # For a column win condition
        if board[0][index] == board[1][index] == board[2][index] == mark: 
            return True
        # For a diagonal from left to right win condition
        if board[0][0] == board[1][1] == board[2][2] == mark:  
            return True
        # For a diagonal from right to left win condition
        if board[0][2] == board[1][1] == board[2][0] == mark: 
            return True
    return False

def check_for_draw(board):
    '''
    The function checks_for_draw bacically checks whether any cell is fuilled or not
    '''
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                return False
    return True

        
def play_game(board):
    # calls the initialise_board function
    board = initialise_board(board)
    # calls the draw_board function
    draw_board(board)

    # Defining the player and computer marks
    player_mark = 'X'
    computer_mark = 'O'

    # Define the current player (player who goes first)
    current_player = 'player'

    #  The game loop starts
    while True:
        # Get the current player's move
        if current_player == 'player':
            row, col = get_player_move(board)
            mark = player_mark
        else:
            row, col = choose_computer_move(board)
            mark = computer_mark

        # Update the board with the current player's move
        board[row][col] = mark

        # Draw the updated board
        draw_board(board)

        # Check for a win
        if check_for_win(board, mark):
            if current_player == 'player':
                # When the Player wins
                return 1
            else:
                # when the computer Computer wins
                return -1

        # conditional statement to check draw
        if check_for_draw(board):
            # Draw
            return 0

        # Switch to the other player
        if current_player == 'player':
            current_player = 'computer'
        else:
            current_player = 'player'

                    
                
def menu():
    while True:
        choice = input("Enter '1' to play the game\nEnter '2' to save score in file 'leaderboard.txt'\nEnter '3' to load and display the scores from the 'leaderboard.txt'\nEnter 'q' to end the program\nEnter your choice: ")
        if choice in ('1', '2', '3', 'q'):
            return choice
        print('Invalid input. Please try again.')


def load_scores():
    # Check if the file exists or not
    if not os.path.isfile('leaderboard.txt'):
        return {}

    # file handling for leaderboard
    with open('leaderboard.txt', 'r') as file:
        scores_json = file.read()

    # It Parse the JSON string into a dictionary
    scores = json.loads(scores_json)

    return scores
    
import json

def save_score(score):
    '''
    The sav_score function saves the score that we play in the game 
    '''
    # Take a input from the player for their names.
    name = input("Enter your name: ")

    # If file is found then its load the exisitng scores from the file.
    try:
        with open('leaderboard.txt', 'r') as f:
            scores_json = f.read()
            scores = json.loads(scores_json)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty, start with an empty dict
        scores = {}

    # It Update the scores dictinary with the new score
    scores[name] = score

    # Save the scores to the file in json format
    with open('leaderboard.txt', 'w') as f:
        f.write(json.dumps(scores))

    # Print a confirmation message for the score to be saved
    print(f"Score of {score} saved successfully for {name}!")



def display_leaderboard(leaders):
    '''
    Its displays the leaderboard score in the console
    '''
    print("LEADERBOARD OF THE GAME")
    for name, score in leaders.items():
        print(f"{name}: {score}")

