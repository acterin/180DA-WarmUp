import random

class RPSBot:
    def __init__(self):
        self.states = ['rock', 'paper', 'scissors']
        self.transitions = {'rock': {'rock': 'draw', 'paper': 'lose', 'scissors': 'win'},
                            'paper': {'rock': 'win', 'paper': 'draw', 'scissors': 'lose'},
                            'scissors': {'rock': 'lose', 'paper': 'win', 'scissors': 'draw'}}
        self.user_score = 0
        self.bot_score = 0

    def get_user_input(self):
        user_input = input("Enter your choice (rock/paper/scissors): ").lower()
        while user_input not in self.states:
            print("Invalid input. Please enter rock, paper, or scissors.")
            user_input = input("Enter your choice (rock/paper/scissors): ").lower()
        return user_input

    def generate_bot_action(self):
        return random.choice(self.states)

    def play_round(self, user_choice, bot_choice):
        result = self.transitions[user_choice][bot_choice]
        print(f"You chose {user_choice}. Bot chose {bot_choice}. Result: {result.capitalize()}")
        if result == 'win':
            self.user_score += 1
        elif result == 'lose':
            self.bot_score += 1

    def print_scores(self):
        print(f"User Score: {self.user_score} | Bot Score: {self.bot_score}")

    def run_game(self):
        while True:
            user_choice = self.get_user_input()
            bot_choice = self.generate_bot_action()
            self.play_round(user_choice, bot_choice)
            self.print_scores()
            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                print("Thanks for playing! Final Scores:")
                self.print_scores()
                break

if __name__ == "__main__":
    rps_bot = RPSBot()
    rps_bot.run_game()