print("welcome to the tip calculator😄.")
total_bill = input("what was the total bill ? $")
tip = float(total_bill) * (float(input("what percentage tip would you like to give ? 10,12, or 15? "))/ 100)
print(f"tip will be {tip}")
total = float(total_bill) + float(tip)

num_of_people = input("how many people to split the bill ? ")

print(f"each person should pay : ${round(float(total) / float(num_of_people), 2)}")
