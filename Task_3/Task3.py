import os  # решил попробовать фичу с урока


def add_space(num_spaces, line_list):
    """
    spaces distribution function
    """
    if num_spaces % (len(line_list) - 1) == 0:  # если нет остатка при делении количества пробелов на количество слов,то
        rang_space = num_spaces // (len(line_list) - 1)  # это - количество пробелов, которое нужно добавить к слову
    else:  # если же имеется остаток от деления
        rang_space = num_spaces // (len(line_list) - 1)
        rang_space_add = num_spaces % (len(line_list) - 1)  # тогда мы добавляем еще одну переменную
        for i in range(len(line_list) - 1):  # здесь мы добавляем пробелы с переменной rang_space_add
            line_list[i] += ' '
            rang_space_add -= 1
            if rang_space_add == 0:
                break
    for i in range(len(line_list) - 1):  # а здесь мы добавляем пробелы с переменной rang_space
        for j in range(rang_space):
            line_list[i] += ' '
    return ' '.join(line_list)


file_name_w = 'w_text.txt'
with open(os.path.join('HomeWork', 'text.txt'), 'r') as f_r, open(os.path.join('HomeWork', file_name_w), 'w') as f_w:
    position = 0  # переменная контролирует положение курсора
    w_line = int(input('Enter line width:'))
    while w_line <= 35:
        print('Your number does not match, please enter a number greater than 35')
        w_line = int(input('Enter line width:'))
    while True:
        f_r.seek(position)  # переводим курсор в нужную позицию
        line = f_r.readline(w_line + 1)  # читаем на один символ больше указанной ширины,чтобы прочесть следующий символ
        position += len(line)
        if line == '\n':  # на случай если вдруг в тексте будет разрыв
            continue
        if line == '':  # выход из цикла в конце файла
            break
        if line[-1] == '\n':  # блок проверяет является ли эта строка концом абзаца
            p = True
        else:
            p = False
        line = line.rstrip('\n')  # убираем символ переноса строки
        if line[-1] == ' ':  # если последний пробел, то удаляем его, а строку записываем
            line = line[:-1]
        elif p is True:  # если последний символ строки '\n', это конец абзаца - запись без форматирования
            pass
        elif ' ' not in line and p is False:  # на случай если ширина слова больше введенной ширины строки
            line = line[:w_line]
        else:  # сюда попадают строки с нецелым словом в конце
            l_list = line.split()  # разбиваем строку по пробелам
            number_of_spaces = len(l_list[-1])  # число пробелов которое необходимо распределить
            position -= number_of_spaces  # число символов на которое необходимо отвести курсор назад
            del l_list[-1]  # удаляем не целое слово из списка
            if len(l_list) == 1:
                line = l_list[0]
            else:
                line = add_space(number_of_spaces, l_list)  # распределяем пробелы
        f_w.write(line + '\n')
    print(f'The formatted text is written to the file "{file_name_w}"')
