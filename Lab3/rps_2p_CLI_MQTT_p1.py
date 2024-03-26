import paho.mqtt.client as mqtt
import time

# Global variables
opponent_choice = None
wins = 0
losses = 0

# MQTT Configuration
broker_address = "mqtt.eclipseprojects.io"
topic_publish = "rps_game/player1_to_player2"  # Topic to publish player's choice
topic_subscribe = "rps_game/player2_to_player1"  # Topic to subscribe for opponent's choice

# Initialize MQTT Client
client = mqtt.Client()

# Callback when connecting to the MQTT broker
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic_subscribe, qos=1)

# Callback when a PUBLISH message is received from the server
def on_message(client, userdata, msg):
    global opponent_choice
    opponent_choice = msg.payload.decode()

# Set MQTT client callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(broker_address)
client.loop_start()

# Revised function to determine the winner and print choices
def determine_winner(user_choice, opponent_choice):
    global wins, losses
    # Mapping single letters to full choice names
    choices_full = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    user_choice_full = choices_full[user_choice]
    opponent_choice_full = choices_full[opponent_choice]

    # Printing both players' choices
    print(f"Your choice: {user_choice_full.capitalize()}\nOpponent's choice: {opponent_choice_full.capitalize()}")

    if user_choice == opponent_choice:
        result = "It's a tie!"
    elif (user_choice == 'r' and opponent_choice == 's') or \
         (user_choice == 'p' and opponent_choice == 'r') or \
         (user_choice == 's' and opponent_choice == 'p'):
        wins += 1
        result = "You win!"
    else:
        losses += 1
        result = "Opponent wins!"
    return result


# Main game loop
def main():
    global opponent_choice
    choices_full = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    while True:
        user_choice = input("Choose rock (r), paper (p), or scissors (s) (or 'q' to quit): ")
        if user_choice == 'q':
            break
        if user_choice not in ['r', 'p', 's']:
            print("Invalid choice.")
            continue

        client.publish(topic_publish, user_choice, qos=1)
        print("Waiting for the opponent's choice...")
        while opponent_choice is None:
            time.sleep(1)  # Simple way to wait for the opponent's choice

        result = determine_winner(user_choice, opponent_choice)
        print(result)
        print(f"Wins: {wins}, Losses: {losses}")
        opponent_choice = None  # Reset for the next round

if __name__ == "__main__":
    main()
