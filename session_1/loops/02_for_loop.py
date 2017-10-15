try:
    limit = int(input('Please enter a number to count to: '))
except ValueError:
    print('You did not enter a valid number!')
    exit()

for number in range(0, limit+1):
    print(number)
