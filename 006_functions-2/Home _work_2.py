
n= input('Ваедите фразу: ')

def control_if_pol(a):
    a = a.replace(' ','')
    a = a.lower()
    if len(a) <= 0:
        print('Это палиндромом!')
        return True
    if a[0] != a[-1]:
        print('Это непалиндромом!')
        return False
    return control_if_pol(a[1:-1])


def main():
    print(control_if_pol(n))

if __name__ == '__main__':
    main()
