import random
import hangman_art as art
import hangman_words as words

MASK_CHAR = '_'
lives = 6
end_of_game = False
guessed = set()

word = random.choice(words.word_list)
word_size = len(word)
display = [MASK_CHAR]*word_size

print(art.banner)

print(art.stages[lives])
print(" ".join(display))

while not end_of_game:
    guess = input("Try to guess a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Bad input, try again...")
        continue

    if guess in guessed:
        print('You already tried with that letter, try again....')
        continue
    else:
        guessed.add(guess)

    if guess in word:
        for i in range(word_size):
            if word[i] == guess:
                display[i] = guess
    else:
        print(f'You guessed {guess}, that\'s not in the word. You lose a life.')
        lives -= 1
    
    print(art.stages[lives])
    print(" ".join(display))
    
    if MASK_CHAR not in display:
        print(art.you_win)
        end_of_game = True

    if lives == 0:
        print(art.game_over)
        end_of_game = True

