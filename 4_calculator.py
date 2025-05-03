def add(n1,n2):
    return n1+n2

def substract(n1,n2):
    return n1-n2

def divide(n1,n2):
    return n1/n2

def multiply(n1,n2):
    return n1*n2

operations = {
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
}

# print (operations["*"](4,8))

def calculator():
    num1 = float(input("Enter first number: "))

    should_accumulate = True
    while should_accumulate:
        for i in operations:
            print(i)
        opr = input("Choose an operation: ")
        num2 = float(input("Enter second number: "))
        ans = (operations[opr]( num1, num2))

        print(f"{num1} {opr} {num2} = {ans}")

        choice = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start again: ")

        if choice == "y":
            num1 = ans
        else: 
            should_accumulate = False
            print("\n"*20)
            calculator()
        
calculator()
