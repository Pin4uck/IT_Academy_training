from data import Durak


class ConsoleRenderer:
    def card_2_str(self, card):
        return '[' + ''.join(card) + ']' if card is not None else '[  ]'

    def cards_2_str(self, cards, enum=True):
        if enum:
            cards = (f"{i}. {self.card_2_str(c)}" for i, c in enumerate(cards, start=1))
        else:
            cards = (self.card_2_str(c) for c in cards)
        return ", ".join(cards)

    def render_game(self, durak: Durak, my_index=None):
        print('*' * 100)

        print(f'Козырь – {durak.full_trump}, {len(durak.deck)} карт в колоде осталось.')

        for player in durak.players:
            marker = " <-- атакующий" if player.index == durak.attacker_index else ""
            me_marker = " (это я)" if player.index == my_index else ""
            defend = " <-- отбивающий " if player.index == durak.opponent_player.index else ""
            podkid = " <-- подкидывает " if player.index == durak.current_player.index else ""
            print(f"{player.index + 1}: {self.cards_2_str(player.cards)}{marker}{me_marker}{defend}{podkid}")

        if durak.field:
            pairs = list(durak.field.items())
            for i, (ac, dc) in enumerate(pairs, start=1):
                print(f'{i}. Ходит: {self.card_2_str(ac)} - отбиться: {self.card_2_str(dc)}')

    def sep(self):
        print('*' * 100)

    def help(self):
        self.sep()
        print('Помощь')
        print('  1. a [номер] -- атаковать картой')
        print('  2. d [номер] -- отбиваться картой')
        print('  3. n -- следующий игрок подкидывает карты')
        print('  4. f -- завершить ход, (если не отбился - берет все карты)')
        print('  5. q -- выход')
        self.sep()
