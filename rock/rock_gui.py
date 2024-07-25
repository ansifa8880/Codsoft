import random
import tkinter as tk
from tkinter import ttk

class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock-Paper-Scissors")
        master.configure(background="#964B00")
        

        self.user_score = 0
        self.computer_score = 0

        # Create labels for the score
        self.user_score_label = ttk.Label(master, text=f"Your Score: {self.user_score}", background="#964B00")
        self.user_score_label.grid(row=0, column=0, padx=10, pady=10)

        self.computer_score_label = ttk.Label(master, text=f"Computer Score: {self.computer_score}", background="#964B00")
        self.computer_score_label.grid(row=0, column=1, padx=10, pady=10)

        # Create buttons for user choices
        self.rock_button = ttk.Button(master, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.grid(row=1, column=0, padx=10, pady=10)

        self.paper_button = ttk.Button(master, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.grid(row=1, column=1, padx=10, pady=10)

        self.scissors_button = ttk.Button(master, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.grid(row=1, column=2, padx=10, pady=10)

        # Create a quit button
        self.quit_button = ttk.Button(master, text="Quit", command=self.quit_game)
        self.quit_button.grid(row=1, column=3, padx=10, pady=10)

        # Create a label to display the result
        self.result_label = ttk.Label(master, text="", wraplength=400, font=("Arial", 12), foreground="black", background="#964B00")
        self.result_label.grid(row=2, column=0, columnspan=4, padx=10, pady=10)

    def play(self, user_choice):
        """Plays a round of Rock-Paper-Scissors."""

        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Determine the winner
        if user_choice == computer_choice:
            self.result_label.config(text=f"You chose {user_choice} and the computer chose {computer_choice}. It's a tie.")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            self.result_label.config(text=f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
            self.user_score += 1
            self.user_score_label.config(text=f"Your Score: {self.user_score}")
        else:
            self.result_label.config(text=f"You chose {user_choice} and the computer chose {computer_choice}. Computer wins!")
            self.computer_score += 1
            self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def quit_game(self):
        self.result_label.config(text="Thanks for playing ansi!")
        self.rock_button.config(state="disabled")
        self.paper_button.config(state="disabled")
        self.scissors_button.config(state="disabled")
        self.quit_button.config(state="disabled")

# Create the main window
root = tk.Tk()


# Create the game object
game = RockPaperScissorsGUI(root)

# Run the main loop
root.mainloop()