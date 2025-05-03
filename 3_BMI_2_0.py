height = float(input("Enter Your Height in Meter:- "))
weight = int(input("Enter your weight in KG:- "))

calculate = round(weight/(height**2),2)

if calculate <= 18.5:
    print(f"your BMI is:- {calculate},you are under weight")
elif calculate <=25:
    print(f"your BMI is:- {calculate},you are normal weight")
elif calculate <=30:
    print(f"your BMI is:- {calculate},you are slightly overweight")
elif calculate <=35:
    print(f"your BMI is:- {calculate},you are obese") 
else:
    print(f"your BMI is:- {calculate},you are clinically overweight")
