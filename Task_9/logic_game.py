from console_view import ConsoleRenderer
from data import Durak


def logic_game():
    g = Durak()
    renderer = ConsoleRenderer()
    renderer.help()

    while not g.winner:
        renderer.render_game(g, my_index=0)
        renderer.sep()
        choice = input('Ваш выбор: ')
        parts = choice.lower().split(' ')
        if not parts:
            break
        command = parts[0]
        try:
            if command == 'f' and g.field:
                r = g.finish_turn()
                print(f'Ход окончен: {r}')
            elif command == 'n':
                g.next()
            elif command == 'a':
                index = int(parts[1]) - 1
                card = g.current_player[index]
                if not g.attack(card, g.current_player):
                    print('Вы не можете ходить с этой карты!')
            elif command == 'd':
                index = int(parts[1]) - 1
                new_card = g.opponent_player[index]
                def_index = int(input(f'Какую позицию отбить {new_card}? ')) - 1
                old_card = list(g.field.keys())[def_index]
                if not g.defend(old_card, new_card):
                    print('Не можете так отбиться')
            elif command == 'q':
                print('QUIT!')
                break
        except IndexError:
            print('Неправильный выбор карты')
        except ValueError:
            print('Введите число через пробел после команды')
        if g.winner:
            print(f'GAME OVER! The winner is player #{g.winner + 1}')
            break


if __name__ == '__main__':
    logic_game()
