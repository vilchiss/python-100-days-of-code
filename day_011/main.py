import random
import art

WIN = 0
LOSE = 1
DRAW = 2

def get_card():
    cards = [
        (11, art.CARD_AS),
        (2,art.CARD_TWO),
        (3,art.CARD_THREE),
        (4,art.CARD_FOUR),
        (5,art.CARD_FIVE),
        (6,art.CARD_SIX),
        (7,art.CARD_SEVEN),
        (8,art.CARD_EIGHT),
        (9, art.CARD_NINE),
        (10, art.CARD_TEN),
        (10, art.CARD_J),
        (10, art.CARD_Q),
        (10, art.CARD_K),
    ]

    return random.choice(cards) 

def format_cards(cards):
    text = ''
    for card in cards:
        text += f' [{card}]'

    return text

def get_points(player):
    return sum([c[0] for c in player])

def get_player_status(player, computer):
    player_points = get_points(player)
    computer_points = get_points(computer) 

    if computer_points < 17:
        computer.append(get_card())
        computer_points = get_points(computer) 
    
    if computer_points > 21 or player_points > computer_points:
        return WIN
    elif player_points == computer_points:
        return DRAW
    else:
        return LOSE

def show_status(status):
    if status == LOSE:
        print(f"{art.LOSE} {art.LOSE_FACE}")
    elif status == WIN:
        print(art.WIN)
    else:
        print(art.DRAW)
    
def get_initial_cards():
    cards = []
    for i in range(2):
       cards.append(get_card())
   
    if get_points(cards) == 22:
        cards[1][0] == 1

    return cards
    

def run_game():
    print(art.logo)
    player = get_initial_cards()
    computer = get_initial_cards()

    game_over = False
    player_status = LOSE 
    
    print(f"Your cards: ")
    for c in player:
        print(c[1])
    print(f"Your score is: {get_points(player)}")
    print(f"Computer's first card: \n{computer[0][1]}")

    while not game_over:
        user_input = input("Type 'y' to get another card or 'n' to pass: ")
        if user_input == 'y':
            player_points = get_points(player) 
            new_card = get_card()
            print(new_card[1])
            if new_card[0] == 11:
                new_card = 1 if player_points + new_card > 21 else new_card

            player.append(new_card)
            print(f"Your new score is: {get_points(player)}")
            if get_points(player) > 21:
                player_status = LOSE
                game_over = True
        else:
            player_status = get_player_status(player, computer)
            game_over = True

    print(f"Computer's cards: ")
    for c in computer:
        print(c[1])
    print(f"Computer score: {get_points(computer)}")
    show_status(player_status)

def main():
    run_again = True
    while run_again:
        run_game()
        user_input = input("Run again? Type 'y' or 'n': ")
        if user_input != 'y':
            run_again = False

if __name__ == '__main__':
    main()
