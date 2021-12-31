# Задание: Написать функцию для вычисления суммы всех элементов вложенных (любая глубина) списков.
# Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элементов - 34
list_num = [1, 2, [2, 4, [[7, 8], 4, 6]]]


def sum_nested_list(collection):
    result = 0
    for i in collection:
        try:
            result += sum_nested_list(i)
        except TypeError:
            result += i
    return result


if __name__ == '__main__':
    sum_nested_list(list_num)
