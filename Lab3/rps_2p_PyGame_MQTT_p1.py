import pygame
import paho.mqtt.client as mqtt
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Rock Paper Scissors - Player 1")

# Colors, Fonts, and other constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
FONT = pygame.font.Font(None, 36)
BUTTON_COLORS = {
    "normal": GREEN,
    "hover": (0, 220, 0),
    "clicked": (0, 190, 0)
}

# MQTT Configuration
broker_address = "mqtt.eclipseprojects.io"
topic_publish = "rps_game/player1_to_player2"
topic_subscribe = "rps_game/player2_to_player1"

# Global game state variables
opponent_choice = None
player_choice = None
waiting_for_opponent = False
button_pressed = False  # Add this near other global variables
wins = 0
losses = 0

# Initialize MQTT Client
client = mqtt.Client()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic_subscribe, qos=1)

def on_message(client, userdata, msg):
    global opponent_choice, waiting_for_opponent
    opponent_choice = msg.payload.decode()
    waiting_for_opponent = True

client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address)
client.loop_start()

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect(center=(x, y))
    surface.blit(textobj, textrect)

def button(surface, text, x, y, w, h, color_scheme, action=None):
    global player_choice, button_pressed
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    button_color = color_scheme["normal"]
    if button_pressed and player_choice == action:
        button_color = color_scheme["clicked"]
    elif x + w > mouse[0] > x and y + h > mouse[1] > y:
        button_color = color_scheme["hover"]
        if click[0] == 1 and action is not None:
            button_color = color_scheme["clicked"]
            player_choice = action
            button_pressed = True
            client.publish(topic_publish, action, qos=1)

    pygame.draw.rect(surface, button_color, (x, y, w, h))
    draw_text(text, FONT, BLACK, surface, x + w / 2, y + h / 2)


def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and opponent_choice == 'scissors') or \
         (user_choice == 'paper' and opponent_choice == 'rock') or \
         (user_choice == 'scissors' and opponent_choice == 'paper'):
        return "You win!"
    else:
        return "Opponent wins!"

def main():
    global opponent_choice, player_choice, waiting_for_opponent, wins, losses, button_pressed
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if player_choice and opponent_choice:
            result = determine_winner(player_choice, opponent_choice)
            if result == "You win!":
                wins += 1
            elif result == "Opponent wins!":
                losses += 1
            draw_text(f"Your choice: {player_choice}", FONT, GREEN, screen, 320, 200)
            draw_text(f"Opponent's choice: {opponent_choice}", FONT, RED, screen, 320, 240)
            draw_text(result, FONT, BLACK, screen, 320, 280)
            pygame.display.flip()
            pygame.time.delay(2000)
            player_choice, opponent_choice = None, None
            waiting_for_opponent = False
            button_pressed = False  # Reset the button state for the next round
        else:
            button(screen, "Rock", 100, 350, 100, 50, BUTTON_COLORS, "rock")
            button(screen, "Paper", 270, 350, 100, 50, BUTTON_COLORS, "paper")
            button(screen, "Scissors", 440, 350, 100, 50, BUTTON_COLORS, "scissors")

        draw_text(f"Wins: {wins}", FONT, BLACK, screen, 150, 40)
        draw_text(f"Losses: {losses}", FONT, BLACK, screen, 490, 40)

        pygame.display.flip()  # Update the display with any changes
        clock.tick(30)  # Control the frame rate

    pygame.quit()
    client.loop_stop()

if __name__ == "__main__":
    main()
