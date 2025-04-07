import os     #imported os for the os.system("clear")
import time   #imported time to allow user's to read dialogue before it disappears
import sys    #imported sys to terminate the program at the end

#These are all of the user's options for the pizza base, crust, cheese, toppings, and sides
pizza_base = [["Thin Base", 5],["Plain Base", 6], ["Gluten Free Base", 6.5], ["Italian Herb Base", 7]]
pizza_crust = [["Plain Crust", 0],["Tomato Crust", 1],["Cheesy Crust", 1],["Vegan Cheesy Crust", 1.5]]
pizza_cheese = [["Mozzarella", 0.5],["Cheddar", 0.5],["4 Cheeses", 1],["Vegan Cheese", 1]]
pizza_toppings = [["Basil", 0.5],["Garlic", 0.75],["Onions", 1],["Tomatoes", 1.25],["Mushrooms", 1.5],["Green Peppers", 1.75],["Ham", 2],["Pepperoni", 2.5]]
pizza_sides = [["Coca Cola", 2],["Sprite", 2],["Fanta", 2],["Fries", 3],["Onion Rings", 3.5],["Garlic Bread", 4]]
user_order = []  #Stores the user's pizza choices
user_sides = []  #Stores the user's sides choices


def menu(): #Displays the options that the user can do
    os.system("clear") #Clears previous code so it doesn't get cluttered
    print("Welcome to Queenstowns Pizzaria!")
    print("1. Make a pizza")
    print("2. Purchase sides")
    print("3. Cart")
    print("4. Leave\n")
    user_input = input("Enter the number for what you would like to do. \n > ")
    if user_input.isdigit(): #The .isdigit() recognises when the input is a number and runs the code
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


def make_pizza(): #Runs the 4 catigories in order, base to crust to cheese to toppings
    pizza_base_choice()
    pizza_crust_choice()
    pizza_cheese_choice()
    pizza_toppings_choice()

def pizza_base_choice():
    os.system("clear")
    print("What type of pizza base would you like")
    counter_1 = 0 #The counter is used for listing the options with numbers
    for base in pizza_base:
        counter_1 = counter_1 + 1
        print(str(counter_1) + ". " + str(base[0]) + " $" + str(base[1])) #Prints out the pizza bases list ordered from 1-4 with symbols
    pizza_base_input = input("Enter the number next to the pizza base for your choice: ")
    if pizza_base_input.isdigit():
        pizza_base_input = int(pizza_base_input)
        if pizza_base_input == 1:
            user_order.append(pizza_base[0]) #This adds the first option to the user's order list, thin base in this instance
        elif pizza_base_input == 2:
            user_order.append(pizza_base[1])
        elif pizza_base_input == 3:
            user_order.append(pizza_base[2])
        elif pizza_base_input == 4:
            user_order.append(pizza_base[3])
        else:
            print("Please enter a valid number")#If the users input is a number but isn't one of the numbers listed they will go the here
            time.sleep(1)
            pizza_base_choice()
    else:
        print("Please enter a valid input") #If the users input isn't a number they will go to here
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
        pizza_cheese_choice()


def pizza_toppings_choice():
    os.system("clear")
    counter_4 = 0
    for toppings in pizza_toppings:
        counter_4 = counter_4 + 1
        print(str(counter_4) + ". " + str(toppings[0]) + " $" + str(toppings[1]))
    user_toppings_confirm = input("\nType yes or no if you would like toppings on your pizza:").lower() #Asks if they actually want toppings or not 
    if user_toppings_confirm == "yes":
        while True: #while True loop is used because it can allow the user to select mulitple toppings without going back and fourth
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
            elif pizza_toppings_input == "exit": #When the user types "exit" it takes them back to the menu
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


def pizza_side_choice():
    while True: #Uses another while True loop so the user can select as many sides as they want
        os.system("clear")
        counter_5 = 0
        for sides in pizza_sides:
            counter_5 = counter_5 + 1
            print(str(counter_5) + ". " + str(sides[0]) + " $" + str(sides[1]))
        user_sides_choice = input("Enter 'exit' to go back to the menu\nEnter the number next to the side would you like to purchase: ").lower()
        if user_sides_choice == "1":
            user_sides.append(pizza_sides[0])
        elif user_sides_choice == "2":
            user_sides.append(pizza_sides[1])
        elif user_sides_choice == "3":
            user_sides.append(pizza_sides[2])
        elif user_sides_choice == "4":
            user_sides.append(pizza_sides[3])
        elif user_sides_choice == "5":
            user_sides.append(pizza_sides[4])
        elif user_sides_choice == "6":
            user_sides.append(pizza_sides[5])
        elif user_sides_choice == "exit":
            menu()
            break
        else:
            print("Please enter a valid input")
            time.sleep(1)
            pizza_side_choice()


def side_confirm(): #This is for if the user wants sides or not, if they do want sides the can order them, if not they go back to the menu
    os.system("clear")
    counter_5 = 0
    for sides in pizza_sides:
        counter_5 = counter_5 + 1
        print(str(counter_5) + ". " + str(sides[0]) + " $" + str(sides[1]))
    user_side_confirm = input("Looking at the available sides, enter yes or no if you want to buy a side: ").lower()
    if user_side_confirm == "yes":
        pizza_side_choice()
    elif user_side_confirm == "no":
        print("Alright, back to the menu!")
        time.sleep(1)
        menu()
    else:
        print("Enter a valid input")
        time.sleep(1)
        side_confirm()


def edit_cart():
    if not user_order: #This see's if the user has anything in the cart, used for making sure they don't try edit their cart with nothing in it
        print("Please order a pizza before editing cart")
        time.sleep(1.5)        
        cart() #If nothing is in the cart to be edited they go back to the cart menu
    print("What part of your pizza would you like to edit?")
    print("1. Pizza base")
    print("2. Pizza crust")
    print("3. Pizza cheese")
    print("4. Pizza toppings")
    print("5. Pizza sides")
    print("6. Back to cart")
    edit_cart_choice = input("Enter the number next to what you would like to do: ")
    if edit_cart_choice.isdigit():
        edit_cart_choice = int(edit_cart_choice)
        if edit_cart_choice == 1:
            user_order.pop(0) #This will clear the pizza base choice in the users order and allows them to choose a different one
            pizza_base_choice()
            os.system("clear")
            edit_cart()
        elif edit_cart_choice == 2:
            user_order.pop(1) #This will clear the pizza crust choice in the users order and allows them to choose a different one
            pizza_crust_choice()
            os.system("clear")
            edit_cart()
        elif edit_cart_choice == 3:
            user_order.pop(2) #This will clear the pizza cheese choice in the users order and allows them to choose a different one
            pizza_cheese_choice()
            os.system("clear")
            edit_cart()
        elif edit_cart_choice == 4:
            user_order[3:] = [] #This will clear the pizza toppings in the users order and allows them to choose a different one
            pizza_toppings_choice()
            os.system("clear")
            edit_cart()
        elif edit_cart_choice == 5:
            user_sides[0:] = [] #This will clear the sides in the users orders and allows them to choose a different one
            pizza_side_choice()
            os.system("clear")
            edit_cart()
        elif edit_cart_choice == 6:
            cart()
        else:
            print("Please enter a valid number")
            time.sleep(1)
            edit_cart()
    else:
        print("Please enter a valid input")
        time.sleep(1)
        edit_cart()


def pizza_checkout(): #This is the final part of the code, the checkout 
    os.system("clear")
    pizza_total_cost = 0 #This is where all of the costs of the pizza get stored
    for item in user_order:
        pizza_total_cost += item[1] #Gets the second value from the lists (price) and adds it together for the total pizza cost
    sides_total_cost = 0 #This is where all of the costs of the sides get stored
    for sides in user_sides:
        sides_total_cost += sides[1] #Gets the second value from the lists (price) and adds it together for the total sides cost
    os.system("clear")
    print("Alright, what size pizza would you like to have")
    print("1. Small, 1x the final price of your pizza")
    print("2. Medium, 1.25x the final price of your pizza")
    print("3. Large, 1.5x the final price of your pizza")
    pizza_size = input("Enter the number next to what you want to do: ") #This will add a muliplier to the pizza cost, simulating a small, medium, or large piza's extra cost
    if pizza_size.isdigit():
        pizza_size = int(pizza_size)
        if pizza_size == 1:
            final_pizza_cost = pizza_total_cost * 1 #Changes the original total pizza cost into a new cost depending on the users choice
        elif pizza_size == 2:
            final_pizza_cost = pizza_total_cost * 1.25 #Changes the original total pizza cost into a new cost depending on the users choice
        elif pizza_size == 3:
            final_pizza_cost = pizza_total_cost * 1.5 #Changes the original total pizza cost into a new cost depending on the users choice
        else:
            print("Please enter a valid number")
            time.sleep(1)
            pizza_checkout()
    else:
        print("Please enter a valid input")
        time.sleep(1)
        pizza_checkout()
    final_cost = final_pizza_cost + sides_total_cost #Adds togther the final pizza cost and the sides cost together
    os.system("clear")
    print("Your final pizza cost is $" + str(final_pizza_cost)) #Dislays the final cost of the pizza alone
    print("Your final pizza cost along with sides is $" + str(final_cost)) #Displays the final cost along with the sides
    input("Enter to complete your order")
    sys.exit()


def cart(): #Like the menu but for the cart
    os.system("clear")
    print("1. Checkout \n2. View cart \n3. Edit cart \n4. Go back to the menu \n")
    user_cart_choice = input("Enter the number next to what you would like to do: ")
    if user_cart_choice.isdigit():
        user_cart_choice = int(user_cart_choice)
        if user_cart_choice == 1: #Takes the user to the checkout
            pizza_checkout() 
        elif user_cart_choice == 2: #Diplays the users cart under catigories of their pizza and sides
            os.system("clear")
            print("Pizza: ")
            for order in user_order:
                print(str(order[0]) + " $" + str(order[1]))
            print("Sides: ")
            for sides in user_sides:
                print(str(sides[0]) + " $" + str(sides[1]))
            input("Enter to go back to the cart")
            cart()
        elif user_cart_choice == 3: #Takes the user to the edit cart section
            edit_cart()
        elif user_cart_choice == 4: #Takes the user back to the menu
            print("Alright, back to the menu")
            time.sleep(1)
            menu()
        else:
            print("Please enter a valid number")
            time.sleep(1)
            cart()
    else:
        print("Please enter a valid input")
        time.sleep(1)
        cart()


def leave(): #This is for if the user wants to end the code and not order a pizza, simulating hanging up closing the website
    os.system("clear")
    leave_call = input("Enter yes or no if you want to end your order: ").lower()
    if leave_call == "yes":
        print("Have a good day!")
        sys.exit()
    elif leave_call == "no":
        print("Alright, back to the menu!")
        time.sleep(1)
        menu()
    else:
        print("Please enter a valid input")
        time.sleep(1)
        leave()

 
menu() #Start of the code, runs the menu