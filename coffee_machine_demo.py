MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

water_for_espresso = MENU["espresso"]["ingredients"]["water"]
coffee_for_espresso = MENU["espresso"]["ingredients"]["coffee"]
cost_of_espresso = MENU["espresso"]["cost"]
water_for_latte = MENU["latte"]["ingredients"]["water"]
milk_for_latte = MENU["latte"]["ingredients"]["milk"]
coffee_for_latte = MENU["latte"]["ingredients"]["coffee"]
cost_of_latte = MENU["latte"]["cost"]
water_for_cappuccino = MENU["cappuccino"]["ingredients"]["water"]
milk_for_cappuccino = MENU["cappuccino"]["ingredients"]["milk"]
coffee_for_cappuccino = MENU["cappuccino"]["ingredients"]["coffee"]
cost_of_cappuccino = MENU["cappuccino"]["cost"]

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


def resources_func(water, milk, coffee, money):
    # resources at start
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${round(money, 2)}")


def enough_resources(user_choice, water, milk, coffee):
    if user_choice == "cappuccino":
        if water >= 250:
            if milk >= 100:
                if coffee >= 24:
                    return 1
                else:
                    print("Sorry, there is not enough coffee.")
                    return None
            else:
                print("Sorry, there is not enough milk.")
                return None
        else:
            print("Sorry, there is not enough water.")
            return None
    elif user_choice == "latte":
        if water >= 200:
            if milk >= 150:
                if coffee >= 24:
                    return 1
                else:
                    print("Sorry, there is not enough coffee.")
                    return None
            else:
                print("Sorry, there is not enough milk.")
                return None
        else:
            print("Sorry, there is not enough water.")
            return None
    elif user_choice == "espresso":
        if water >= 50:
            if coffee >= 24:
                return 1
            else:
                print("Sorry, there is not enough coffee.")
                return None
        else:
            print("Sorry, there is not enough water.")
            return None


def process_coins(quarters, dimes, nickles, pennies): 
    #insert coins to calculate
    print("Enter coins.")
    user_quarters = int(input("How many quarters?: "))
    user_dimes = int(input("How many dimes?: "))
    user_nickles = int(input("How many nickles?: "))
    user_pennies = int(input("How many pennies?: "))
    global value
    value = (user_quarters * quarters) + (user_dimes * dimes) + (user_nickles * nickles) + (user_pennies * pennies)
    return value


def transaction(value_1, user_choice, quarters, dimes, nickles, pennies): 
    #check if transaction can be completed or not
    if user_choice == "espresso":
        if value_1 > cost_of_espresso:
            money_left = value_1 - cost_of_espresso
            print(f"Here is ${round(money_left, 2)} dollars in change.")
            make_espresso(water_for_espresso, coffee_for_espresso)
            return
        else:
            return print("Sorry that's not enough money. Money refunded.")
    elif user_choice == "latte":
        if value_1 > cost_of_latte:
            money_left = value_1 - cost_of_latte
            print(f"Here is ${round(money_left, 2)} dollars in change.")
            make_latte(water_for_latte, milk_for_latte, coffee_for_latte)
            return
        else:
            return print("Sorry that's not enough money. Money refunded.")
    else:
        if value_1 > cost_of_cappuccino:
            money_left = value_1 - cost_of_cappuccino
            print(f"Here is ${round(money_left, 2)} dollars in change.")
            make_cappuccino(water_for_cappuccino, milk_for_cappuccino, coffee_for_cappuccino)
            return
        else:
            return print("Sorry that's not enough money. Money refunded.")


def make_espresso(water_for_espresso, coffee_for_espresso):
    #function to make espresso
    global  water
    water -= water_for_espresso
    global coffee
    coffee -= coffee_for_espresso
    print(f"Here is your Espresso ☕. Enjoy!")


def make_latte(water_for_latte, milk_for_latte, coffee_for_latte):
    global water
    water -= water_for_latte
    global milk
    milk -= milk_for_latte
    global coffee
    coffee -= coffee_for_latte
    print(f"Here is your Latte ☕. Enjoy!")


def make_cappuccino(water_for_cappuccino, milk_for_cappuccino, coffee_for_cappuccino):
    global water
    water -= water_for_cappuccino
    global milk
    milk -= milk_for_cappuccino
    global coffee
    coffee -= coffee_for_cappuccino
    print(f"Here is your Cappuccino ☕. Enjoy!")


def update_money(cost_of_anything):
    money_left_2 = value_1 - cost_of_anything
    global money
    money += money_left_2


is_machine_on = True

while is_machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # x = 0
    if user_choice == "espresso": 
        #do the functions for espresso
        if enough_resources(user_choice, water, milk, coffee) == None:
            # x = 1
            continue
        else:
            value_1 = process_coins(quarters, dimes, nickles, pennies)
            transaction(value_1, user_choice, quarters, dimes, nickles, pennies)
            update_money(cost_of_espresso)
    elif user_choice == "latte": 
        #do the functions for latte
        if enough_resources(user_choice, water, milk, coffee) == None:
            # x = 1
            continue
        else:
            value_1 = process_coins(quarters, dimes, nickles, pennies)
            transaction(value_1, user_choice, quarters, dimes, nickles, pennies)
            update_money(cost_of_latte)
    elif user_choice == "cappuccino": 
        #do the functions for cappuccino
        if enough_resources(user_choice, water, milk, coffee) == None:
            # x = 1
            continue
        else:
            value_1 = process_coins(quarters, dimes, nickles, pennies)
            transaction(value_1, user_choice, quarters, dimes, nickles, pennies)
            update_money(cost_of_cappuccino)
    elif user_choice == "off":
        #shutdown the coffee machine
        is_machine_on = False
    elif user_choice == "report":
        #show the list of resources remaining and show the balance money
        resources_func(water, milk, coffee, money)
    else:
        print("Wrong input!")
