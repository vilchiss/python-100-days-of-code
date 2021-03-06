import art

print(art.banner)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '_', '-', '?']

def caesar(text, shift, direction):
    if direction == 'encode':
        shift = len(alphabet) - shift
    new_text = ''
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_text += alphabet[index - shift]
        else:
            new_text += char 
    print(f'The {direction}d text is {new_text}')
   

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction != 'encode' and direction != 'decode':
        print('Invalid option')
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        if shift > len(alphabet):
            shift = shift % len(alphabet)
        caesar(text, shift, direction)
    retry = input("Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if retry != 'yes':
        print(art.bye)
        break
