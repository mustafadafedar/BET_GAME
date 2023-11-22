import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_value = {
    "A" : 5,
    "B" : 4,
    "C" : 3,
    "D" : 2
}
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings , winning_lines



def get_slot_machine_spin(rows, cols, symbols,):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbol = all_symbols[:]
        for _ in range(ROWS):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

            columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) -1:
                print(column[row], end = " | ")
            else:
                print(column[row], end="")
        print()

def deposite():
    while True:
        amount = input("How Much Would You Like To Deposite? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount Is Must Be Greater Than 0.")
        else:
            print("Please Enter A Number")

    return amount


def get_number_of_lines():
    while True:
        lines = input("Enter The Number Of Lines To Bet On (1-" + str(MAX_LINES) +"?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter A Valid Number Of Lines.")
        else:
            print("Please Enter A Number")

    return lines

def get_bet():
    while True:
        amount = input("How Much Would You Like To Bet On Each Line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount Is Must Be Between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please Enter A Number")

    return amount

def spin(Balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > Balance:
            print(f"You Do Not Have Enough Amount To Bet, Your Current Balance Is: ${Balance}")
        else:
            break
    print(f"You Are Betting ${bet} On {lines} Lines. Total Bet Is Equal To: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You Won ${winnings}.")
    print(f"You Won On Lines", *winning_lines)
    return winnings - total_bet

def main():
    Balance = deposite()
    while True:
        print(f"Current Balance Is ${Balance}")
        answer = input("Press Enter To Play (q to quit).")
        if answer == "q":
            break
        Balance += spin(Balance)

    print(f"You Left With {Balance}")

main()