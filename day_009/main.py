from getpass import getpass
import art

print(art.logo)
bidders = {}
more_players = True

while more_players:
    name = input("What is yout name: \n")
    bid = getpass("What is bid: \n$")
    bidders[name] = int(bid)
    answer = input("Are there any other bidders? Type 'yes' or 'no'\n")
    if answer != 'yes':
        more_players = False
winner = ''
for name in bidders:
    if winner == '':
        winner = name
    if bidders[name] > bidders[winner]:
        winner = name

print(f"The winner is {winner} with a bid of ${bidders[winner]}.")
