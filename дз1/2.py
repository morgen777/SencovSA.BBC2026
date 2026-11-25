def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def umn(a, b):
    return a * b

def delit(a, b):
    return a // b


a = int(input())
b = int(input())
d = input()

if d == '+':
    print(plus(a, b))

elif d == '-':
    print(minus(a, b))

elif d == '*':
    print(umn(a, b))

elif d == '/':
    print(delit(a, b))
