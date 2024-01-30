# BMI calculator
print("*"*5 + " BMI calculator " + "*"*5)
# Height set to right data type
height = float(input("What is your height? (ex. 1.65)\n"))
# Weight set to right data type
weight = int(input("What is your weight? (ex. 60)\n"))
# Calculations
bmi = weight / height ** 2
print(f"Your BMI: {bmi:.2f}")
if bmi < 18.5:
    print("You are under weight.")
elif bmi >= 18.5:
    print("You have normal weight.")
elif bmi >= 25:
    print("You are slightly overweight.")
elif bmi >= 30:
    print("You are obese.")
else:
    print("You are clinically obese")



