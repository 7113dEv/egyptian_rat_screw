from enum import Enum, IntEnum
from random import *

# Initializing Deck
fullDeck = []
currentDeck = []

# Card enumeration for playing cards


class card(IntEnum):
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEEN = 12
    KING = 13
    ACE = 14

# Suit enumeration for playing cards


class suit(Enum):
    SPADES = 'spades'
    CLUBS = 'clubs'
    HEARTS = 'hearts'
    DIAMONDS = 'diamonds'

# Playing card class information


class playingCard:
    def __init__(card, value, suit):
        card.value = value
        card.suit = suit


# Create a full deck
def createDeck():
    for s in suit:
        for c in card:
            fullDeck.append(playingCard(card(c), suit(s)))
    return fullDeck


def shuffleDeck(deckToShuffle):
    topHalf = []
    bottomHalf = []
    shuffledDeck = []

    # Separate top half of deck
    for i in range(1, len(deckToShuffle)):
        topHalf.append(deckToShuffle[i])

    # Separate bottom half of deck
    for card in deckToShuffle:
        bottomHalf.append(card)

    while len(shuffledDeck) != len(deckToShuffle):
        shuffledDeck.append(topHalf[len(topHalf)-1])
        topHalf.pop()
        shuffledDeck.append(bottomHalf[len(bottomHalf)-1])
        bottomHalf.pop()

    return shuffledDeck


createDeck()
fullDeck = shuffleDeck(fullDeck)

for card in fullDeck:
    print("Card: ", card.value, " of ", card.suit)
