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
print(f"You: \n {options[player_choice]}")
computer_choice = random.randint(0, 2)
print(f"Computer: \n {options[computer_choice]}")

if player_choice == computer_choice:
    print("Draw! -_-")
elif player_choice == 0:
    if computer_choice == 1:
        print("You Lose! :(")
    elif computer_choice == 2:
        print("You Win :)")
elif player_choice == 1:
    if computer_choice == 0:
        print("You Win :)")
    elif computer_choice == 2:
        print("You Lose! :(")
elif player_choice == 2:
    if computer_choice == 0:
        print("You Lose! :(")
    elif computer_choice == 1:
        print("You Win :)")
else:
    print("Invalid Option. You lose :(")
