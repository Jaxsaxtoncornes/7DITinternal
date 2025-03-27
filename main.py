import os
import time

user = []
pizza_base = [["Thin Base", 5],["Plain Base", 6], ["Gluten Free Base", 6.5], ["Italian Herb Base", 7]]
pizza_crust = [["Plain Crust", 0],["Cheesey Crust", 1],["Vegan Cheesey Crust", 1.5]]
pizza_cheese = [["Mozzarella", 0.5],["Chedder", 0.5],["4 Cheese's", 1],["Vegan Cheese", 1]]
pizza_toppings = [["Basil", 0.5],["Garlic", 0.75],["Onions", 1],["Tomatoes", 1.25],["Mushrooms", 1.5],["Ham", 2],["Pepperoni", 2.5]]
sides = [["Coca Cola", 2],["Sprite", 2],["Fries", 3],["Onion Rings", 3.5],["Garlic Bread", 4]]


def menu():
    os.system("clear")
    print("Welcome to Queenstowns Pizzaria!")
    print("1. Make a pizza")
    print("2. Purchase sides")
    print("3. Cart")
    print("4. Leave\n")

def make_pizza():
    print("Placeholder")
    input("")

def purchase_sides():
    print("Placeholder")
    input("")

def cart():
    print("Placeholder")
    input("")

def leave():
    print("Placeholder")
    input("")

while True:
    try:
        menu()
        user_input = int(input("Enter the number for what you would like to do. \n > "))
        if user_input == 1:
            make_pizza()
        elif user_input == 2:
            purchase_sides()
        elif user_input == 3:
            cart()
        elif user_input == 4:
            leave()
        else:
            print("enter a number between 1 to 4")
            time.sleep(1)
    except ValueError:
        print("Please enter a valid number.") 
        time.sleep(1)