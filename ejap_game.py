from enum import Enum, IntEnum
import random

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

# Shuffle a given deck n times


def shuffleDeck(deckToShuffle, numOfShuffles):

    while numOfShuffles > 0:

        x = int(len(deckToShuffle))
        shuffledDeck = []

        for i in range(0, x):
            randCard = randint(0, len(deckToShuffle)-1)
            card = deckToShuffle.pop(randCard)
            shuffledDeck.append(card)

        numOfShuffles -= 1

    return shuffledDeck

# Shuffles a deck AS A LIST


def test(deck):
    return random.shuffle(deck)


def printDeck(deck):
    for card in deck:
        print(card.value, " of ", card.suit)


createDeck()
currentDeck = list(fullDeck)
test(currentDeck)
printDeck(currentDeck)
