print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
print("You're at a cross road. Where do you want to go?")
choice_1 = input('Type "left" or "right"\n').lower()

if choice_1 == "left":
    choice_2 = input('You\'ve come to a leak, there is an island in the middle of the leak, '
          'Type "wait" to wait for a boat.Type "swim" to swim across.\n').lower()
    if choice_2 == "wait":
        choice_3 = input("You arrive at the island unharmed,There ia a house with 3 doors."
                         "One red, one yellow and one blue. which colour do you choose?\n").lower()
        if choice_3 == "red":
            print("The room in fire.Game over\n")
        elif choice_3 == "yellow":
            print("You found the treasure! You Win!\n")
        elif choice_3 == "blue":
            print("You entered room of beasts.Game Over\n")
        else:
            print("Your selected door dosn\'t exit .Game over\n")
    else:
        print("You have attacked by shark. Game over\n")
else:
    print("you fell into a hele. Game Over.\n")

