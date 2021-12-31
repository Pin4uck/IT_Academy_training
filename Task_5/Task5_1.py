# Задание: Binary Search (рекурсивный, в идеале без слайсов)
list_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
x = len(list_numbers) - 1


def binary_search(checklist, value, start=0, end=x):
    mid_index = start + (end - start) // 2
    if checklist[mid_index] == value:
        return f'The index of the element you are looking for is: {mid_index}.'
    elif start == end:
        return 'The element you are looking for is missing.'
    elif checklist[mid_index] > value:
        return binary_search(checklist, value, start, mid_index-1)
    elif checklist[mid_index] < value:
        return binary_search(checklist, value, mid_index+1, end)


if __name__ == '__main__':
    binary_search(list_numbers, 11)
