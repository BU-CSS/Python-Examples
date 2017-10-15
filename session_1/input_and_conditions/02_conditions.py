command = input('Please enter a command: ')

if command == 'print':
    print(command)
elif command == 'name':
    name = input('Please enter your name: ')
    print(name)
else:
    print('The command you entered was not valid!')
