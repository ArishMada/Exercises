Select_the_operation = input('Choose a number(1.Addition, 2.Subtraction, 3.Multiplication, 4.Division): ')
n1 = int(input('Enter a first number: '))
n2 = int(input('Enter a second number: '))

if Select_the_operation == '1':
    print(f'The result is {n1 + n2}')
elif Select_the_operation == '2':
    print(f'The result is {n1 - n2}')
elif Select_the_operation == '3':
    print(f'The result is {n1 * n2}')
elif Select_the_operation == '4':
    print(f'The result is {n1 / n2}')

else:
    print('error')


