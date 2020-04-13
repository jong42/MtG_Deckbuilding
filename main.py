"""
Task: Implement an AI for deckbuilding in Magic:The Gathering
"""

from inference.randombuilder import RandomBuilder

cards = ['Mountains','Hill Giant'] # cards are given as strings for now
deckbuilder = RandomBuilder(cards)
deck = deckbuilder.build_deck()

print(deck)

