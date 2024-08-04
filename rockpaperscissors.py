#This is rock paper scissors game using python
#The game allows the user to play multiple rounds of rock, paper, scissors against the computer.
#The game keeps track of the number of games won by the user and the computer.
#The game displays the total number of games won by the user and the computer at the end of each round.
#The game uses the random module to generate a random choice for the computer.
#The game is written in Python.
#************************CODE************************
import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

def display_title():
    print("ROCK PAPER SCISSORS GAME")
    print()

def get_name():
    player_name = input("What is your name? ")
    print(f"Hello {player_name}! Welcome to my game")
    print()

def play_game():
    global user_wins, computer_wins
    
    while True:
        user_input = input("Enter your choice: rock, paper or scissors or Q to quit: ").lower()
        if user_input == 'q':
            break
        if user_input not in options:
            print("Invalid input")
            continue
        
        random_number = random.randint(0, 2)
        computer_pick = options[random_number]
        print("Computer picked:", computer_pick)
        
        if user_input == 'rock' and computer_pick == 'scissors':
            print("You won")
            user_wins += 1
        elif user_input == 'paper' and computer_pick == 'rock':
            print("You won")
            user_wins += 1
        elif user_input == 'scissors' and computer_pick == 'paper':
            print("You won")
            user_wins += 1
        else:
            print("You lost")
            computer_wins += 1

def main():
    display_title()
    get_name()
    play_game()

if __name__ == "__main__":
    main()

print("You won " + str(user_wins) + " times")
print("Computer won " + str(computer_wins) + " times")
print("Thanks for playing")
