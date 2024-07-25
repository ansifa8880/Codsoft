import random

def play_rock_paper_scissors():
    """Plays a game of Rock-Paper-Scissors with the user."""

    user_score = 0
    computer_score = 0

    while True:
        # Get user input
        user_choice = input("Choose rock, paper, or scissors: ").lower()

        # Validate user input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue

        # Generate computer's choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Determine the winner
        if user_choice == computer_choice:
            print(f"You chose {user_choice} and the computer chose {computer_choice}. It's a tie.")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print(f"You chose {user_choice} and the computer chose {computer_choice}. You win!")
            user_score += 1
        else:
            print(f"You chose {user_choice} and the computer chose {computer_choice}. Computer wins!")
            computer_score += 1

        # Display the scores
        print(f"Current score: You: {user_score}, Computer: {computer_score}")

        # Ask if the user wants to play again
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")

# Call the function to start the game
play_rock_paper_scissors()

