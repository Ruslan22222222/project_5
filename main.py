import os

from art import logo

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

option = {
    "+": add,
    "-": substract, 
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's your first numbder?: "))
    for symbol in option:
        print(symbol) # Вывод доступных операторов

    should_countinue = True

    while should_countinue:
        symbol = input("Pick an option: ")
        num2 = float(input("What's a second number"))
        calculation = option[symbol] # Выбор соответствующей функции из словаря по введенному оператору
        answer = calculation(num1, num2) # Выполнение выбранной операции

        print(f"{num1} {symbol} {num2} = {answer}")

        if input(f"Type 'y' to countinue calculating with {answer}, or type 'no' to start a new calculation: ") == "yes":
            num1 = answer

        else:
            os.system('clear')
            should_countinue = False
            calculator()


calculator()
