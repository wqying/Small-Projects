MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

machine_money = 0  # initializes the money the machine has in the beginning


def check_resources(coffee):
    for liquids in resources:
        if resources[liquids] < MENU[coffee]["ingredients"][liquids]:
            print(f"Sorry there is not enough {liquids}.")
            return False
    return True


def process_coins(coffee):
    uppercase_coffee = coffee.capitalize()
    total_inserted = 0
    print(f"{uppercase_coffee} costs ${MENU[coffee]["cost"]}.\nInsert coins to pay.")
    coins = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }
    for i in coins:
        number_of_inserted_coins = int(input(f"How many {i}?: "))
        user_paid = coins[i] * number_of_inserted_coins
        total_inserted += user_paid
    total_inserted = round(total_inserted, 2)
    print(f"You have inserted ${total_inserted}.")
    return total_inserted  # don't change the global value of machine money directly!!


def transaction(money_in_machine, coffee):
    global machine_money
    if money_in_machine < MENU[coffee]["cost"]:
        print("Sorry that's not enough money. Money refunded.")  # nothing is done to global machine_money
        return False
    elif money_in_machine == MENU[coffee]["cost"]:
        print("Preparing your drink...")
        machine_money += money_in_machine
        return True
    elif money_in_machine > MENU[coffee]["cost"]:
        change = money_in_machine - MENU[coffee]["cost"]
        money_in_machine -= change
        machine_money += money_in_machine
        print(f"Here is ${round(change, 2)} in change.")
        print("Preparing your drink...")
        return True
    else:
        print("Please enter valid values.")
        return False


def resource_management(coffee):
    for liquids in resources:
        resources[liquids] = resources[liquids] - MENU[coffee]["ingredients"][liquids]


while True:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == "off":
        break
    elif coffee_type == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${abs(machine_money)}")
    elif coffee_type in MENU:  # check if the user entered a valid coffee type
        enough_resources = check_resources(coffee_type)
        if enough_resources is False:
            break
        money = process_coins(coffee_type)
        successful_trans = transaction(money, coffee_type)
        if successful_trans:
            resource_management(coffee_type)
        else:
            continue
        print("Here is your latte. Enjoy!")
    else:
        print("Please enter a valid drink.")
