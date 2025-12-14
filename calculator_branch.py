import sys

def add(num):
    return sum(num)

def subtract(num):
    if len(num) == 0:
        return 0
    difference = num[0]
    for n in num[1:]:
        difference -= n
    return difference

def multiply(num):
    if len(num) == 0:
        return 0
    product = 1
    for _ in num:
        product *= _
    return product

def divide(num):
    if len(num) == 0:
        return 0
    if len(num) == 1:
        return num[0]
    quotient = num[0]
    for num in num[1:]:
        if num == 0:
            raise ValueError("Cannot divide by zero")
        quotient /= num
    return quotient

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

def read():
    expression = input("Enter your expression: ")
    print("Expression:", expression)
    if ' ' in expression:
        return expression.split()    
    for op in operations.keys():
        expression = expression.replace(op, f' {op} ')    
    return expression.split()
    
def parser(expression):
    global operations
    num = []
    for var in expression:
        if (var.isdigit() and int(var) in range(0,100000000)):
            num.append(int(var))
        elif (var in operations.keys()):
            operator = var
    try:
        return (num, operator)
    except UnboundLocalError:
        print("Ensure there is a space between arguments of your expression")
        sys.exit()

def calculate(numbers, operator):
    global operations
    if not numbers:
        raise ValueError("Numbers array cannot be empty")
    if operator not in operations:
        raise ValueError(f"Invalid operator: {operator}. Use '+', '-', '*', or '/'")
    return operations[operator](numbers)

def display(answer):
    print("The answer is : {}".format(answer))

def main():
    global expression
    choice = " "
    print("----------------")
    print("CALCULATOR")
    print("----------------\n")
    while(True):
        if choice == "exit": break
        expression = read()
        arguments = parser(expression)
        display(calculate(*arguments))
        choice = input("\nEnter 'exit' to quit the program, and any key to continue: ")

if __name__ == "__main__":
    main()