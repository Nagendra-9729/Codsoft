import tkinter as tk
from tkinter import ttk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!", 1
    else:
        return "Computer wins!", -1

# Function to handle user's choice
def user_choice(choice):
    global user_score, computer_score
    computer_choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_choices)

    result, score = determine_winner(choice, computer_choice)

    user_score += score
    computer_score -= score
    
    # Update the score labels
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer Score: {computer_score}")
    
    # Show the computer's choice and the result
    computer_label.config(text=f"Computer's choice: {computer_choice}")
    result_label.config(text=result, foreground="green" if result == "You win!" else "red" if result == "Computer wins!" else "black")

# Function to reset the game
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer Score: 0")
    result_label.config(text="")
    computer_label.config(text="")
    feedback_entry.delete(0, tk.END)  # Clear the feedback entry

# Function to submit feedback
def submit_feedback():
    feedback_text = feedback_entry.get()
    if feedback_text:
        feedback_label.config(text=f"Feedback: {feedback_text}")
        feedback_entry.delete(0, tk.END)  # Clear the feedback entry

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# Create labels with styling
style = ttk.Style()
style.configure("TLabel", foreground="blue", font=("Arial", 12))
user_label = ttk.Label(root, text="Your choice:")
computer_label = ttk.Label(root, text="Computer's choice:")
result_label = ttk.Label(root, text="", font=("Arial", 14, "bold"))
user_score_label = ttk.Label(root, text="Your Score: 0", font=("Arial", 12))
computer_score_label = ttk.Label(root, text="Computer Score: 0", font=("Arial", 12))

# Create buttons with styling
style.configure("TButton", font=("Arial", 12))
rock_button = ttk.Button(root, text="Rock", command=lambda: user_choice("rock"))
paper_button = ttk.Button(root, text="Paper", command=lambda: user_choice("paper"))
scissors_button = ttk.Button(root, text="Scissors", command=lambda: user_choice("scissors"))
play_again_button = ttk.Button(root, text="Play Again", command=reset_game)

# Create feedback widgets
feedback_entry_label = ttk.Label(root, text="Provide Feedback:")
feedback_entry = ttk.Entry(root, width=40)
submit_feedback_button = ttk.Button(root, text="Submit Feedback", command=submit_feedback)
feedback_label = ttk.Label(root, text="", font=("Arial", 12, "italic"))

# Place widgets on the window with alignment
user_label.grid(row=0, column=0, padx=10, pady=10)
rock_button.grid(row=0, column=1, padx=10, pady=10)
paper_button.grid(row=0, column=2, padx=10, pady=10)
scissors_button.grid(row=0, column=3, padx=10, pady=10)
computer_label.grid(row=1, columnspan=4, padx=10, pady=10)
result_label.grid(row=2, columnspan=4, padx=10, pady=10)
user_score_label.grid(row=3, column=0, padx=10, pady=10)
computer_score_label.grid(row=3, column=3, padx=10, pady=10)
play_again_button.grid(row=4, columnspan=4, padx=10, pady=10)

feedback_entry_label.grid(row=5, column=0, padx=10, pady=10)
feedback_entry.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
submit_feedback_button.grid(row=5, column=3, padx=10, pady=10)
feedback_label.grid(row=6, columnspan=4, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
