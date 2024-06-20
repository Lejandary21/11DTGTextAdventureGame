import random

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}
        self.items = {}
    
    def add_exit(self, direction, room):
        self.exits[direction] = room
    
    def add_item(self, item_name, item_description):
        self.items[item_name] = item_description
    
    def get_items(self):
        return self.items.keys()

class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []
        self.magic_element = None

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print("You move to the", self.current_room.name)
            self.look_around()
            self.handle_cave_encounter()
        else: 
            print("You cannot go that way.")

    def look_around(self):
        print("You are in the", self.current_room.name)
        print(self.current_room.description)
        if self.current_room.exits:
            print("Where do you want to go?")
            for direction, room in self.current_room.exits.items():
                print(f"- {direction.capitalize()}: {room.name}")
        if self.current_room.items:
            print("You see the following items:")
            for item in self.current_room.get_items():
                print("-", item)
    
    def take_item(self, item_name):
        if item_name in self.current_room.items:
            self.inventory.append(item_name)
            print("You take the", item_name)
            del self.current_room.items[item_name]
        else:
            print("There is no", item_name, "here.")
    
    def inventory_status(self):
        if self.inventory:
            print("You are carrying:")
            for item in self.inventory:
                print("-", item)
        else:
            print("You are not carrying anything.")
    
    def choose_magic_element(self):
        elements = ["Fire Magic", "Bone Magic", "Crystal Magic"]
        self.magic_element = random.choice(elements)
        print(f"You have chosen {self.magic_element} as your magic element")
    
    def handle_cave_encounter(self):
        if self.current_room.name == "Goblin's Lair":
            print("A goblin appears!")
            self.fight_goblin()
    
    def fight_goblin(self):
        print("A goblin blocks your path!")
        while True:
            action = input("Do you want to fight or run? ").strip().lower()
            if action == "fight":
                print("You engage in combat with the goblin...")
                if random.choice([True, False]):
                    print("You defeated the goblin!")
                    break
                else:
                    print("The goblin overpowers you...")
                    print("You managed to escape!")
                    self.move("north")  # Move the player back to the previous room
                    break
            elif action == "run":
                print("You choose to run away...")
                print("You managed to escape!")
                self.move("north")  # Move the player back to the previous room
                break
            else:
                print("Invalid action. Please enter 'fight' or 'run'.")

# Create rooms
befallen_forest = Room("Befallen Forest", "A woodland forest in the north. An ancient grimoire lies in the heart of the forest, are you bold enough to go?")
mystic_cave_entrance = Room("Mystic Cave Entrance", "The entrance of the cave. It's dark and chilly.")
tunnel_1 = Room("Tunnel 1", "A narrow tunnel leading deeper into the cave.")
tunnel_2 = Room("Tunnel 2", "A winding tunnel with faint echoes.")
goblins_lair = Room("Goblin's Lair", "A large chamber with ominous shadows lurking in the corners. You sense danger.")

# Add exits to rooms
befallen_forest.add_exit("south", mystic_cave_entrance)
mystic_cave_entrance.add_exit("north", befallen_forest)
mystic_cave_entrance.add_exit("east", tunnel_1)
tunnel_1.add_exit("west", mystic_cave_entrance)
tunnel_1.add_exit("east", tunnel_2)
tunnel_2.add_exit("west", tunnel_1)
tunnel_2.add_exit("south", goblins_lair)
goblins_lair.add_exit("north", tunnel_2)

# Add items to rooms
befallen_forest.add_item("ancient grimoire", "An old book with mysterious symbols.")

# Function to show the commands
def show_commands():
    print("\nCommands:")
    print("move <direction>")
    print("look")
    print("take <item>")
    print("inventory")
    print("quit")

# Game loop
def game_loop(player):
    print(f"\nWelcome, {player.name}! Your adventure begins now.")
    player.look_around()
    show_commands()

    while True:
        command = input("\nEnter a command: ").split()
        if len(command) == 0:
            continue
        
        action = command[0].lower()
        
        if action == "move" and len(command) > 1:
            player.move(command[1])
        elif action == "look":
            player.look_around()
        elif action == "take" and len(command) > 1:
            item_name = " ".join(command[1:])
            player.take_item(item_name)
        elif action == "inventory":
            player.inventory_status()
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Unknown command.")
            show_commands()

# Game introduction
def game_intro():
    print("You're a peasant living in a town on the outskirts of Struht.")
    print("Opportunities are yet to come for you, adventurer.")
    print("You constantly dream of being at the top, the strongest, the one to inspire people.")
    player_name = input("What's your name, adventurer? ")
    
    print("\nChoose your magic element:")
    elements = ["Fire Magic", "Bone Magic", "Crystal Magic"]
    for index, element in enumerate(elements, 1):
        print(f"{index}. {element}")
    element_choice = int(input("Enter the number of your chosen element: ")) - 1
    
    player = Player(player_name, befallen_forest)
    player.magic_element = elements[element_choice]
    print(f"\nYou have chosen {player.magic_element} as your magic element.")
    
    return player

# Start the game
player = game_intro()
game_loop(player)
