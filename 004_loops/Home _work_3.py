height = int(input('Введите высоту прямоугольного треугольника: '))
for row in range(height + 1):
    for column in range(height):
        if height - row < column:
            print('*', end='')
        else:
            print('', end='')
    for column in range(height):
        if row > column:
            print('*', end='')
        else:
            print('', end='')
    print()

