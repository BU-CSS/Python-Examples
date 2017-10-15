def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

while True:
    try:
        first_number = int(input('Enter your first number: '))
        second_number = int(input('Enter your second number: '))
    except ValueError:
        print('You entered an invalid number!')
        exit()

    operation = input('Enter the operation to perform: ').strip()

    if operation == 'add' or operation == '+':
        print(add(first_number, second_number))
    elif operation == 'sub' or operation == '-':
        print(subtract(first_number, second_number))
    elif operation == 'mult' or operation == '*':
        print(multiply(first_number, second_number))
    elif operation == 'div' or operation == '/':
        print(divide(first_number, second_number))
    elif operation == 'exit':
        print('Exiting!')
        exit()
    else:
        print('You entered an unrecognised operation!')
