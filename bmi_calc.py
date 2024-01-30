# BMI calculator
print("*"*5 + " BMI calculator " + "*"*5)
# Height set to right data type
height = float(input("What is your height? (ex. 1.65)\n"))
# Weight set to right data type
weight = int(input("What is your weight? (ex. 60)\n"))
# Calculations
bmi = weight / height ** 2
if bmi < 18.5:
    print(f"Your BMI is {bmi:.2f}, you are under weight.")
elif bmi < 25:
    print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi:.2f}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi:.2f}, you are obese.")
else:
    print(f"Your BMI is {bmi:.2f}, you are clinically obese")



