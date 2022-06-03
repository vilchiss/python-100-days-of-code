import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
}


def run_calculator():
    print(art.logo)
    number1 = float(input("What's the first number? "))
    for key in operations:
        print(key)

    can_continue = True
    while can_continue:
        operation_symbol = input("Pick an operation: ")
        operation = operations[operation_symbol]
        number2 = float(input("What's the next number? "))

        result = operation(number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {result}")

        user_input = input(f"Type 'y' to continue calculating with {result}, type 'n' to restart or 'e' to exit: ")
        if user_input == 'y':
            number1 = result
        elif user_input == 'n':
            can_continue = False
            run_calculator()
        else:
            can_continue = False


run_calculator()
