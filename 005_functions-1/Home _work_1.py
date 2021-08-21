n = str(input('Введите ваше имя: '))

def hello(x):
    if not x:
        print('Привет безымянный! Я буду называть тебя Дмитрй')
    else:
        print('Привет',x, '!')

def main():
    hello(n)

if __name__ == '__main__':
    main()