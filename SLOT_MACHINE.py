import random

MAX_LINE=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLUMN=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns,lines,bet,values):
    winnings=0
    winnings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings +=values[symbol]*bet
                winnings_lines.append(line + 1)

    return winnings,winnings_lines



def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]

    for symbol,symbol_count in symbols.items():
        for _  in range (symbol_count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i !=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")

        print()

def deposit():
    while True:
        amount =input("WHAT WOULD YOU LIKE TO DEPOSITE ? 💲")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("AMOUNT MUST BE GREATER THAN '0'.")
        else:
            print("PLEASE ENTER A NUMBER!!")
    return amount

def get_number_of_lines():
    while True:
        lines =input("ENTER THE NUMBER OF LINES TO BET ON (1 -" + str(MAX_LINE)+")? = ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINE:
                break
            else:
                print("LINES MUST BE GREATER THAN '1'.")
        else:
            print("PLEASE ENTER A NUMBER OF LINES!!")
    return lines

def get_bet():
    while True:
        amount =input("WHAT WOULD YOU LIKE TO BET ON EACH LINE ? 💲")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print("BET MUST BE BETWEEN",MIN_BET,"TO",MAX_BET)
        else:
            print("PLEASE ENTER A BET AMOUNT CORRECTLY!!")
    return amount

def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        TOTAL_BET=bet*lines

        if TOTAL_BET>balance:
            print("YOU DO NOT HAVE ENOUGH TO BET THAT AMOUNT ,YOUR CURRENT BALANCE IS :",balance)
        else:
            break
    print("YOU ARE BETTING",bet,"ON",lines,"LINES \n TOTAL BET =",TOTAL_BET)

    slots = get_slot_machine_spin(ROWS,COLUMN,symbol_count)
    print_slot_machine(slots)
    winnings,winnings_lines=check_winnings(slots,lines,bet,symbol_value)
    print("YOU WON",winnings,".")
    print("YOU WON ON LINES : ",winnings_lines,".")
    return winnings-TOTAL_BET



def main():
    balance = deposit()
    while True:
        print("CURRENT BALANCE IS",balance)
        answer=input("PRESS ENTER TO PLAY or Q TO QUIT : ").lower()
        if answer=="q":
            break
        balance += spin(balance)

    print("YOU LEFT WITH",balance)

main()
