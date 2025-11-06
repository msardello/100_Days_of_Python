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

def print_report():
    """Returns the current quantity of all coffee machine resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * .25
    total += int(input("how many dimes?: ")) * .10
    total += int(input("how many nickels?: ")) * .05
    total += int(input("how many pennies?: ")) * .01
    return total


def is_resource_sufficient(drink_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for ingredient in drink_ingredients:
        required = drink_ingredients[ingredient]
        available = resources[ingredient]
        if required > available:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

def is_transaction_successful(cost, paid):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if paid >= cost:
        change_made = (round(paid - cost, 2))
        print(f"Here is ${change_made} in change.")
        global money
        money += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_ingredients):
    """Deduct the required ingredients from the resources."""
    for ingredient in drink_ingredients:
        required = drink_ingredients[ingredient]
        available = resources[ingredient]
        resources[ingredient] = available - required

money = 0
coffee_machine_on = True
while coffee_machine_on:
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if drink == "off":
        coffee_machine_on = False
    elif drink == "report":
        print_report()
    else:
        if drink in MENU:
            ingredients = MENU[drink]['ingredients']
            if is_resource_sufficient(ingredients):
                payment = process_coins()
                drink_cost = MENU[drink]['cost']
                if is_transaction_successful(drink_cost, payment):
                    make_coffee(ingredients)
                    print(f"Here is your {drink}. ☕️ Enjoy!")
        else:
            print("Invalid selection. Please choose espresso, latte, or cappuccino.")









