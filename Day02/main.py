print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
pepple = int(input("How many people to slit the bill? "))

each_person_pay = round((total_bill + total_bill * tip / 100) / pepple, 2)
print(f"Each person should pay ${each_person_pay}")