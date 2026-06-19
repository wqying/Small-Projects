import random


MAX_LINES = 5
ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,  # the most valuable symbol, the rarest
    "B": 4,
    "C": 6,
    "D": 8,
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items(): # specifically for dicts
        for _ in range(symbol_count):
            all_symbols.append(symbol)

     columns =


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit(): # only takes into account positive
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"How many lines would you like to bet on? (1-{MAX_LINES})")
        if lines.isdigit(): # only takes into account positive
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Amount must be greater than (1-{MAX_LINES}).")
        else:
            print("Please enter a number.")

    return lines

def betting_amount(deposit):
    while True:
        bet = input(f"How much would you like to bet? $")
        if bet.isdigit(): # only takes into account positive
            bet = int(bet)
            if 1 <= bet <= deposit:
                break
            else:
                print(f"Amount must be less than your ${deposit} deposit.")
        else:
            print("Please enter a number.")

    return bet

def main():
    balance = deposit()
    line = get_number_of_lines()
    while True:
        bet = betting_amount(balance)
        total_bet = line * bet
        if total_bet < balance:
            break
        else:
            print(f"Amount must be less than your ${balance} deposit.")

    print(f"You are betting ${bet} on {line} lines. Total bet is equal to: ${total_bet}")


main()