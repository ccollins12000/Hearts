"""The Deck Model

This module contains all the code for the deck of cards object
"""

import pytest
import CardModel
import random

Suits = [
    'Clubs',
    'Hearts',
    'Diamonds',
    'Spades'
]

card_values = [
    'Ace',
    'Two',
    'Three',
    'Four',
    'Five',
    'Six',
    'Seven',
    'Eight',
    'Nine',
    'Ten',
    'Jack',
    'Queen',
    'King'
]


class Deck:
    """
    This is a class for a deck of playing card
    """

    def __init__(self):
        self._cards = []
        self._reset()

    def shuffle(self):
        """Shuffles the cards"""
        random.shuffle(self._cards)

    def deal_card(self):
        """obj: returns a card from the deck"""
        return self._cards.pop()

    def __str__(self):
        text = ''
        for card in self._cards:
            text += str(card) + '\n'
        return text

    def _reset(self):
        """Recreates the deck. Cards will be in order. Shuffle must be called after _reset for a random deck"""
        self._cards = []
        for suit_index in range(0, len(Suits)):
            for value_index in range(0, len(card_values)):
                self._cards.append(CardModel.Card(suit_index, value_index))


def test_create_deck():
    test_deck = Deck()
    assert (str(test_deck) ==
            'Ace of Clubs\nTwo of Clubs\nThree of Clubs\nFour of Clubs\nFive of Clubs\nSix of Clubs\n' +
            'Seven of Clubs\nEight of Clubs\nNine of Clubs\nTen of Clubs\nJack of Clubs\nQueen of Clubs' +
            '\nKing of Clubs\nAce of Hearts\nTwo of Hearts\nThree of Hearts\nFour of Hearts' +
            '\nFive of Hearts\nSix of Hearts\nSeven of Hearts\nEight of Hearts\nNine of Hearts' +
            '\nTen of Hearts\nJack of Hearts\nQueen of Hearts\nKing of Hearts\nAce of Diamonds\n' +
            'Two of Diamonds\nThree of Diamonds\nFour of Diamonds\nFive of Diamonds\nSix of Diamonds' +
            '\nSeven of Diamonds\nEight of Diamonds\nNine of Diamonds\nTen of Diamonds\nJack of Diamonds' +
            '\nQueen of Diamonds\nKing of Diamonds\nAce of Spades\nTwo of Spades\nThree of Spades\n' +
            'Four of Spades\nFive of Spades\nSix of Spades\nSeven of Spades' +
            '\nEight of Spades\nNine of Spades\nTen of Spades'
            '\nJack of Spades\nQueen of Spades\nKing of Spades\n'
            )


def test_deal_card():
    test_deck = Deck()
    assert(str(test_deck.deal_card()) == 'King of Spades')
