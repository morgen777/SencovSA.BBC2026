def profit(v, p, c, r, z, o):
    doh = v * 30 * p
    rash = v * 30 * c + r + z + o
    return doh, rash, doh - rash


print('КАЛЬКУЛЯТОР КОФЕЙНИ')

v = int(input('Продаж кофе в день: '))
p = int(input('Цена одного кофе: '))
c = int(input('Себестоимость одного кофе: '))
r = int(input('Аренда за месяц: '))
z = int(input('Зарплата сотрудников: '))
o = int(input('Другие расходы: '))

d, r, pr = profit(v, p, c, r, z, o)

print('\n--- РЕЗУЛЬТАТЫ ---')
print('Выручка:', d, 'руб.')
print('Расходы:', r, 'руб.')
print('Прибыль:', pr, 'руб.')

if pr > 0:
    print('Кофейня приносит прибыль!')
elif pr < 0:
    print('Кофейня работает в убыток!')
else:
    print('Кофейня работает в ноль.')
