print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You are at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")
if choice1 == "left":
    pass
else:
    print("You fall into a hole. GAME OVER! 😒")

choice2 = input("You got to a river. Do you want to swim across or wait for a boat? Type \"swim\" or \"wait\"\n")
if choice2 == "swim":
    print("You were attacked by trout. GAME OVER! 😒")
else:
    pass
choice3 = input("You came to a wall with 3 door. Which door do you choose? Type \"red\" or \"yellow\" or \"green\"\n")
if choice3 == "red":
    print("You were burned by fire. GAME OVER! 😒")
elif choice3 == "yellow":
    print("There is your treasure!!! 💎💎💎 You WIN! 😅")
elif choice3 == "green":
    print("You were eaten by bats. GAME OVER! 😒")
else:
    print("GAME OVER! 😒")
