a = int(input())
b = int(input())
operacia = input()

if operacia == '+':
    print(a + b)

elif operacia == '-':
    print(a - b)

elif operacia == '*':
    print(a * b)

elif operacia == '/':
    if b == 0:
        print("Деление на ноль!")
    else:
        print(a / b)

elif operacia == '%':
    if b == 0:
        print("Деление на ноль!")
    else:
        print(a % b)

elif operacia == '//':
    if b == 0:
        print("Деление на ноль!")
    else:
        print(a // b)
