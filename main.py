def get_coords(textmsg):
    str_val = input(textmsg).split()
    while len(str_val) != 2 or not all(map(str.isdigit, str_val)):
        str_val = input('Некорректный ввод. Попробуйте ещё раз: ').split()
    return tuple(map(int, str_val))


def check_win(coord_list):  #Проверяет победу после последнего добавленного элемента
    x = [(coord_list[-1][0], i) for i in range(3)] #Строчка
    if all(map(lambda a: a in coord_list, x)):
        return True
    x = [(i, coord_list[-1][1]) for i in range(3)] #Столбец
    if all(map(lambda a: a in coord_list, x)):
        return True
    if coord_list[-1][0] == coord_list[-1][1]: #Главаня диагональ
        x = [(i, i) for i in range(3)]
        if all(map(lambda a: a in coord_list, x)):
            return True
    if coord_list[-1][0] + coord_list[-1][1] == 2: #Побочная диагональ
        x = [(i, 2-i) for i in range(3)]
        if all(map(lambda a: a in coord_list, x)):
            return True
    return False


def print_field(fields):
    field = [['x' if (i, j) in fields[0][1] else 'o' if (i, j) in fields[1][1] else '-' for j in range(3)] for i in range(3)]
    field = list(map(' '.join, field))
    print('  0 1 2')
    print('\n'.join([f'{i} {field[i]}' for i in range(3)]))


def run_game():
    fields = (('крестик', []), ('нолик', []))
    element = 0
    while len(fields[0][1]) < 5:
        x = get_coords(f'Введите коордиаты для {fields[element][0]}а: ')
        while True:
            if x in fields[0][1] + fields[1][1]:
                x = get_coords('Клетка уже занята. Попробуйте ещё раз: ')
            elif not (0 <= x[0] <= 2 and 0 <= x[1] <= 2):
                x = get_coords('Выход за рамки игрового поля. Попробуйте ещё раз: ')
            else:
                break
        fields[element][1].append(x)
        print_field(fields)
        if check_win(fields[element][1]):
            print(f'{fields[element][0].title()}и победили!')
            return element
        element = 1-element
    print('Ничья!')
    return -1


if __name__ == '__main__':
    run_game()
