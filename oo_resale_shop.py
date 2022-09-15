from typing import Dict, Union, Optional
from computer import *

"""
All resale methods can be found here:
init
buy, 
update price,
sell,
print inventory,
refurbish

"""
class ResaleShop:
    """
    create definition for inventory and itemID
    """
    def __init__(self):
        self.inventory : Dict[int, Dict[str, Union[str, int, bool]]] = {} 
        self.itemID = 0
    """
    "Buys" a computer by adding itemID and adding it to the inventory. 

    Returns itemID
    """
    def buy(self, computer: Dict[str, Union[str, int, bool]]):
        # global itemID
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer

        print("Buying", computer.get_attribute("description"))
        print("Adding to inventory...")
        print("Done.\n") 

        return self.itemID

    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """
    def update_price(self, item_ID: int, new_price: int):
        if item_ID in self.inventory:
            self.inventory[item_ID]["price"] = new_price
        else:
            print("Item", item_ID, "not found. Cannot update price.")

    """
    Takes in an item_id, removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, item_ID: int):
        print("Selling Item ID:", item_ID)
        if item_ID in self.inventory:
            del self.inventory[item_ID]
            print("Item", item_ID, "sold!")
        else: 
            print("Item", item_ID, "not found. Please select another item to sell.")

    """
    Prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        # If the inventory is not empty
        print("Checking inventory...")
        if self.inventory:
            # For each item
            for item_ID in self.inventory:
                # Print its details
                print(f'Item ID: {item_ID} : {self.inventory[item_ID].get_attribute("all attributes")}')
        else:
            print("No inventory to display.")
        print("Done.\n")

    """
    Finds the computer in the inventory, then assigns price for how much the computer can sell for, and updates OS. 
    Otherwise prints error message that item is not found.
    """
    def refurbish(self, item_ID: int, new_os: Optional[str] = None):
        if item_ID in self.inventory:
            computer = self.inventory[item_ID] # locate the computer
            if int(computer.get_attribute("year_made")) < 2000:
                computer.update_attribute("price", 0) # too old to sell, donation only
            elif int(computer.get_attribute("year_made")) < 2012:
                computer.update_attribute("price", 250) # heavily-discounted price on machines 10+ years old
            elif int(computer.get_attribute("year_made")) < 2018:
                computer.update_attribute("price", 550) # discounted price on machines 4-to-10 year old machines
            else:
                computer.update_attribute("price", 1000) # recent stuff

            if new_os is not None:
                computer.update_attribute("operating_system", new_os) # update details after installing new OS
        else:
            print("Item", item_ID, "not found. Please select another item to refurbish.")
        print("Done.\n")