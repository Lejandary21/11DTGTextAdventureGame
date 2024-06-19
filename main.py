# INTRODUCTION 
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
        self.exits[item_name] = item_description
    def get_items(self):
        return self.items.keys()
    
class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_name = starting_room
        self.inventory = []
        self.magic_element = None
        
def move(self, direction):
    if direction in self.current_room.exits:
        self.current_room = self.current_room.exits[direction]
        print("You move to the", self.current_room.name)
        self.look_around()
    else: 
        print("You cannot go that way.")

def look_around(self):
    print("You are in the", self.current_room.name)
    print(self.current_room.description)
    if self.current_room.items:
        print("You see the following items:")
        for item in self.current_room.get_items():
            print("-"), item

def take_item(self, item_name):
    if item_name in self.current_room.items:
        self.inventory.append(item_name)
        print("You take the", item_name)
        del self.current_room.items[item_name]
def inventory_status(self):
    if self.inventory:
        print("You are carrying:")
        for item in self.inventory:
            print("-"), item
    else:
        print("You are not carrying anything.")
def choose_magic_element(self):
    elements = ["Fire Magic", "Bone Magic", "Crystal Magic"]
    self.magic_element = random.choice(elements)
    print(f"You have chosen {self.magic_element} as your magic element")
#The rooms
befallen_forest = Room("Befallen Forest", "A woodland forest in the north. An ancient grimoire lies in the heart of the forest, are you bold enough to go?")
mystic_cave = Room("Mystic Cave", "A dark, damp cave. You can hear the faint sound of dripping water echoing through the cavern.")
enchanted_lake = Room("Enchanted Lake", "A serene lake with water that glows softly under the moonlight")