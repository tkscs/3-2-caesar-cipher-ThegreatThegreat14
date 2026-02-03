import string
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"

plaintext = "this is a secret message"
key = 1

ciphertext = ""
for character in plaintext:
    if character == " ":
        encrypted_character = " "
        ciphertext += encrypted_character
    else:
        index = alphabet.index(f"{character}")
        encrypted_character = alphabet[index+key]
        ciphertext += encrypted_character

print(f"{ciphertext = }")