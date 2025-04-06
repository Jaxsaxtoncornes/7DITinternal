import os     #imported os for the os.system("clear")
import time   #imported time to allow user's to read dialogue before it disappears


pizza_base = [["Thin Base", 5],["Plain Base", 6], ["Gluten Free Base", 6.5], ["Italian Herb Base", 7]]
pizza_crust = [["Plain Crust", 0],["Tomato Crust", 1],["Cheesey Crust", 1],["Vegan Cheesey Crust", 1.5]]
pizza_cheese = [["Mozzarella", 0.5],["Chedder", 0.5],["4 Cheese's", 1],["Vegan Cheese", 1]]
pizza_toppings = [["Basil", 0.5],["Garlic", 0.75],["Onions", 1],["Tomatoes", 1.25],["Mushrooms", 1.5],["Green Peppers", 1.75],["Ham", 2],["Pepperoni", 2.5]]
pizza_sides = [["Coca Cola", 2],["Sprite", 2],["Fanta", 2],["Fries", 3],["Onion Rings", 3.5],["Garlic Bread", 4]]
user_order = []
user_sides = []


def menu():
    os.system("clear")
    print("Welcome to Queenstowns Pizzaria!")
    print("1. Make a pizza")
    print("2. Purchase sides")
    print("3. Cart")
    print("4. Leave\n")
    user_input = input("Enter the number for what you would like to do. \n > ")
    if user_input.isdigit():
        user_input = int(user_input)
        if user_input == 1:
            make_pizza()
        elif user_input == 2:
            side_confirm()
        elif user_input == 3:
            cart()
        elif user_input == 4:
            leave()
        else:
            print("Enter a valid number input")
            time.sleep(1)
            menu()
    else:
        print("enter a valid input")
        time.sleep(1)
        menu()


def make_pizza():
    def pizza_base_choice():
        os.system("clear")
        print("What type of pizza base would you like")
        counter_1 = 0
        for base in pizza_base:
            counter_1 = counter_1 + 1
            print(str(counter_1) + ". " + str(base[0]) + " $" + str(base[1]))
        pizza_base_input = input("Enter the number next to the pizza base for your choice: ")
        if pizza_base_input.isdigit():
            pizza_base_input = int(pizza_base_input)
            if pizza_base_input == 1:
                user_order.append(pizza_base[0])
            elif pizza_base_input == 2:
                user_order.append(pizza_base[1])
            elif pizza_base_input == 3:
                user_order.append(pizza_base[2])
            elif pizza_base_input == 4:
                user_order.append(pizza_base[3])
            else:
                print("Please enter a valid number")
                time.sleep(1)
                pizza_base_choice()
        else:
            print("Please enter a valid input")
            time.sleep(1)
            pizza_base_choice()
    
    def pizza_crust_choice():
        os.system("clear")
        print("What type of pizza crust would you like")
        counter_2 = 0
        for crust in pizza_crust:
            counter_2 = counter_2 + 1
            print(str(counter_2) + ". " + str(crust[0]) + " $" + str(crust[1]))
        pizza_crust_input = input("Enter the number next to the pizza crust for your choice: ")
        if pizza_crust_input.isdigit():
            pizza_crust_input = int(pizza_crust_input)
            if pizza_crust_input == 1:
                user_order.append(pizza_crust[0])
            elif pizza_crust_input == 2:
                user_order.append(pizza_crust[1])
            elif pizza_crust_input == 3:
                user_order.append(pizza_crust[2])
            elif pizza_crust_input == 4:
                user_order.append(pizza_crust[3])
            else:
                print("Please enter a valid number")
                time.sleep(1)
                pizza_crust_choice()
        else:
            print("Please enter a valid input")
            time.sleep(1)
            pizza_crust_choice()
    
    def pizza_cheese_choice():
        os.system("clear")
        print("What type of pizza cheese would you like")
        counter_3 = 0
        for cheese in pizza_cheese:
            counter_3 = counter_3 + 1
            print(str(counter_3) + ". " + str(cheese[0]) + " $" + str(cheese[1]))
        pizza_cheese_input = input("Enter the number next to the pizza cheese for your choice: ")
        if pizza_cheese_input.isdigit():
            pizza_cheese_input = int(pizza_cheese_input)
            if pizza_cheese_input == 1:
                user_order.append(pizza_cheese[0])
            elif pizza_cheese_input == 2:
                user_order.append(pizza_cheese[1])
            elif pizza_cheese_input == 3:
                user_order.append(pizza_cheese[2])
            elif pizza_cheese_input == 4:
                user_order.append(pizza_cheese[3])
            else:
                print("Please enter a valid number")
                time.sleep(1)
                pizza_cheese_choice()
        else:
            print("Please enter a valid input")
            time.sleep(1)
            pizza_base_choice()
    
    def pizza_toppings_choice():
        os.system("clear")
        user_toppings_confirm = input("Say yes or no if you would like toppings on your pizza.\n").lower()
        if user_toppings_confirm == "yes":
            while True:
                os.system("clear")
                counter_4 = 0
                for toppings in pizza_toppings:
                    counter_4 = counter_4 + 1
                    print(str(counter_4) + ". " + str(toppings[0]) + " $" + str(toppings[1]))
                print("Enter 'exit' to go back to the menu and finish selecting toppings")
                pizza_toppings_input = input("Enter the number next to the toppings for your choice: ").lower()
                if pizza_toppings_input == "1":
                    user_order.append(pizza_toppings[0])
                elif pizza_toppings_input == "2":
                    user_order.append(pizza_toppings[1])
                elif pizza_toppings_input == "3":
                    user_order.append(pizza_toppings[2])
                elif pizza_toppings_input == "4":
                    user_order.append(pizza_toppings[3])
                elif pizza_toppings_input == "5":
                    user_order.append(pizza_toppings[4])
                elif pizza_toppings_input == "6":
                    user_order.append(pizza_toppings[5])
                elif pizza_toppings_input == "7":
                    user_order.append(pizza_toppings[6])
                elif pizza_toppings_input == "8":
                    user_order.append(pizza_toppings[7])
                elif pizza_toppings_input == "exit":
                    menu()
                    break
                else:
                    print("Please enter a valid input")
                    time.sleep(1)
        elif user_toppings_confirm == "no":
            print("Alright, back to the menu!")
            time.sleep(1)
            menu()
        else:
            print("Please enter a valid input")
            time.sleep(1)
            pizza_toppings_choice()
    
    pizza_base_choice()
    pizza_crust_choice()
    pizza_cheese_choice()
    pizza_toppings_choice()


def side_choice():
    os.system("clear")
    counter_5 = 0
    for sides in pizza_sides:
        counter_5 = counter_5 + 1
        print(str(counter_5) + ". " + str(sides[0]) + " $" + str(sides[1]))
    user_sides_choice = input("What side would you like to purchase: ")
    if user_sides_choice.isdigit():
        user_sides_choice = int(user_sides_choice)
        if user_sides_choice == 1:
            user_sides.append(pizza_sides[0])
        elif user_sides_choice == 2:
            user_sides.append(pizza_sides[1])
        elif user_sides_choice == 3:
            user_sides.append(pizza_sides[2])
        elif user_sides_choice == 4:
            user_sides.append(pizza_sides[3])
        elif user_sides_choice == 5:
            user_sides.append(pizza_sides[4])
        elif user_sides_choice == 6:
            user_sides.append(pizza_sides[5])
        else:
            print("Enter a number between 1-6")
            time.sleep(1)
            side_choice()
        menu()
    else:
        print("Enter a valid input")
        time.sleep(1)
        side_choice()


def side_confirm():
    os.system("clear")
    counter_5 = 0
    for sides in pizza_sides:
        counter_5 = counter_5 + 1
        print(str(counter_5) + ". " + str(sides[0]) + " $" + str(sides[1]))
    user_side_confirm = input("Looking at the availble sides, enter yes or no if you want to buy a side: ").lower()
    if user_side_confirm == "yes":
        side_choice()
    elif user_side_confirm == "no":
        print("Alright, back to the menu!")
        time.sleep(1)
        menu()
    else:
        print("Enter a valid input")
        time.sleep(1)
        side_confirm()


def cart():
    os.system("clear")
    print(user_order)
    print(user_sides)
    user_input = input("Enter yes or no if you would like to check out: ").lower()
    if user_input == "yes":
        input("What size pizza would you like?")
    elif user_input == "no":
        print("Alright, back to the menu!")
        time.sleep(1)
        menu()
    else:
        print("Please enter a valid input")
        time.sleep(1)
        cart()


def leave():
    os.system("clear")
    leave_call = input("Enter yes or no if you want to end your order: ").lower()
    if leave_call == "yes":
        print("have a good day!")
    elif leave_call == "no":
        print("Alright, back to the menu!")
    else:
        print("Please enter a valid input")
        time.sleep(1)
        leave()

 
menu()