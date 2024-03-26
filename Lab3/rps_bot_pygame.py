import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 400, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock Paper Scissors")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fonts
font = pygame.font.Font(None, 30)

# Game variables
player_score = 0
bot_score = 0

# Function to determine winner
def determine_winner(player_choice, bot_choice):
    if player_choice == bot_choice:
        return "It's a tie!"
    elif (player_choice == "rock" and bot_choice == "scissors") or \
         (player_choice == "paper" and bot_choice == "rock") or \
         (player_choice == "scissors" and bot_choice == "paper"):
        return "Player wins!"
    else:
        return "Bot wins!"

# Function to generate bot choice
def generate_bot_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to display scores
def display_scores():
    player_score_text = font.render(f"Player: {player_score}", True, BLACK)
    bot_score_text = font.render(f"Bot: {bot_score}", True, BLACK)
    screen.blit(player_score_text, (10, 10))
    screen.blit(bot_score_text, (WIDTH - bot_score_text.get_width() - 10, 10))

# Initial rendering of player and bot choice texts
player_choice_text = font.render("Player: ", True, BLACK)
bot_choice_text = font.render("Bot: ", True, BLACK)

# Main game loop
running = True

while running:
    screen.fill(WHITE)
    display_scores()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if 50 <= mouse_x <= 150 and 100 <= mouse_y <= 200:
                player_choice = "rock"
            elif 150 <= mouse_x <= 250 and 100 <= mouse_y <= 200:
                player_choice = "paper"
            elif 250 <= mouse_x <= 350 and 100 <= mouse_y <= 200:
                player_choice = "scissors"
            else:
                continue

            bot_choice = generate_bot_choice()
            result = determine_winner(player_choice, bot_choice)
            if "Player" in result:
                player_score += 1
            elif "Bot" in result:
                bot_score += 1

            pygame.draw.rect(screen, (200, 200, 200), (50, 100, 300, 100))
            result_text = font.render(result, True, BLACK)
            screen.blit(result_text, (WIDTH//2 - result_text.get_width()//2, 120))
            
            # Update player choice text
            player_choice_text = font.render(f"Player: {player_choice}", True, BLACK)

            # Update bot choice text
            bot_choice_text = font.render(f"Bot: {bot_choice}", True, BLACK)

    # Draw player choice text
    screen.blit(player_choice_text, (10, HEIGHT - 40))

    # Draw bot choice text
    screen.blit(bot_choice_text, (WIDTH - bot_choice_text.get_width() - 10, HEIGHT - 40))

    pygame.draw.rect(screen, (200, 200, 200), (50, 100, 100, 100))  # Rock
    pygame.draw.rect(screen, (200, 200, 200), (150, 100, 100, 100))  # Paper
    pygame.draw.rect(screen, (200, 200, 200), (250, 100, 100, 100))  # Scissors

    rock_text = font.render("Rock", True, BLACK)
    paper_text = font.render("Paper", True, BLACK)
    scissors_text = font.render("Scissors", True, BLACK)

    screen.blit(rock_text, (100 - rock_text.get_width() // 2, 150 - rock_text.get_height() // 2))
    screen.blit(paper_text, (200 - paper_text.get_width() // 2, 150 - paper_text.get_height() // 2))
    screen.blit(scissors_text, (300 - scissors_text.get_width() // 2, 150 - scissors_text.get_height() // 2))

    pygame.display.flip()

pygame.quit()
