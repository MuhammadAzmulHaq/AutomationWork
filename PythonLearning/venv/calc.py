on = True

def add():
    a = float(input("Enter a number"))
    b = float(input("Enter another number"))
    print(a + b)

def sub():
    a = float(input("Enter a number"))
    b = float(input("Enter another number"))
    print(a - b)

def mult():
    a = float(input("Enter a number"))
    b = float(input("Enter another number"))
    print(a * b)

def division():
    a = float(input("Enter a number"))
    b = float(input("Enter another number"))
    print(a / b)

while on:
    operation = input("Please type +, -, *, / or quit")
    if operation == '+':
        add()
    elif operation == '-':
        sub()
    elif operation == '*':
        mult()
    elif operation == '/':
        division()
    elif operation == "quit":
        on = False
    else:
     print("That operater isn't availible")
