import random

# масти
SPADES = '♠'
HEARTS = '♥'
DIAMS = '♦'
CLUBS = '♣'

# достоинтсва карт
NOMINALS = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# поиск индекса по достоинству
NAME_TO_VALUE = {n: i for i, n in enumerate(NOMINALS)}

# карт в руке при раздаче
CARDS_IN_HAND_MAX = 6

# эталонная колода (каждая масть по каждому номиналу) - 36 карт
DECK = [(nom, suit) for nom in NOMINALS for suit in [SPADES, HEARTS, DIAMS, CLUBS]]


def rotate(l, n):
    return l[n:] + l[:n]


class Player:
    def __init__(self, index, cards, mast):
        self.index = index
        self.cards = list(map(tuple, cards))
        self.mast = mast

    def take_cards_from_deck(self, deck: list):
        lack = max(0, CARDS_IN_HAND_MAX - len(self.cards))
        n = min(len(deck), lack)
        self.add_cards(deck[:n])
        del deck[:n]
        return self

    def add_cards(self, cards):
        self.cards += list(cards)
        self.sort_hand(self.mast)
        return self

    def sort_hand(self, trum):
        count = []
        self.cards.sort(key=lambda c: (NAME_TO_VALUE[c[0]], c[1]))
        for i in range(len(self.cards)):
            if self.cards[i][1] == trum:
                count.append(i)
        j = 0
        for i in count:
            self.cards.append(self.cards.pop(i - j))
            j += 1
        return self

    def take_card(self, card):
        self.cards.remove(card)

    def __repr__(self):
        return f"Player{self.cards!r}"

    def __getitem__(self, item):
        return self.cards[item]


class Durak:
    NORMAL = 'normal'
    TOOK_CARDS = 'took_cards'
    GAME_OVER = 'game_over'

    def __init__(self):
        self.attacker_index = 0

        self.rng = random.Random()

        self.deck = list(DECK)
        self.rng.shuffle(self.deck)

        self.trump = self.deck[-1][1]
        self.full_trump = f'{self.deck[-1][0]}{self.deck[-1][1]}'
        self.N_PLAYERS = 6

        self.players = [Player(i, [], self.trump).take_cards_from_deck(self.deck)
                        for i in range(self.N_PLAYERS)]

        self.field = {}
        self.winner = None
        self.kef = 0
        self.current_player = self.players[self.attacker_index]

        self.list_c = [i for i in range(self.N_PLAYERS)]

    @property
    def opponent_player(self):
        return self.players[(self.attacker_index + 1) % self.N_PLAYERS]

    @property
    def attacking_cards(self):
        return list(filter(bool, self.field.keys()))

    @property
    def defending_cards(self):
        return list(filter(bool, self.field.values()))

    def finish_turn(self):
        took_cards = False
        status = False
        self.kef = 0
        if any(def_card is None for _, def_card in self.field.items()):
            self.take_all_field()
            took_cards = True
        else:
            self.field = {}

        for p in rotate(self.players, self.attacker_index):
            p.take_cards_from_deck(self.deck)
            if not p.cards and len(self.players) > 2:
                status = True
                ind = p.index
                if took_cards:
                    if self.opponent_player.index == len(self.players) - 1:
                        self.attacker_index = 0
                    elif self.opponent_player.index == 0:
                        self.attacker_index = 1
                    else:
                        self.attacker_index = self.opponent_player.index
                else:
                    self.attacker_index = self.opponent_player.index - 1
                    if self.attacker_index < 0:
                        self.attacker_index = 0
                del self.players[p.index]
                self.N_PLAYERS -= 1
                for i in self.players:
                    if i.index > ind:
                        i.index -= 1
                self.current_player = self.players[self.attacker_index]
            else:
                self.winner = p.index
                return self.GAME_OVER

        if took_cards and not status:
            if self.opponent_player.index == len(self.players) - 1:
                self.attacker_index = 0
            else:
                self.attacker_index = self.opponent_player.index + 1
            self.current_player = self.players[self.attacker_index]
            return self.TOOK_CARDS
        elif not status:
            self.attacker_index = self.opponent_player.index
            self.current_player = self.players[self.attacker_index]
            return self.NORMAL

    def take_all_field(self):
        cards = self.attacking_cards + self.defending_cards
        self.opponent_player.add_cards(cards)
        self.field = {}

    def attack(self, card, cur):
        if not self.can_add_to_field(card):
            return False
        cur.take_card(card)
        self.field[card] = None
        return True

    def can_add_to_field(self, card):
        if not self.field:
            return True
        for attack_card, defend_card in self.field.items():
            if self.card_match(attack_card, card) or self.card_match(defend_card, card):
                return True
        return False

    def card_match(self, card1, card2):
        if card1 is None or card2 is None:
            return False
        n1, _ = card1
        n2, _ = card2
        return n1 == n2

    def defend(self, attacking_card, defending_card):
        if self.field[attacking_card] is not None:
            return False
        if self.can_beat(attacking_card, defending_card):
            self.field[attacking_card] = defending_card
            self.opponent_player.take_card(defending_card)
            return True
        return False

    def can_beat(self, card1, card2):
        nom1, suit1 = card1
        nom2, suit2 = card2
        nom1 = NAME_TO_VALUE[nom1]
        nom2 = NAME_TO_VALUE[nom2]

        if suit2 == self.trump:
            return suit1 != self.trump or nom2 > nom1
        elif suit1 == suit2:
            return nom2 > nom1
        else:
            return False

    def next(self):
        if self.opponent_player.index == len(self.list_c) - 1:
            num_pl_rev = self.list_c
        else:
            num_pl_rev = rotate(self.list_c, self.opponent_player.index - len(self.players) + 1)
        self.current_player = self.players[num_pl_rev[self.kef]]
        self.kef += 1
        if self.kef == self.N_PLAYERS - 1:
            print('все подкинули')
            self.kef = 0
            self.finish_turn()
        return self
