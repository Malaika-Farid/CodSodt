import tkinter as tk
import random
import sys

# Function to determine the winner and update the score
def determine_winner(player_choice):
    global player_score, computer_score
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    computer_label.config(text=f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (
        (player_choice == "Rock" and computer_choice == "Scissors") or
        (player_choice == "Paper" and computer_choice == "Rock") or
        (player_choice == "Scissors" and computer_choice == "Paper")
    ):
        result_label.config(text="You win!")
        player_score += 1
        player_score_label.config(text=f"Player: {player_score}")
    else:
        result_label.config(text="Computer wins!")
        computer_score += 1
        computer_score_label.config(text=f"Computer: {computer_score}")

# Function to quit the game
def quit_game():
    root.destroy()
    sys.exit()

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Initialize scores
player_score = 0
computer_score = 0

# Create and place game labels
instruction_label = tk.Label(root, text="Select your choice:")
instruction_label.pack(pady=10)

computer_label = tk.Label(root, text="")
computer_label.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

player_score_label = tk.Label(root, text=f"Player: {player_score}")
player_score_label.pack(side=tk.LEFT, padx=20)

computer_score_label = tk.Label(root, text=f"Computer: {computer_score}")
computer_score_label.pack(side=tk.RIGHT, padx=20)

# Create and place game buttons
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: determine_winner("Rock"))
paper_button = tk.Button(root, text="Paper", width=10, command=lambda: determine_winner("Paper"))
scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: determine_winner("Scissors"))
quit_button = tk.Button(root, text="Quit", width=10, command=quit_game)

rock_button.pack(side=tk.LEFT, padx=20)
paper_button.pack(side=tk.LEFT)
scissors_button.pack(side=tk.LEFT, padx=20)
quit_button.pack(side=tk.RIGHT, padx=20)

# Start the main loop
root.mainloop()