import os

from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def myltiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

option = {
"+": add,
"-": substract,
"*": myltiply,
"/": divide
}

def calculator():
    print(logo)
    
    while True:
        num1 = input("What's your first number:? ")
        if num1.isdigit():
            num = float(num1)
            break
        else:
            print("Invalid input. Please enter a valid number.")
    
    for symbol in option:
        print(symbol)

    should_countinue = True

    while should_countinue:
        symbol = input("Pick an option: ")
        num2 = float(input("WHat's your second number?: "))
        calculation = option[symbol]
        answer = calculation(num1, num2)
    print(f"{num1} {symbol} {num2} = {answer}")

    if input("Type 'yes' or 'no'. ") == "yes":
        num = answer
        
    else:
        os.system('clear')
        should_countinue = False
        calculator()

calculator()
