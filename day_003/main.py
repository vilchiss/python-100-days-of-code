print('''
                          /\          /\
                         ( \\        // )
                          \ \\      // /
                           \_\\||||//_/
                            \/ _  _ \
                           \/|(O)(O)|
                          \/ |      |
      ___________________\/  \      /
     //                //     |____|
    //                ||     /      \
   //|                \|     \ 0  0 /
  // \       )         V    / \____/
 //   \     /        (     /
""     \   /_________|  |_/
       /  /\   /     |  ||
      /  / /  /      \  ||
      | |  | |        | ||
      | |  | |        | ||
      |_|  |_|        |_||
       \_\  \_\        \_\\
''')
print('Welcome to Donkey Island.')
print('Your mission is to find the donkey.') 
movement = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if movement == 'left':
    action = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" for wait to a boat. Type "swim" to swim across\n').lower()
    if action == 'wait':
        color = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n')
        if color == 'yellow':
            print('YOU WIN!!!')
        elif color == 'blue':
            print('Eaten by beasts. Game Over.')
        elif color == 'red':
            print('Burned by fire. Game Over.')
        else:
            print('Game Over.')
    else:
        print('Attacked by trout. Game Over.')
else:
    print('Fall into hole. Game Over.')
