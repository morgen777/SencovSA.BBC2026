def calc(a, b, d):
    if d == '+':
        return a + b
    elif d == '-':
        return a - b
    elif d == '*':
        return a * b
    elif d == '/':
        if b == 0:
            return "Деление на ноль!"
        return a / b
    elif d == '%':
        if b == 0:
            return "Деление на ноль!"
        return a % b
    elif d == '//':
        if b == 0:
            return "Деление на ноль!"
        return a // b

g = 0
while g != 1:
    a = int(input())
    b = int(input())
    d = input()
    print(calc(a, b, d))
