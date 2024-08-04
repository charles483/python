#************************GUESS THE NUMBER GAME IN PYTHON************************
#This is a simple game that allows the user to guess a number between 1 and 10, 1 and 100, or 1 and 1000 depending on the level of difficulty chosen by the user. The user has a limited number of tries to guess the number correctly. The game also keeps track of the number of games won by the user. The user can choose to play the game again after each round.
#The game consists of the following functions:
#display_title(): This function displays the title of the game.
#get_name(): This function asks the user for their name and displays a welcome message.
#play_game(wins): This function allows the user to play the game by choosing a level of difficulty (easy, medium, or hard) and guessing the number. The function returns the number of games won by the user.
#main(): This function calls the display_title(), get_name(), and play_game(wins) functions to run the game.
#The main function also allows the user to play the game again after each round.
#The game uses the random module to generate a random number for the user to guess.
#The game also uses a while loop to allow the user to play multiple rounds of the game.
#The game keeps track of the number of games won by the user and displays the total number of games won at the end of each round.
#The game ends when the user chooses not to play again.
#The game displays a goodbye message when the user decides to stop playing.
#The game is written in Python.
#************************CODE************************
import random
def display_title():
    print("GUES THE NUMBER GAME ")
    print()
def get_name():
    player_name= input("what is your name?")
    print(f"hello {player_name}! welcome to my game")
print()
def play_game(wins):
    level=input("what game level would you like to play? (e. easy, m. medium, h. hard):")
    
    if level.lower()=='e':
        max_number=10
        tries=5
    elif level.lower()=='m':
        max_number=100
        tries=10
    elif level.lower()=='h':
        max_number=1000
        tries=15
    else:
        print("invalid input please try agin later ")
        return  
    number= random.randint(1,max_number)
    print("I'M thinking of a number between 1 to " + str(max_number)+"\n")
    count=1
    while count<=tries:
      guess=int(input("what is your guess?"))
      if guess<number:
            print("Too low ")
            count+=1
      elif guess>number:
          print("Guess too high")
          count+=1
      elif guess==number:
          print("you gussed it in "+ str(count)+"tries"+"\n")
          wins+=1
          print("you have won "+str(wins)+" "+"game(s)"+"\n")
          return wins
    else:
        print("you have exhausted all your tries")
        print("the number i was thinking of was "+str(number)+"\n")
    
def main():
    display_title()
    get_name()
    wins=0
    again="y"
    while  again.lower()=="y":
        wins=play_game(wins)
        again=input("Do you want to play again? (y/n): ")
        print()
    print("BYE!")
    
if __name__=="__main__":
        main()
print("Thanks for playing and welcome back again")
        