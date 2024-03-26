import random

# Game variables (global)
player_score = 0
opponent_score = 0

# Mapping for choices
choice_mapping = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

# Main game loop
def play_rps_simulated():
    global player_score, opponent_score  # Declare as global variables
    
    choices = list(choice_mapping.keys())  # Use keys of choice_mapping
    
    while True:
        user_choice = input("Enter rock (R), paper (P), or scissors (S) (or 'Q' to exit): ").lower()
        
        if user_choice == 'q':
            print("Exiting game.")
            break
        
        if user_choice not in choices:
            print("Invalid choice. Please choose R, P, or S.")
            continue
        
        # Simulate opponent's move
        opponent_choice = random.choice(choices)
        
        # Compute result
        if user_choice == opponent_choice:
            result = "It's a tie!"
        elif (user_choice == 'r' and opponent_choice == 's') or \
             (user_choice == 'p' and opponent_choice == 'r') or \
             (user_choice == 's' and opponent_choice == 'p'):
            result = "Player wins!"
            player_score += 1
        else:
            result = "Opponent wins!"
            opponent_score += 1
        
        print("Player's choice:", choice_mapping[user_choice])
        print("Opponent's choice:", choice_mapping[opponent_choice])
        print("Result:", result)
        print("Player Score:", player_score)
        print("Opponent Score:", opponent_score)
        print()

play_rps_simulated()  # Start the simulated game
