# INTRODUCTION 


name = input("You're a peasant living in a town on the outskirts of Struht. Opportunities are yet to come for you, adventurer. You constantly dream of being at the top, the strongest, the one to inspire people.  What's your name, Adventurer?")
print(f" As the first rays of dawn pierce through the window shutters, casting a warm glow upon the humble room, {name} awakens from a night of restless dreams. With a yawn and a stretch, they rise from their simple bed, the wooden floorboards creaking softly beneath their feet. Outside, the small town stirs to life, the sounds of roosters crowing and distant chatter filling the air. Donning their worn cloak and securing their trusty belongings, {name} steps out into the crisp morning, a sense of adventure beckoning from beyond the familiar cobblestone streets.")
response = input(f"Or... you can just stay on your bed and keep sleeping, it's your choice, {name}. Do you want to wake up? Yes or No?")
if response.lower() == "yes":
    print("Good choice...")
    input("In the hushed dawn, the user's home stirs to life. They gather provisions, a water flack,their trusty blade and their grimoire. With belongings packed and cloak donned, they bid farewell to familiar comforts. Stepping into the crisp morning air, they leave behind the safety of home, venturing forth into the unknown, ready to embrace the challenges and wonders that await on their medieval journey. Choose your magic element: Fire Magic/Bone Magic/Crystal Magic")
elif response.lower() == "no":
    print("You decided to slack off and stay in bed for the rest of the day. Your life becomes uneventful as you grow old.")
else:
    print("Invalid response. Please choose 'yes' or 'no'")
