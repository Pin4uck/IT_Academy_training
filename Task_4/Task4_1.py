def valid():  # функция валидации данных ввода
    while True:
        try:
            list_num = sorted(set([int(num) for num in input('Enter a list of numbers, for example "2, 8, 9":\n').strip(' ').split(',')]))
            return list_num
        except (TypeError, ValueError):
            print('Incorrect input, please try again!')
            continue


def get_ranges(l_num):
    result = ''
    count = 0  # счетчик, при помощи которого мы потом определяем первое число диапазона
    if len(l_num) == 1:  # на случай если длинна списка равна 1
        result += str(l_num[0])
    for i in range(1, len(l_num)):  # начинаю с индекса 1
        count += 1
        if l_num[i-1] < l_num[i] - 1:  # если соседи различаются более чем на 1
            x1 = l_num[i - count]  # если до этого был диапазон, то это первое число диапазона
            x2 = l_num[i - 1]
            x3 = l_num[i]
            if count == 1 and i == len(l_num) - 1:  # до этого соседи были различны более чем на 1 и последняя итерация
                result += f'{str(x2)}, {str(x3)}'
            elif count == 1:  # если count=1 то это первая итерация, или на предыдущей итерации соседи были различны более чем на 1
                result += f'{str(x2)}, '
            elif count > 1 and i == len(l_num) - 1:  # был диапазон и последняя итерация
                result += f'{str(x1)}-{str(x2)}, {x3}'
            elif count > 1:  # если count>1 то был диапазон
                result += f'{str(x1)}-{str(x2)}, '
            count = 0  # обнуляем счетчик если соседи различны более чем на 1
        elif i == len(l_num) - 1:  # если имеет место диапазон и список кончается
            x1 = l_num[i - count]
            x3 = l_num[i]
            result += f'{str(x1)}-{str(x3)}'
    return result


get_ranges(valid())
