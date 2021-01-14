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
items = [1, 2, 3]
next_id = 0

# TODO Make a menu print out showing options
def menu():
    print("""
1. List All Items
2. Add New Item
3. Update Existing Item
4. Delete Item (By item id)
5. Exit
""")

# List all items
def list_items():
    for item in items:
        print(item)
    print("in list_item function")
  
# Add New Item
def new_item():
    global next_id
    name = input("Name: ")
    cond = input("Condition: ")
    item_id = next_id
    next_id += 1


# Update Existing Item
def update_existing(itemId):
    pass

# Delete Item (By item id)
def delete_item(itemId):
    pass


# Make the menu questions that grab the data
while True:
    menu()
    choice = input("> ")

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
    else:
        input("Invalid input, give a number\n(Press Enter to try again)")





# Make the File Saving stuff