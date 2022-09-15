"""
CSC120: Object Oriented Programming
A2: Tina Chang
Collaborated with: Tseegi Nyamdorj

"""

# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union
from computer import *
from oo_resale_shop import *

# Import the functions we wrote in procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
"""
Calls computer and oo_resale_shop classes and tests each method within.
"""
def main():

    # First, let's make a computer
    computer = Computer(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 64,
        "macOS Big Sur", 2013, 1500
    )
    
    # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    shop = ResaleShop()
    computer_id = shop.buy(computer)
    # Make sure it worked by checking inventory
    shop.print_inventory()

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    shop.refurbish(computer_id, new_OS)

    # Make sure it worked by checking inventory
    shop.print_inventory()
    
    # Now, let's sell it!
    shop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    shop.print_inventory()

# Calls the main() function when this file is run
if __name__ == "__main__": main()
