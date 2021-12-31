import math
from scipy.special import cbrt
A = int(input('Введите коэфициент А:'))
B = int(input('Введите коэфициент B:'))
C = int(input('Введите коэфициент C:'))
D = int(input('Введите коэфициент D:'))

S = (4 * (3 * A * C - B ** 2) ** 3 + (2 * B ** 3 - 9 * A * B * C + 27 * A ** 2 * D) ** 2) / (2916 * A ** 6)
p = (3 * A * C - B ** 2) / (3 * A ** 2)
q = (2 * B ** 3 - 9 * A * B * C + 27 * A ** 2 * D) / (27 * A ** 3)


if S < 0:
    if q < 0:
        F = math.atan((math.sqrt(-(q ** 2 / 4 + p ** 3 / 27))) / (-q / 2))
    elif q > 0:
        F = math.atan((math.sqrt(-(q ** 2 / 4 + p ** 3 / 27))) / (-q / 2)) + math.pi
    else:
        F = math.pi/2
    x1 = 2 * math.sqrt(-p / 3) * math.cos(F / 3) - B / (3 * A)
    x2 = 2 * math.sqrt(-p / 3) * math.cos(F / 3 + (2 * math.pi) / 3) - B / (3 * A)
    x3 = 2 * math.sqrt(-p / 3) * math.cos(F / 3 + (4 * math.pi) / 3) - B / (3 * A)
    print(f'x1 = {x1}, X2 = {x2}, x3 = {x3}')
elif S > 0:
    y1 = (-1 / 2) * (cbrt(-q / 2 + math.sqrt((q ** 2) / 4 + (p ** 3) / 27)) + cbrt(-q / 2 - math.sqrt((q ** 2) / 4 + (p ** 3) / 27))) - B / (3 * A)
    y2 = math.sqrt(3) / 2 * (cbrt(-q / 2 + math.sqrt((q ** 2) / 4 + (p ** 3) / 27)) - cbrt(-q / 2 - math.sqrt((q ** 2) / 4 + (p ** 3) / 27)))
    x1 = cbrt(-q / 2 + math.sqrt((q ** 2) / 4 + (p ** 3) / 27)) + cbrt(-q / 2 - math.sqrt((q ** 2) / 4 + (p ** 3) / 27)) - B / (3 * A)
    print(f'x1 = {x1}')
    print('x2 = ', y1, ' + ', ' i ', ' * ', y2)
    print('x3 = ', y1, ' - ', ' i ', ' * ', y2)
elif S == 0:
    y1 = 2 * cbrt(-q/2)
    y2 = -cbrt(-q/2)
    x1 = y1 - 4
    x2 = y2 - 4
    x3 = y2 - 4
    print(f'x1 = {x1}, X2 = {x2}, x3 = {x3}')
