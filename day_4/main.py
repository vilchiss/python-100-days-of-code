import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(f"You: \n {options[player_choice - 1]}")
computer_choice = random.randint(1, len(options))
print(f"Computer: \n {options[computer_choice - 1]}")

if player_choice == computer_choice:
    print("Drawn! -_-")
elif player_choice == 1:
    if computer_choice == 2:
        print("You Lose! :(")
    elif computer_choice == 3:
        print("You Win :)")
elif player_choice == 2:
    if computer_choice == 1:
        print("You Win :)")
    elif computer_choice == 3:
        print("You Lose! :(")
elif player_choice == 3:
    if computer_choice == 1:
        print("You Lose! :(")
    elif computer_choice == 2:
        print("You Win :)")
else:
    print("Invalid Option. You lose :(")
