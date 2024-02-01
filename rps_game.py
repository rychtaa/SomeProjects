import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice >=3 or choice < 0:
    print("Wrong number! Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    exit()
else:
    print(game_images[choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")
print(game_images[computer_choice])
"""
rock > scissors
scissors > paper
paper > rock
"""
if choice == computer_choice:
    print("It's a draw.")
elif choice == 0 and computer_choice == 2:
    print("You won!")
elif choice == 2 and computer_choice == 1:
    print("You won!")
elif choice == 1 and computer_choice == 0:
    print("You won!")
else:
    print("You lose!")
