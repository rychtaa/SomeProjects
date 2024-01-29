# Tip calculator

print("***** Tip calculator *****")

# Ask a user how much was the total bill

bill = float(input("What was the total bill?\n" + "€"))

# Ask user how big tip they want to give

tip = int(input("What pecentage tip would you like to give? 10, 12, 15?\n" "Type in just a number\n" + "%"))

# Ask user how many peaple thay want to split a bill for

total_people = int(input("How many people to split the bill?\n"))

# Count how much each person needs to pay

each_pays = float((bill + (bill * tip / 100)) / total_people)

# Tell user how much each person needs to pay

print(f"Each person should pay: €{each_pays:.2f}")
