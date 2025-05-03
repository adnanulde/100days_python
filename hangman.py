import random

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

blanks = []
for letters in chosen_word:
    blanks += "_"
print(blanks)

guess = input("Guess the letter: ").lower()

for letter in chosen_word:
    if guess == letter:
        print("True")
    else:
        print("False")
