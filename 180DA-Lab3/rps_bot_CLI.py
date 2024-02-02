import random

def get_player_choice(player_num):
    choice = input(f"Player {player_num}, enter your choice (rock/paper/scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input(f"Player {player_num}, enter your choice (rock/paper/scissors): ").lower()
    return choice

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "paper" and player2_choice == "rock") or \
         (player1_choice == "scissors" and player2_choice == "paper"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_rps():
    player1_score = 0
    player2_score = 0

    while True:
        print("\nCurrent Score:")
        print(f"Player 1: {player1_score}")
        print(f"Player 2: {player2_score}")

        print("\nWelcome to Rock-Paper-Scissors!")

        player1_choice = get_player_choice(1)
        player2_choice = get_player_choice(2)

        print(f"Player 1 chose {player1_choice}.")
        print(f"Player 2 chose {player2_choice}.")

        result = determine_winner(player1_choice, player2_choice)
        print(result)

        if "Player 1 wins" in result:
            player1_score += 1
        elif "Player 2 wins" in result:
            player2_score += 1

        option = input("\nDo you want to play again? (1: Yes, 2: Reset Score, 3: Quit): ")
        if option == "2":
            player1_score = 0
            player2_score = 0
            print("Scores reset.")
        elif option == "3":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_rps()