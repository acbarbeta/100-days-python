# 100 Days of Python - Day 02

TIP_VALID_VALUES = [10, 12, 15]

greeting = print("Welcome to the tip calculator!")

total_bill_value = float(input("What was the total bill? $"))
tip_percentage_value = int(input("What percentage would you like to give? 10, 12 or 15?"))
total_people = int(input("How many people to split the bill?"))

if tip_percentage_value not in TIP_VALID_VALUES:
    print("Please, insert a valid value")

final_tip_amount = total_bill_value * tip_percentage_value / 100
value_per_person = (total_bill_value + final_tip_amount) / total_people

print(f"Each person should pay ${round(value_per_person, 2)}")