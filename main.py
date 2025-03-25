import os

user = []
pizza_base = [["Thin Base", 5],["Plain Base", 6], ["Gluten Free Base", 6.5], ["Italian Herb Base", 7]]
pizza_crust = [["Plain Crust", 0],["Cheesey Crust", 1],["Vegan Cheesey Crust", 1.5]]
pizza_cheese = [["Mozzarella", 0.5],["Chedder", 0.5],["4 Cheese's", 1],["Vegan Cheese", 1]]
pizza_toppings = [["Basil", 0.5],["Garlic", 0.75],["Onions", 1],["Tomatoes", 1.25],["Mushrooms", 1.5],["Ham", 2],["Pepperoni", 2.5]]
sides = [["Coca Cola", 2],["Sprite", 2],["Fries", 3],["Onion Rings", 3.5],["Garlic Bread", 4]]


def menu():
    os.system("clear")
    print("Welcome to Queenstowns Pizzaria,\n Please enter your name and select what toppings you want on your pizza! ")

menu()