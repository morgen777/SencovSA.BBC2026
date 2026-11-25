while True:
    choice = input('Введите номер уровня (1-5): ')
    if choice == '1':
        print('Уровень 1: upper, lower, capitalize')
        m = input('Введите метод: ')
        if m == 'ExIt': break
        w = input('Введите слово: ')
        if m == 'upper': print(w.upper())
        elif m == 'lower': print(w.lower())
        elif m == 'capitalize': print(w.capitalize())
    elif choice == '2':
        print('Уровень 2: find, replace, count, index')
        m = input('Введите метод: ')
        if m == 'ExIt': break
        w = input('Введите слово: ')
        if m == 'find':
            print(w.find(input('Введите подстроку: ')))
        elif m == 'replace':
            print(w.replace(input('Что заменить: '), input('На что заменить: ')))
        elif m == 'count':
            print(w.count(input('Введите подстроку: ')))
        elif m == 'index':
            print(w.index(input('Введите подстроку: ')))
    elif choice == '3':
        print('Уровень 3: split, join')
        m = input('Введите метод: ')
        if m == 'ExIt': break
        w = input('Введите слово: ')
        if m == 'split':
            print(w.split(input('Введите разделитель: ')))
        elif m == 'join':
            print(input('Введите разделитель: ').join(w))
    elif choice == '4':
        print('Уровень 4: isdigit, isalpha, strip, format, r, l, f')
        m = input('Введите метод: ')
        if m == 'ExIt': break
        w = input('Введите слово: ')
        if m == 'isdigit': print(w.isdigit())
        elif m == 'isalpha': print(w.isalpha())
        elif m == 'strip': print(w.strip())
        elif m == 'format': print("{:.2f}".format(float(w)))
        elif m == 'r': print(w[::-1])
        elif m == 'l': print(w.lower())
        elif m == 'f': print(w.upper())
    elif choice == '5':
        print('    pYtHon;is;AWESome    '.strip().replace(';', ' ').upper().capitalize())
