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

game_options = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors."))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. Game over.")
else:
    print(game_options[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer's choice: ")
    print(game_options[computer_choice])
    
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose!")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win!")
    else:
        print("It's a draw!")