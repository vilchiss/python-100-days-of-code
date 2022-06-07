import art
import random

print(art.logo)

HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10



print("I'm thinking of a number between 1 and 100")
number = random.randint(1, 100)

mode = input("Type 'easy' or 'hard' to select mode: ")
if mode == 'easy':
    attempts = EASY_ATTEMPTS
else:
    attempts = HARD_ATTEMPTS

is_game_over = False
is_winner = False
while attempts > 0 and not is_winner:
    print(f"You have {attempts} to remaingin to guess the number")
    guess = int(input('Make a guess: '))
    if guess == number:
        is_winner = True
    if guess > number:
        print("Too high!")
    else:
        print("Too low!")
    
    if not is_winner:
        print("Guess again")
    attempts -= 1

if is_winner:
    print(art.win_logo)
else:
    print(f"The number was: {number}")
    print(art.lose_logo)
        
    
    
