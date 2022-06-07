import art
import random


HARD_ATTEMPTS = 5
EASY_ATTEMPTS = 10


def show_result(is_winner):
    if is_winner:
        print(art.win_logo)
    else:
        print(f"The number was: {number}")
        print(art.lose_logo)
  
def select_mode():
    while True:
        mode = input("Type 'easy' or 'hard' to select mode: ").strip()
        if mode == 'easy':
            return EASY_ATTEMPTS
        elif mode == 'hard':
            return HARD_ATTEMPTS
        else:
            print('Invalid input. Please select a valid mode')

def get_guess():
    while True:
        guess = int(input('Make a guess: '))
        if guess > 0 and guess <= 100:
            return guess
        else:
            print("Your guess is out of range. Please try again...")


    

def play_game():
    print(art.logo)
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 100)

    attempts = select_mode()

    is_winner = False
    while attempts > 0 and not is_winner:
        print(f"You have {attempts} to remaingin to guess the number")
        guess = get_guess() 
        if guess == number:
            is_winner = True
        if guess > number:
            print("Too high!")
        else:
            print("Too low!")
        
        if not is_winner:
            print("Guess again")
        attempts -= 1
        
    show_result(is_winner)

   
def main():
    while True:
        play_game()
        repeat_game = input("Try again? Type 'y' or 'n': ")
        if repeat_game != 'y':
            break

if __name__ == '__main__':
    main()
    
