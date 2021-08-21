def standart():
    global g
    print(g)
    g ='Новая глобальная переменная'

g = 'Глобальная переменная'

def main():
    standart()

if __name__ == '__main__':
    main()

print(g)