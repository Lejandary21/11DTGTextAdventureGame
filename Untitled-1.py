import random

#------------FUNCTIONS---------------

#------------Game introduction--------
def game_intro():
        print("Welcome to Abaddon! A simple Text Adventure game made by Pranaya, Lejan and Apanui. Enjoy your gameplay!")
        print("You're a peasant living in a town on the outskirts of Struht.")
        print("Opportunities are yet to come for you, adventurer.")
        print("You constantly dream of being at the top, the strongest, the one to inspire people.")
        print("You open your eyes. You sit up on your bed and your eyes began to wonder around your surroundings. Your house is dusty, shabby house. Cobwebs linger in the corner of each room, it's been a long time since you last cleaned it. You get up from your bed and decided to start anew and begin your journey.")
        name = input("What's your name, adventurer? ")   
        print("Great! Best of luck" ,name)

game_intro()

#----------character choice-----------
print("Now you have option of two chracters.")
choice = input("Choose your character (1 for Warrior, 2 for Mage): ")
    
if choice == '1':
        character = "Warrior"
        print("Brilliant choice, brave Warrior!")
        equipment = ["Basic Sword", "Leather Armor"]
elif choice == '2':
        character = "Mage"
        print("Brilliant choice, wise Mage!")
        equipment = ["Basic Staff", "Robe"]
#--------------Instruction for the character----------
print("Instructions for your character:")
print("Use these commands to move:")
print("- 'up': Move up")
print("- 'down': Move down")
print("- left': Move left")
print("- 'right': Move right")
if character == "Warrior":
        print("As a Warrior, you are strong and brave. You excel in close combat and can take a lot of damage.")
elif character == "Mage":
        print("As a Mage, you are wise and powerful. You excel in casting spells and using magic.")


#----- Staring Equiment-------
print("Your equipment")
if character == "Warrior":
       print("- Wooden Sword")
       print("- Leather Armor")
elif character == "Mage":
       print("- Wooden staff")
       print("- Linen Robe")

#----- The Game Starts -----
print("You come across a 2 way path. The right side leads to the forest and the left leads to the cave. which way do you want to go? (Forest/Cave)")
areaChoice = input("")
if (areaChoice == "Forest"):
       print("The forest it is...")
       print("As you walk deeper into the forest, you see a statue wearing a necklace.")
       print("Do you want to take the necklace from the statue? ")
       statueChoice = input("")

 if (statueChoice == "Yes"):
       print("You walk closer to the statue and slowly grabbed the necklace from the statue's neck")
       print("It's a living statue! It began moving and grabbed your neck, crushing it.")
       print("You have died.")
 elif (statueChoice == "No"):
       print("You decided to ignore it and move on.")
 else:
       print("Invalid choice. Please enter Yes or No.")

elif (areaChoice == "Cave"):
       print("The cave it is...")
       print("As you venture inside the cave, you encounter a hostile goblin.")
       print("Do you want to fight it? Yes or No?")
       

else:
   print("Invalid choice. Please enter Forest or Cave. (Run the game again to proceed)")



