#building the calculator
from art_calculator import logo
print(logo)
def add(n1, n2):
    """Add function"""
    return n1 + n2
def subtract(n1, n2):
    """perfrom subtraction between two numbers"""
    return n1 - n2
def multiple(n1, n2):
    """perform multiplication between two numbers"""
    return n1 * n2
def divide(n1, n2):
    """perform divide between two numbers"""
    return n1 / n2
operators = {
    "+" : add,
    "-" : subtract,
    "*" : multiple,
    "/" : divide
}
#ask the user for the number and that number must be converted into the int
def calculator():
    num_1 = float(input("What's the first number you like to enter?: "))

#op=input("which operation you want to do?:)
    for sign in operators:
        print(sign)
    should_continue = True
#this while loop will keep the program
    while should_continue:
        operation_sign = input("Pick an operation: ")
        num_2 = float(input("What's the next number you like to enter?: "))
        calculation_function = operators[operation_sign]
        answer = calculation_function(num_1, num_2)

        print(f"Here you go: {num_1} {operation_sign} {num_2} = {answer}")
        # for sign in operators:
        #     print(sign)
        # operation_sign = input("Pick an operation from the above: ")
        # num_3 =int(input("What's the next number?: "))
        # calculation_function = operators[operation_sign]
        # second_answer = calculation_function(calculation_function(num_1,num_2), num_3)
        #
        # print(f"{first_answer} {operation_sign} {num_3} = {second_answer}")
        if input(f" Type 'y' to continue calculating with {answer}, or type 'n' if you start a new calculator") == "y":
            num_1 = answer
        else:
            should_continue = False
            calculator()

calculator()

#Recursion 