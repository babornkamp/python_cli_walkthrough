"""
Work wants an inventory app that:
    Stores data into a file
    Uses the command line to list/add/update/delete:
        "Items" they have:
            id
            name
            cond
            ?checkedIn?
"""

from models.item import Item # an import statement to make code from other files available

items = [] # this will be used to store items
next_id = 0

# TODO Make a menu print out showing options
def menu(): # prints menu options for the user
    print("""
1. List All Items
2. Add New Item
3. Update Existing Item
4. Delete Item (By item id)
5. Exit
""")

# List all items
def list_items(): # writes all items to the terminal
    for item in items:
        print(item)
  
# Add New Item
def new_item(): # gets user input for all needed fields for an item
    global next_id # allows us access to the next_id number
    global items

    name = input("Name: ")
    cond = input("Condition: ")
    item_id = next_id # uses the global counter to give a unique id for each item
    next_id += 1 # updates id with new value so next one is 1 more

    # this is the class -> Item from the other file we imported
    tmp = Item(item_id, name, cond) # builds an item/stores it in tmp
    items.append(tmp) # adds item to global items array
    

# Update Existing Item
def update_existing(itemId):
    pass

# Delete Item (By item id)
def delete_item(itemId):
    pass


# Make the menu questions that grab the data
def main(): # starts the program off, holds the loop until exit
    while True:
        menu() # prints the options to the terminal
        choice = input("> ") # takes user choice

        # the conditional options
        # hands off the work to the functions above
        if choice == "1": # list items
            list_items()
        elif choice == "2": # add items
            new_item()
        elif choice == "3": # update items
            pass
        elif choice == "4": # delete items
            pass
        elif choice == "5": # exit
            exit()
        else: # user gave us bad input we let them loop again
            input("Invalid input, give a number\n(Press Enter to try again)")

if __name__ == "__main__":
    main()





# Make the File Saving stuff