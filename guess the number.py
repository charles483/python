import random
HARD_LEVEL_ATTEMPS=10
EASY_LEVEL_ATTEMPTS=5
MEDIUM_LEVEL_ATTEMPTS=7
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='medium':  # Add condition here
        return MEDIUM_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPS

print("guesse a number between 1 and 100")
answer=random.randint(1,100)
print(answer)
level=input(" Choose a level ... type 'Easy', 'Medium' or 'hard':")
attempt=set_difficulty(level)
print(f"yoy have {attempt} attemps remaining")
guess=0
while guess != answer:
    guess=int(input("Make a guess: "))
    if guess==answer:
        print(f"you got it! The answer was {answer}")
        break
    elif guess>answer:
        print("Too high")
        attempt-=1
        print(f"you have {attempt} attempts remaining")
    elif guess<answer:
        print("Too low")
        attempt-=1
        print(f"you have {attempt} attempts remaining")
    if attempt==0:
        print("you have run out of attempts, you lose")
        break
    elif guess!=answer:
        print("guess again")
    else:
        print("you have run out of attempts, you lose")
        break
