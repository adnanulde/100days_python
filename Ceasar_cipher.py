alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# #Encyrption
# def encrypt(original_text, shift_amt):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_amt
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]

#     print(f"Here is the Encoded result: {cipher_text}")

# # encrypt(original_text=text,shift_amt=shift)

# #Decryption
# def decrypt(original_text, shift_amt):
#     output_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_amt
#         shifted_position %= len(alphabet)
#         output_text += alphabet[shifted_position]
#     print(f"Here is the Encoded result: {output_text}")

# decrypt(original_text=text,shift_amt=shift)

def ceasar(original_text, shift_amt,encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amt *= -1
    for letter in original_text:

        if letter not in alphabet:
            cipher_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amt
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {cipher_text}")

should_continue = True

while should_continue:
    directon = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(original_text=text,shift_amt=shift,encode_or_decode=directon)
    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye.")