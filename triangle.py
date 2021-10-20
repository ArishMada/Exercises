rows = eval(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    for k in range (i-1):
        print(' ', end='')
    for j in range(i-1, rows):
        print('*', end='')
    print("")