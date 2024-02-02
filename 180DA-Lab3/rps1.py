import paho.mqtt.client as mqtt
import random
import time

count = 0

def on_connect(client, userdata, flags, rc):
    print("Connection returned result: " + str(rc))
    client.subscribe("ece180d/jkwon/rps2", qos=1)

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print('Unexpected Disconnect')
    else:
        print('Expected Disconnect')

def on_message(client, userdata, message):
    msg_payload = int(message.payload.decode())
    global count
    # if (msg_payload < 10):
    print('Received message: "' + str(msg_payload) + '" on topic "' + 
            message.topic + '" with QoS ' + str(message.qos))
    count += 1 
    print("Published Counter: ", count)

def get_player_choice():
    choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        choice = input("Enter your choice (rock/paper/scissors): ").lower()
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
    print("Welcome to Rock-Paper-Scissors!")

    player1_choice = get_player_choice()
    print("Waiting for player 2")
    player2_choice = get_player_choice()

    print(f"Player 1 chose {player1_choice}.")
    print(f"Player 2 chose {player2_choice}.")

    result = determine_winner(player1_choice, player2_choice)
    print(result)    

client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect_async('mqtt.eclipseprojects.io')

client.loop_start()

while True: 
    client.publish("ece180d/jkwon/rps1", int (count), qos=1)
    play_rps()
    pass 

# ctrl + c to disconnect
# use disconnect() to disconnect from the broker.
client.loop_stop()
client.disconnect()