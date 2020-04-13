# -*- coding: utf-8 -*-
"""
Trivial deckbuilding algorithm
"""

import random
from inference.deckbuilder import Deckbuilder

class RandomBuilder(Deckbuilder):
    
    def build_deck(self):
        basics = ['Forest','Plains','Swamp','Mountain','Island']
        deck = dict.fromkeys(self.cards, 0)
        
        while sum(deck.values()) < 60:
            # Randomly increment one card
            k = random.choice(list(deck.keys()))
            if deck[k] < 4 or k in basics:
                deck[k] += 1
        self.deck = deck
        self.test_deck_legality()
        return deck

    