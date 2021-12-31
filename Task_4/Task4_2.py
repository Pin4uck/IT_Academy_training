from decimal import Decimal  # имеем дело с деньгами


def valid():  # функция валидации данных ввода, может и намудрил, но мне было интересно сделать так
    list_input = ['Enter the amount of the check:', 'Enter the number of persons:', 'Enter the amount of each person, for example "30,20,100":']
    input_data = []  # переменная для накопления данных ввода
    for i in range(len(list_input)):
        while True:
            try:
                [input_data.append(int(num)) for num in input(f'{list_input[i]}\n').strip(' ').split(',')]
                if i == 2 and len(input_data) != input_data[1] + 2:  # на случай если количество человек не совпадает с количеством сумм
                    input_data = input_data[0:2]  # убираем из списка ошибочный ввод
                    raise RuntimeError('Incorrect input, the number of persons must match the number of amounts.')
                if i == 2 and input_data[0] != sum(input_data[2:]):  # на случай если сумма чека не совпадает с суммами персон
                    input_data = input_data[0:2]  # убираем из списка ошибочный ввод
                    raise RuntimeError('Incorrect input, the amount of the check doesn\'t match the amount of payment.')
                break
            except RuntimeError as Error:
                print(Error)
                continue
            except (TypeError, ValueError):
                print('Incorrect input, please try again!')
                continue
    return input_data


def get_debt(inp_data):  # передаем список - где под индексом 0 - общая сумма, 1 - количество персон, остальные - это суммы персон
    results = []  # накапливаем вывод
    # имея дело с деньгами правильнее в начале округлить до сотых, то есть до копеек, или можно и в конце при выводе??? если в конце - то остаток меньше выходит
    sum_each = (Decimal(str(inp_data[0])) / Decimal(str(inp_data[1])))  # сумму чека делим на количество персон
    person_amount = {f'Person №{i - 1}': Decimal(str(inp_data[i])) for i in range(2, len(inp_data))}  # создаем словарь с каждой персоной и её суммой
    creditors = {}  # создадим словарь с кредиторами, можно было бы использовать списки, не знаю как лучше
    debtors = {}  # создадим словарь с должниками
    for k, v in person_amount.items():  # алгоритм по наполнению словарей creditors и debtors
        if v > sum_each:  # сумма больше средней - ему должны
            creditors[k] = Decimal(str(v)) - Decimal(str(sum_each))  # сумма которую кредитору должны
        elif v < sum_each:  # сумма меьшн средней - он должен
            debtors[k] = Decimal(str(sum_each)) - Decimal(str(v))  # сумма которую должник должен
    if creditors == {}:  # словарь пустой, значит все заплатили поровну
        results = ['Everything is fine, there are no debtors']
        return results
    count1 = 0  # счетчик итерация первого цикла for
    for k, v in creditors.items():
        count1 += 1
        count2 = 0  # счетчик итерация второго цикла for
        while v != 0:  # пока не обнулим долг кредитору итерируемся по должникам ниже
            for k1, v1 in debtors.items():
                count2 += 1
                if v1 == 0:  # пропускаем должника если он уже отдал деньги
                    continue
                if v >= v1:  # если данному кредитору должны больше чем должен данный должник
                    v = Decimal(str(v)) - Decimal(str(v1))  # отнимаем долг
                    results.append(f'{k1} owes {k} - {round(float(v1), 2):.2f}')
                    debtors[k1] = 0  # данный должник отдал
                    if count1 == len(creditors) and count2 == len(debtors):  # может образоваться остаток, который му остаемся должны
                        print('We will owe -', v)
                        v = 0  # останавливаем цикл while
                elif v < v1:  # если данному кредитору должны меньше чем должен данный должник
                    v1 = Decimal(str(v1)) - Decimal(str(v))  # отнимаем сумму кредитора
                    debtors[k1] = v1  # и изменяем сумму которую остался должен должник
                    results.append(f'{k1} owes {k} - {round(float(v), 2):.2f}')
                    v = 0
                    if count1 == len(creditors) and count2 == len(debtors) and v1 != 0:  # при какой-то комбинации цифр могут образоваться чаевые
                        print('Tips', v1)
                        v = 0
                    break
    return results


for i in get_debt(valid()):  # вывод результата из списка, не знаю насколько корректно в аргументы функции запихивать функцию
    print(i)
