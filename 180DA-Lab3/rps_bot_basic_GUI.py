import tkinter as tk
import random

def determine_winner(player_choice, bot_choice):
    if player_choice == bot_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and bot_choice == "scissors") or \
         (player_choice == "paper" and bot_choice == "rock") or \
         (player_choice == "scissors" and bot_choice == "paper"):
        return "Player 1 wins!"
    else:
        return "Bot wins!"

def generate_bot_choice():
    return random.choice(["rock", "paper", "scissors"])

def play_rps(player_choice):
    bot_choice = generate_bot_choice()
    result = determine_winner(player_choice, bot_choice)
    result_label.config(text=result)
    player_choice_label.config(text=f"Player 1 chose: {player_choice}")
    bot_choice_label.config(text=f"Bot chose: {bot_choice}")
    if "Player 1 wins" in result:
        player1_score_var.set(player1_score_var.get() + 1)
    elif "Bot wins" in result:
        bot_score_var.set(bot_score_var.get() + 1)

def on_player1_choice(choice):
    player1_choice_var.set(choice)
    play_rps(choice)

def rematch():
    player1_choice_var.set("")
    result_label.config(text="")
    player_choice_label.config(text="")
    bot_choice_label.config(text="")
    player1_rock_btn.config(state="normal")
    player1_paper_btn.config(state="normal")
    player1_scissors_btn.config(state="normal")
    bot_score_var.set(0)

def reset_scores():
    player1_score_var.set(0)
    bot_score_var.set(0)

root = tk.Tk()
root.title("Rock Paper Scissors")

player1_choice_var = tk.StringVar()
player1_score_var = tk.IntVar()
bot_score_var = tk.IntVar()

player1_score_label = tk.Label(root, text="Player 1's Score:")
player1_score_label.grid(row=0, column=0)
player1_score_display = tk.Label(root, textvariable=player1_score_var)
player1_score_display.grid(row=0, column=1)

bot_score_label = tk.Label(root, text="Bot's Score:")
bot_score_label.grid(row=0, column=2)
bot_score_display = tk.Label(root, textvariable=bot_score_var)
bot_score_display.grid(row=0, column=3)

player_choice_label = tk.Label(root, text="")
player_choice_label.grid(row=1, columnspan=2)

bot_choice_label = tk.Label(root, text="")
bot_choice_label.grid(row=1, column=2, columnspan=2)

player1_choice_label = tk.Label(root, text="Player 1's Choice:")
player1_choice_label.grid(row=2, column=0)

player1_rock_btn = tk.Button(root, text="Rock", command=lambda: on_player1_choice("rock"))
player1_rock_btn.grid(row=2, column=1)

player1_paper_btn = tk.Button(root, text="Paper", command=lambda: on_player1_choice("paper"))
player1_paper_btn.grid(row=2, column=2)

player1_scissors_btn = tk.Button(root, text="Scissors", command=lambda: on_player1_choice("scissors"))
player1_scissors_btn.grid(row=2, column=3)

rematch_btn = tk.Button(root, text="Rematch", command=rematch)
rematch_btn.grid(row=4, column=0)

reset_scores_btn = tk.Button(root, text="Reset Scores", command=reset_scores)
reset_scores_btn.grid(row=4, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=5, columnspan=4)

root.mainloop()