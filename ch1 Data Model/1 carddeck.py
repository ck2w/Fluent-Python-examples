import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card('7', 'diamonds')
print beer_card

deck = FrenchDeck()
print len(deck)
print deck[0]
print choice(deck)  # pick a random card

# advantages: easy to remember methods; use rich Python standard library

# slice
print deck[:3]

# iterable
for card in deck:
    # print card
    pass

# sorting
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    # by rank then by suit
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print card

# special methods should be called by the Python interpreter

# better to call the related built-in function: len, iter, str, etc, faster than method calls

print 'end'
