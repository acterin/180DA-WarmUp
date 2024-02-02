import tkinter as tk

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice:
        return "It's a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \
         (player1_choice == "paper" and player2_choice == "rock") or \
         (player1_choice == "scissors" and player2_choice == "paper"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

def play_rps(player1_choice, player2_choice):
    result = determine_winner(player1_choice, player2_choice)
    result_label.config(text=result)
    player1_choice_label.config(text=f"Player 1 chose: {player1_choice}")
    player2_choice_label.config(text=f"Player 2 chose: {player2_choice}")
    if "Player 1 wins" in result:
        player1_score_var.set(player1_score_var.get() + 1)
    elif "Player 2 wins" in result:
        player2_score_var.set(player2_score_var.get() + 1)

def on_player1_choice(choice):
    player1_choice_var.set(choice)
    player1_rock_btn.config(state="disabled")
    player1_paper_btn.config(state="disabled")
    player1_scissors_btn.config(state="disabled")
    if player2_choice_var.get():
        play_rps(choice, player2_choice_var.get())

def on_player2_choice(choice):
    player2_choice_var.set(choice)
    player2_rock_btn.config(state="disabled")
    player2_paper_btn.config(state="disabled")
    player2_scissors_btn.config(state="disabled")
    if player1_choice_var.get():
        play_rps(player1_choice_var.get(), choice)

def rematch():
    player1_choice_var.set("")
    player2_choice_var.set("")
    result_label.config(text="")
    player1_choice_label.config(text="")
    player2_choice_label.config(text="")
    player1_rock_btn.config(state="normal")
    player1_paper_btn.config(state="normal")
    player1_scissors_btn.config(state="normal")
    player2_rock_btn.config(state="normal")
    player2_paper_btn.config(state="normal")
    player2_scissors_btn.config(state="normal")

def reset_scores():
    player1_score_var.set(0)
    player2_score_var.set(0)

root = tk.Tk()
root.title("Rock Paper Scissors")

player1_choice_var = tk.StringVar()
player2_choice_var = tk.StringVar()

player1_score_var = tk.IntVar()
player2_score_var = tk.IntVar()

player1_score_label = tk.Label(root, text="Player 1's Score:")
player1_score_label.grid(row=0, column=0)
player1_score_display = tk.Label(root, textvariable=player1_score_var)
player1_score_display.grid(row=0, column=1)

player2_score_label = tk.Label(root, text="Player 2's Score:")
player2_score_label.grid(row=0, column=2)
player2_score_display = tk.Label(root, textvariable=player2_score_var)
player2_score_display.grid(row=0, column=3)

player1_choice_label = tk.Label(root, text="Player 1's Choice:")
player1_choice_label.grid(row=1, column=0)

player1_rock_btn = tk.Button(root, text="Rock", command=lambda: on_player1_choice("rock"))
player1_rock_btn.grid(row=1, column=1)

player1_paper_btn = tk.Button(root, text="Paper", command=lambda: on_player1_choice("paper"))
player1_paper_btn.grid(row=1, column=2)

player1_scissors_btn = tk.Button(root, text="Scissors", command=lambda: on_player1_choice("scissors"))
player1_scissors_btn.grid(row=1, column=3)

player2_choice_label = tk.Label(root, text="Player 2's Choice:")
player2_choice_label.grid(row=2, column=0)

player2_rock_btn = tk.Button(root, text="Rock", command=lambda: on_player2_choice("rock"))
player2_rock_btn.grid(row=2, column=1)

player2_paper_btn = tk.Button(root, text="Paper", command=lambda: on_player2_choice("paper"))
player2_paper_btn.grid(row=2, column=2)

player2_scissors_btn = tk.Button(root, text="Scissors", command=lambda: on_player2_choice("scissors"))
player2_scissors_btn.grid(row=2, column=3)

rematch_btn = tk.Button(root, text="Rematch", command=rematch)
rematch_btn.grid(row=3, column=0)

reset_scores_btn = tk.Button(root, text="Reset Scores", command=reset_scores)
reset_scores_btn.grid(row=3, column=1)

result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=4)

root.mainloop()