import random

# ------------FUNCTIONS---------------

# ------------Game introduction--------
def game_intro():
    print("You're a peasant living in a town on the outskirts of Struht.")
    print("Opportunities are yet to come for you, adventurer.")
    print("You constantly dream of being at the top, the strongest, the one to inspire people.")
    print("You open your eyes. You sit up on your bed and your eyes begin to wander around your surroundings. Your house is dusty, shabby, with cobwebs lingering in the corners. It's been a long time since you last cleaned it. You get up from your bed and decide to start anew and begin your journey.")
    name = input("What's your name, adventurer? ")
    print("Great! Best of luck,", name)
    return name

# ----------character choice-----------
def choose_character():
    print("Now you have the option of two characters.")
    choice = input("Choose your character (1 for Warrior, 2 for Mage): ")

    if choice == '1':
        character = "Warrior"
        print("Brilliant choice, brave Warrior!")
        equipment = ["Basic Sword", "Leather Armor"]
    elif choice == '2':
        character = "Mage"
        print("Brilliant choice, wise Mage!")
        equipment = ["Basic Staff", "Robe"]
    else:
        character = "Peasant"
        print("Invalid choice, you remain a humble peasant.")
        equipment = []

    return character, equipment

# ------------Instructions function--------
def instructions(character, equipment):
    print("\nInstructions for your character:")
    print("Use these commands to move:")
    print("  - 'up': Move up")
    print("  - 'down': Move down")
    print("  - 'left': Move left")
    print("  - 'right': Move right")

    if character == "Warrior":
        print("As a Warrior, you are strong and brave. You excel in close combat and can take a lot of damage.")
    elif character == "Mage":
        print("As a Mage, you are wise and powerful. You excel in casting spells and using magic.")
    else:
        print("As a Peasant, you have no special abilities. You must rely on your wit and determination to survive.")

    print("\nStarting Equipment:")
    for item in equipment:
        print(f"  - {item}")

    print("\nAdditional Instructions:")
    print("  - Explore the town to find quests and challenges.")
    print("  - Collect items to help you on your journey.")
    print("  - Engage with other characters to gather information and aid.")

# MAIN CODE

# Start the game
name = game_intro()
character, equipment = choose_character()
print(f"{name}, the {character}, your journey begins now!")

# Provide instructions
instructions(character, equipment)
