import os     #imported os for the os.system("clear")
import time   #imported time to allow user's to read dialogue before it disapears

pizza_base = [["Thin Base", 5],["Plain Base", 6], ["Gluten Free Base", 6.5], ["Italian Herb Base", 7]]
pizza_crust = [["Plain Crust", 0],["Tomato Crust", 1],["Cheesey Crust", 1],["Vegan Cheesey Crust", 1.5]]
pizza_cheese = [["Mozzarella", 0.5],["Chedder", 0.5],["4 Cheese's", 1],["Vegan Cheese", 1]]
pizza_toppings = [["Basil", 0.5],["Garlic", 0.75],["Onions", 1],["Tomatoes", 1.25],["Mushrooms", 1.5],["Green Peppers", 1.75],["Ham", 2],["Pepperoni", 2.5]]
pizza_sides = [["Coca Cola", 2],["Sprite", 2],["Fanta", 2],["Fries", 3],["Onion Rings", 3.5],["Garlic Bread", 4]]
user_order = []

def menu():
    os.system("clear")
    print("Welcome to Queenstowns Pizzaria!")
    print("1. Make a pizza")
    print("2. Purchase sides")
    print("3. Cart")
    print("4. Leave\n")

def make_pizza():
    os.system("clear")
    print("What type of pizza base would you like")
    counter_1 = 0
    for base in pizza_base:
        counter_1 = counter_1 + 1
        print(str(counter_1) + ". " + str(base[0]) + " $" + str(base[1]))
    pizza_base_input = int(input("Enter the number next to the pizza base: "))
    if pizza_base_input == 1:
        user_order.append()

    
def purchase_sides():
    os.system("clear")
    print("What side would you like to purchase")
    counter_5 = 0
    for sides in pizza_sides:
        counter_5 = counter_5 + 1
        print(str(counter_5) + ". " + str(sides[0]) + " $" + str(sides[1]))
    sides_choice = int(input("What side would you like to purchase?"))
    if sides_choice == 1:
        sides.append()


def cart():
    os.system("clear")
    print(user_order)
    user_input = input("Would you like to check out?").lower()
    if user_input == "Yes":
        input("What size pizza would you like?")
    elif user_input == "No":
        print("Alright, back to the menu!")
        time.sleep(1)
        menu()
    else:
        print("Please enter a valid input")
        time.sleep(1)
        cart()

def leave():
    os.system("clear")
    leave_call = input("Are you sure you want to end your order?").lower()
    if leave_call == "Yes":
        print("have a good day!")
    elif leave_call == "No":
        print("Alright, back to the menu!")
    else:
        print("Please enter a valid input")
        time.sleep(1)
        leave()
    

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