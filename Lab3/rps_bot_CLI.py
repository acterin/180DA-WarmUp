import random

def play_rps():
    choices = ['r', 'p', 's']
    choices_words = ['Rock', 'Paper', 'Scissors']
    rounds = 0
    
    while True:
        rounds += 1
        print(f"\nRound {rounds}:")
        
        user_choice = input("Enter rock (R), paper (P), or scissors (S) (or 'Q' to exit): ").lower()
        
        if user_choice == 'q':
            print("Thanks for playing!")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == "r" and computer_choice == "s") or \
             (user_choice == "p" and computer_choice == "r") or \
             (user_choice == "s" and computer_choice == "p"):
            result = "You win!"
        else:
            result = "You lose!"
            
        print(f"Your choice: {choices_words[choices.index(user_choice)]}. Computer's choice: {choices_words[choices.index(computer_choice)]}. {result}")
        
        while True:
            play_again = input("Do you want to play again? (Y/N): ").lower()
            if play_again == 'y':
                break
            elif play_again == 'n':
                print("Thanks for playing!")
                exit()  # Exiting the program when the user chooses not to play again
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

# To play the game, call play_rps().
play_rps()
