a = [str(i) for i in input('Введите любое колличество слов через пробел: ').split()]

def dictionary(x):
    result = []
    for element in sorted(x):
        result.append(element)
    return result

def main():
    print(dictionary(a))

if __name__ == '__main__':
    main()

