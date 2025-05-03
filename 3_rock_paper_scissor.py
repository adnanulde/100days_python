import random
str_rps = ("Rock, Paper, Scissor")
rps = ["r", "p", "s"]
print(str_rps)

user = input("Choose:- r for rock, p for paper, s for scissor:- ").lower()
if user == "r":
    print(f"You've Selected Rock")
elif user == "p":
    print(f"You've Selected Paper")
elif user == "s":
    print(f"You've Selected Scissor")
else:
    print("Enter correct letter.")


computer = random.choice(rps)
if computer == "r":
    print(f"Computer Selected Rock")
elif computer == "p":
    print(f"Computer Selected Paper")
elif computer == "s":
    print(f"Computer Selected Scissor")


if user == "r" and computer == "s":
    print("You Won!!!")
elif user == "s" and computer == "p":
    print("You Won!!!")
elif user == "p" and computer == "r":
    print("You Won!!!")
elif user == computer:
    print("Tie(*-*)")
else:
    print("You Lost(^_^)")
