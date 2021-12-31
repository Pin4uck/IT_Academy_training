import data


def create_calc_str(string):  # находим выражение в скобках, так как они подсчитываются в первую очередь
    start = string.rfind('(')  # находим последнюю открывающуюся скобку
    if start == -1:
        return string
    end = string.find(')', start)  # находим первую закрывающуюся скобку после последней открывающейся скобки
    calc_str = string[start+1:end]
    return calc_str  # выводим выражение которое в скобках


def create_calc_list(calc_str):  # преобразуем строку в список '2*-2' -> [2, '*', -2]
    num_acc = ''  # с помощью этой переменной собираем число из строки
    calc_list = []  # в список поочередно добавляем числа и знаки со строки
    for i in range(len(calc_str)):  # итерируемся по строке
        if (i == 0 and calc_str[0] == '-') or (i != 0 and (calc_str[i-1] == '*' or calc_str[i-1] == '/') and calc_str[i] == '-'):  # если в начале строки "-" или после знака "*" или "/", тогда этот минус относится к числу
            num_acc += calc_str[i]
            continue
        if calc_str[i] == '.':  # если есть точка, то она относится к числу
            num_acc += calc_str[i]
            continue
        if calc_str[i].isdigit():  # если на итерации число
            num_acc += calc_str[i]  # добавляем в строку
            try:
                if not calc_str[i+1].isdigit() and calc_str[i+1] != '.':  # если на следующей итерации нет числа
                    calc_list.append(float(num_acc))  # то добавляем то что накопилось
                    num_acc = ''  # и обнуляем аккумулятор
            except IndexError:  # если вышли за диапазон
                calc_list.append(float(num_acc))  # добавляем число
        else:
            calc_list.append(calc_str[i])  # в этом случае добавляются операторы со строки
    return calc_list


def calculate_list(calc_list):  # функция высчитывает выражение в списке
    oper_1 = None
    oper_2 = None
    while oper_1 != -1 and oper_2 != -1:  # пока в списке есть оператор умножения или деления - то выполняем операции
        if oper_1 != -1:
            try:
                oper_1 = calc_list.index('*')
                calc_list[oper_1 - 1] = calc_list[oper_1 - 1] * calc_list[oper_1 + 1]
                calc_list.pop(oper_1), calc_list.pop(oper_1)
            except ValueError:
                oper_1 = -1
        if oper_2 != -1:
            try:
                oper_2 = calc_list.index('/')
                calc_list[oper_2 - 1] = calc_list[oper_2 - 1] / calc_list[oper_2 + 1]
                calc_list.pop(oper_2), calc_list.pop(oper_2)
            except ValueError:
                oper_2 = -1
    while len(calc_list) != 1:  # and not calc_list[1].isdigit():  # выполняем все оставшиеся операции
        if calc_list[1] == '+':  # второй элемент по-любому оператор, еслю плюс, то
            calc_list[0] += calc_list[2]  # слаживаем первый и третий элемент
            calc_list.pop(1), calc_list.pop(1)  # и удаляем из списка второй и третий
        elif calc_list[1] == '-':  # по аналогии с сложением
            calc_list[0] -= calc_list[2]
            calc_list.pop(1), calc_list.pop(1)
    return str(calc_list[0])


def string_count(string):  # это функция высчитывает полное поступившее выражение
    while True:
        substring = create_calc_str(string)  # выбираем нужную подстроку
        calc_bracket = calculate_list(create_calc_list(substring))  # высчитываем её
        string = string.replace(f'({substring})', calc_bracket)  # подставляем высчитанную подстроку обратно в строку
        if '(' not in string:  # если в строке нет скобки, значит высчитываем строку сразу целиком
            string = string.replace(substring, calc_bracket)
        if '+-' in string:  # заменяем двойные знаки если они есть
            string = string.replace('+-', '-')
        elif '--' in string:
            string = string.replace('--', '+')
        if string.isdigit() or string[1:].isdigit():  # если строка число, мы высчитали выражение. Если число отрицательное - убираем минус в начале и проверяем
            break
        if string.count('.') == 1 and (string.replace('.', '').isdigit() or string[1:].replace('.', '').isdigit()):  # если в строке есть одна точка а все остальное числа, мы высчитали выражение
            break
    if string.endswith('.0'):
        string = round(float(string))
    return string


def valid(inp_data):
    # TODO implement validation
    expression = inp_data.replace(' ', '')
    return expression


def show_results():
    res = data.results
    if res:
        return f'Your saved results: {str(res)[1:-1]}'
    else:
        return 'You haven\'t saved your results yet'


def save_result(result):
    return data.save_result(result)


def clear():
    return data.clear_result()
