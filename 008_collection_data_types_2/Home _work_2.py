d = {'a':3, 'b':0, 'c':4, 'd':-3}

def func(**kwargs):
    for key in kwargs:
        return max(kwargs.values())


def main():
    print('Максимальное значение из списка: ',func(**d))


if __name__ == '__main__':
    main()


