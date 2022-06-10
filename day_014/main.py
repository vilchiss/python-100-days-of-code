import art
import game_data
import random


def run_game():
    is_loser = False
    score = 0
    index_a, item_a = get_item()
    while not is_loser:
        print(art.logo)
        if score > 0:
            print(f"You're right! Current score: {score}")

        index_b = index_a
        while index_a == index_b:
            index_b, item_b = get_item()

        print(f"Hint A: {item_a['follower_count']} B: {item_b['follower_count']}")
        print(f"Compare A: {format_item(item_a)}")
        print(art.vs)
        print(f"Compare B: {format_item(item_b)}\n")
        answer = get_user_answer()
        correct_answer = get_correct_answer(item_a, item_b)

        if answer != correct_answer:
            is_loser = True
            print(f"Sorry, that's wrong. Final score: {score}")
        else:
            index_a = index_b
            item_a = item_b
            score += 1
            
def get_item():
    size_data = len(game_data.data)
    index = random.randint(0, size_data - 1)
    item = game_data.data[index]
    return index, item
    

def get_user_answer():
    while True: 
        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer == 'A' or answer == 'B':
            return answer
        print("Invalid input, try again...")


def get_correct_answer(item_a, item_b):
    followers_a = item_a["follower_count"]
    followers_b = item_b["follower_count"]
    if followers_a > followers_b:
        return 'A'
    else:
        return 'B'

def format_item(person):
    name = person['name']
    description = person['description']
    country = person['country']
    return f'{name}, a {description}, from {country}'

def main():
    while True:
        run_game()
        user_response = input("Try again? Type 'y' or 'n': ")
        if user_response != 'y':
            break

if __name__ == '__main__':
    main()
