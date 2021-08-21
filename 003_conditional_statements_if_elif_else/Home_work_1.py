import math

x=float(input('Введите значение х для функции y = f(x) :'))

if -math.pi <= x <= math.pi:
    print(f'Функции y = f(x) ровняется {round(math.cos(3*x),2)}')
elif x < -math.pi:
    print(f'Функции y = f(x) ровняется {x}')
else:
    print(f'Функции y = f(x) ровняется {x}')


