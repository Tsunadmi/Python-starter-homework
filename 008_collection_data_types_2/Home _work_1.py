a = str(input('Введите первую строку '))
b = str(input('Введите вторую строку '))

def first(x):
    return (list(set(x)))

def main():
    print(first(a))
    print(first(b))
    print(set(first(a)) & set(first(b)))

if __name__ == '__main__':
    main()


