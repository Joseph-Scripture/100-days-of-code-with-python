alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(plain_text, shift_amount):
    for letter in plain_text:
        index_of_letters = alphabet.index(letter)
        new_letter = index_of_letters + shift_amount
        print(alphabet[new_letter], end='')


def decrypt(new_word, shift_amount):
    for letter in new_word:
        index_of_letter = alphabet.index(letter)
        new_indexed_letters = index_of_letter - shift_amount
        word = alphabet[new_indexed_letters]
        print(word, end='')


if direction == 'encode':
    encrypt(plain_text=text, shift_amount=shift)

elif direction == 'decode':
    decrypt(new_word=text, shift_amount=shift)
