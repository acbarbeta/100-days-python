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

left_or_right_option = input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'.")

if left_or_right_option == 'left':
    swim_or_wait_option = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    if swim_or_wait_option == 'wait':
        door_option = input("You arrive at the island unhamed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")
        if door_option == 'red':
            print("You were burned by fire. Game over.")
        elif door_option == 'blue':
            print("You were eaten by beasts. Game over.")
        elif door_option == 'yellow':
            print("CONGRATULATIONS, YOU FOUND THE TREASURE! YOU WIN!")
        else:
            print("Game over.")
    else:
        print("Oh no! You were attacked by a trout! Game over.")
else:
    print("You fall into a hole. Game over.")