#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A card game called War created as the Capstone Project for Unit 7.

Created on Sat May 23 12:37:16 2020

@author: Mark Thomas
"""
from dataclasses import dataclass
from enum import IntEnum
from random import shuffle


class Suit(IntEnum):
    """ An enumeration of the four traditional card suits.
    Suits can be compared. Spades>Hearts>Diamonds>Clubs
    """
    CLUBS = 0
    DIAMONDS = 1
    HEARTS = 2
    SPADES = 3

    def __str__(self):
        return self.name.title()


@dataclass(order=True)
class Card:
    " Represents a Playing Card with a rank & suit. "
    # data attributes (__init__ is generated)
    rank: int
    suit: Suit

    def __str__(self):
        return f'{self.rank!s} of {self.suit!s}'


class Deck:
    """ Represents a shuffled deck of cards
    from which pairs of cards are dealt.
    """

    def __init__(self):
        self.cards = []
        for rank in range(2, 10):
            for suit in Suit:
                self.cards.append(Card(rank, suit))
        shuffle(self.cards)

    def deal(self):
        " Returns two cards taken from the deck. "
        return self.cards.pop(), self.cards.pop()

    def cards_left(self):
        " Returns the number of cards left in the deck. "
        return len(self.cards) > 0


class Player:
    " Represents one of two players in the game of War. "

    def __init__(self, name):
        self.name = name
        self.cards = []

    def __gt__(self, other):
        return len(self.cards) > len(other.cards)

    def __eq__(self, other):
        return len(self.cards) == len(other.cards)

    def __str__(self):
        return self.name

    def take_cards(self, cards):
        " Adds the cards supplied to the player's hand. "
        self.cards += cards

    def status(self):
        " Returns a string describing the player's current status. "
        return f'{self.name} has {len(self.cards)} cards'


def play_game():
    " Runs a game of War between two players. "

    name1 = input("What's your name? Player 1: ")
    player1 = Player(name1)
    name2 = input("What's your name? Player 2: ")
    player2 = Player(name2)

    deck = Deck()

    while deck.cards_left():
        input('Deal?')
        cards = deck.deal()
        print(f'''Cards drawn are:
    {cards[0]} for {player1}
    {cards[1]} for {player2}''')
        if cards[0] > cards[1]:
            print(f'{player1} wins this draw')
            player2.take_cards(cards)
        else:
            print(f'{player2} wins this draw')
            player1.take_cards(cards)

    print('\nGame Over')
    print(f'    {player1.status()}')
    print(f'    {player2.status()}')
    if player1 == player2:
        print("It's a draw")
    else:
        winner = player1 if player1 < player2 else player2
        print(f'    {winner} wins')

if __name__ == '__main__':
    play_game()
