a = [int(i) for i in input('Введите любое колличество элиментов списка через пробел: ').split()]

def check_max(x):
        return max(x)

def check_min(x):
        return min(x)

def check_sum(x):
    return sum(x)

def check_arithmetic(x):
    return sum(x) / len(x)

def main():
    print('наибольший элемент списка: ', check_max(a))
    print('наименьший элемент списка: ', check_min(a))
    print('сумма списка: ', check_sum(a))
    print('среднее арифметическое: ', check_arithmetic(a))

if __name__ == '__main__':
    main()



