print("Welcome to tip calculator")

bill_amt = float(input("What's was the total Bill? $"))
tip_percnt = int(input("How much tip would you like to give? 10, 12, 15?"))
bill_tip_cal = tip_percnt/100 * bill_amt + bill_amt
# bill_12 = 1.12 / 100 * bill_amt(error), didn't add bill_amt
# bill_15 = 1.15 * bill_amt(error)

split = int(input("How many people to split the bill? "))
cal_splt = bill_tip_cal/split
# round_bill = (round(cal_splt,2)) -> logic, round_bill put in f string. I use the logic directly in f string
print(f"Each person should pay ${(round(cal_splt,2))}")
