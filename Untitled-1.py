import random

#------------FUNCTIONS---------------

#------------Game introduction--------
def game_intro():
 print("You're a peasant living in a town on the outskirts of Struht.")
print("Opportunities are yet to come for you, adventurer.")
print("You constantly dream of being at the top, the strongest, the one to inspire people.")
print("You open your eyes. You sit up on your bed and your eyes began to wonder around your surroundings. Your house is dusty, shabby house. Cobwebs linger in the corner of each room, it's been a long time since you last cleaned it. You get up from your bed and decided to start anew and begin your journey.")
name = input("What's your name, adventurer? ")   
print("Great! Best of luck" ,name)

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
       print("- Basic Sword")
       print("- Leather Armor")
elif character == "Mage":
       print(" - You will choose")
       print("- You will choose")

def bad_ending ():
       
        print("Dragon slays the King as his crown falls off his head down the stairs a long fall...")
        print("Explore the town to find quests and challenges.")
        print("Collect items to help you on your journey.")
                