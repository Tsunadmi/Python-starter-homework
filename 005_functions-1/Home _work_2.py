a = float(input ('Введите первое число '))
b = float(input ('Введите второе число '))
print('''
Выберете действое которое вам небходимо:
Меню:
1. Сложение.
2. Вычитание.
3. Умножение.
4. Деление.
Если вы введете "END" программа будет завершена.
''')
def sum(a,b):
    return a + b
def sub(a,b):
    return a - b
def mult(a,b):
    return a * b
def div(a,b):
    if b != 0:
        return a / b
    else:
        print('На 0 делить нельзя')
def calculator():
    while True:
        s = str(input('Ваш выбор : '))
        if s == '1':
            d = sum(a,b)
            print('Ваш результат ', d)
        elif s == '2':
            d = sub(a,b)
            print('Ваш результат ', d)
        elif s == '3':
            d = mult(a,b)
            print('Ваш результат ', d)
        elif s == '4':
            d = div(a,b)
            print('Ваш результат ', d)
        elif s == 'END':
            print('Программа завершена')
            break
        else:
            print('Вы выбрали несуществующие действие')
def main():
    calculator()
if __name__ == '__main__':
    main()
