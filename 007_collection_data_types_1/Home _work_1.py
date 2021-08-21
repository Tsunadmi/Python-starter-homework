a = [2, 4, 65, 32, 2, 6, 0, -1, 3]

def control(x):
    result =[]
    for element in x:
        if element < 5:
            result.append(element)
    return result

def main():
    print(control(a))

if __name__ == '__main__':
    main()
