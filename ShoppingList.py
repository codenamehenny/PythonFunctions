#2. The Shopping List Maker
#Objective: The aim of this assignment is to create a program that helps users make a shopping list.
#Task 1: Write a function that lets the user add items to a list.

def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"\n{item} has been added to your shopping list")

# Task 2: Include a function to remove items from the list.
def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"\n{item} has been removed from your shopping list")
    else:
        print(f"\n{item} is not in your shopping list")

#Task 3: Add a function that prints out the entire list in a formatted way.
def print_shopping_list(shopping_list):
    if shopping_list:
        index = 0
        print("\nHere's your shopping list: ")
        for item in shopping_list:
            index += 1
            print(f"{index}. {item}")
    else:
        print("\nList empty, start shopping!")

# function asking for user inputs
def go_shopping():
    shopping_list = [] # empty list
    item = 0
    while True:
        print("\nLet's go shopping! Please select one of the following options by number:")
        print("1. Add an item to your shopping list")
        print("2. Remove an item from your shopping list")
        print("3. Display your shopping list")
        print("4. Quit")
        option = input("Enter option number: ")
        if option == "1":   # add item option
            item = input("Enter the item to add: ")
            add_item(shopping_list, item)
        elif option == "2":  # remove item option
            item = input("Enter the item for removal: ")
            remove_item(shopping_list, item)
        elif option == "3":   # print shopping list
            print_shopping_list(shopping_list)
        elif option == "4": # end program
            print("\nLeaving shopping list")
            break

go_shopping()