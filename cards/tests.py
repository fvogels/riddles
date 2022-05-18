'''
This is a logic puzzle which allows you to check your solution using Python.

Alice and Bob have once again been imprisoned under the watch of a crazy logician warden
who promises to let them free if they can solve the puzzle or otherwise they face a terrible fate.

The warden picks five cards from a standard playing card deck and gives them to Alice.
Alice may stack the cards in any order then give them back to the warden.
The warden will give the top four cards of the stack to Bob.
Bob must now deduce which card the warden is still holding.
Alice and Bob may discuss strategy beforehand but once the process starts
they can only communicate via the special order of cards Alice gives back to the warden.

Can you help Alice and Bob escape this time?
'''

import itertools
from collections import namedtuple
from typing import List

# Set up a standard deck of cards.
VALUES = ['ACE', *[str(i) for i in range(2, 11)], 'JACK', 'QUEEN', 'KING']
SUITS = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']
Card = namedtuple('Card', 'value suit')
DECK = [Card(value, suit) for value, suit in itertools.product(VALUES, SUITS)]
assert len(DECK) == 52





def special_sort(five_cards: List[Card]):
    """
    === IMPLEMENT THIS ===
    Shuffles the five_cards such that predict_next can do its job sucessfully.
    """
    # Dummy implementation.
    five_cards[:] = [five_cards[0], five_cards[1], five_cards[3], five_cards[2], five_cards[4]]

def predict_next(four_cards: List[Card]) -> Card:
    """
    === IMPLEMENT THIS ===
    Predicts the next card in the specially shuffled five card sequence
    of which we only know the first four cards.
    """
    # Dummy implementation.
    return Card('ACE', 'SPADES')


def check(five_cards: List[Card]):
    """
    Checks that special_sort and predict_next are implemented properly.
    """
    original = set(five_cards)
    special_sort(five_cards)
    assert set(five_cards) == original and len(five_cards) == 5, "Oi! No cheating!"
    guess = predict_next(five_cards[:4])
    assert five_cards[4] == guess, f"{guess} was the wrong prediction for last card of {five_cards}"


check(DECK[:5])

# The warden is adversarial - any 5 cards could be chosen and you'll need to deal with it.
for i, five_cards in enumerate(itertools.combinations(DECK, 5)):
    check(list(five_cards))
    if i and i % 10000 == 0:
        print('works so far :) ', i, '/', 2598960, five_cards)
print('congratulations! :D')