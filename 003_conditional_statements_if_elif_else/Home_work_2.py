import math

x=float(input('Введите значение х для функции y = f(x) :'))

res = round(math.cos(3*x),2) if -math.pi <= x <= math.pi else x

print(res)

