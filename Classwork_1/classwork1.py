numbers = sorted([{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
    'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
    'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}[word] for word in list(
    set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()))])
num = list()
for i in range(len(numbers)):
    if i == (len(numbers) - 1):
        break
    if i % 2 == 0:
        num.append(numbers[i] * numbers[i + 1])
    else:
        num.append(numbers[i] + numbers[i + 1])
print(num)

num = ([num for num in num if num % 2 == 1])

print(sum(num))

# попытка решить с помощью одной переменной (тоже самое что и выше - только выражение переменной numbers,
# подставлено в цикл вместо самой переменной)

num = list()
for i in range(len(sorted([{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
    'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,'sixteen': 16,
    'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}[word] for word in list(
    set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()))]))):
    if i == (len(sorted([{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
        'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}[word] for word in list(
        set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()))])) - 1):
        break
    if i % 2 == 0:
        num.append(sorted([{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
        'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}[word] for word in
        list(set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()))])[i] *
        sorted([{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}[word] for word in list(
        set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()))])[i + 1])
    else:
        num.append(sorted([{
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
        'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}[word] for word in
        list(set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()))])[i] +
        sorted([{'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}[word] for word in list(
        set('five thirteen two eleven seventeen two one thirteen ten four eight five nineteen'.split()))])[i + 1])
print(num)

num = ([num for num in num if num % 2 == 1])
print(sum(num))
