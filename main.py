import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns =[]
    for _ in range(cols):
        column = []
        cur_symbol = all_symbols[:]
        for _ in range(rows):
            val = random.choice(all_symbols)
            cur_symbol.remove(val)
            column.append(val)
        
        columns.append(column)
    
    return columns

def deposit():
    while True:
        amount = input("What would you like to deposit? $: ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        
        else:
            print("please enter a number.")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on(1-"+str(MAX_LINES)+")?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("enter a valid numbert of lines.")
        
        else:
            print("please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $: ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        
        else:
            print("please enter a number.")

    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet*lines
        if total_bet > balance:
            print(f"You do not have enough balance to bet, your current balance: ${balance}")
        else:
            break

    print(f"you are betting ${bet} on ${lines}. Total bet is equal to: ${total_bet}")

main()