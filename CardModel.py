"""The Card Model

This module contains all the code for the playing card object
"""

import pytest

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


class Card:
    """
    This is a class for a playing card
    """
    def __init__(self, suit, value):
        """
        The constructor for a playing card

        Args:
            suit (int): The suit of the playing card
            value (int): The value of the playing card
        """
        self._value = card_values[value]
        self._suit = Suits[suit]

    @property
    def suit(self):
        """str: The suit of the card"""
        return self._suit

    def value(self):
        """str: the value of the card"""
        return self._value

    def __str__(self):
        """str: gives a description of the card"""
        return self._value + ' of ' + self._suit


def test_playing_card():
    test_card = Card(0, 0)
    assert(str(test_card) == 'Ace of Clubs')

