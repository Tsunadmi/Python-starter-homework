number_1 = int(input('Text the first number: '))
number_2 = int(input('Text the second number: '))

def answer(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    print(a + b)

def main():
    answer(number_1, number_2)

if __name__ == '__main__':
    main()
