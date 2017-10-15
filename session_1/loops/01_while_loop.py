command = ''

while command != 'exit':
    command = input('Please enter a command: ')

    if command == 'print':
        print(command)
    elif command == 'name':
        name = input('Please enter your name: ')
        print(name)
    elif command == 'exit':
        print('Exiting')
    else:
        print('The command you entered is invalid!')
