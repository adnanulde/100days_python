print("Welcome to python pizza")

size = input("What size Dou you want? S, M, L. ").upper()

bill = 0
if size == "S":
    bill = 15
    print("Small pizza for $15")
elif size == "M":
    bill = 20
    print("Medium pizza for $20")
else:
    bill = 25 
    print("Large pizza for $25")

add_pepperoni = input("Do you want to add pepperoni? Y or N. ").upper()
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

extra_cheese = input("Do you want to add extra cheese? Y or N. ").upper()
if extra_cheese == "Y":
    bill += 1
print(f"Your total bill is ${bill}")
