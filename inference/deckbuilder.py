"""
Base class for deckbuilding algorithms
"""

class Deckbuilder():
    
    def __init__(self, cards):
        assert len(cards) != 0
        self.cards = cards
        
    
    def build_deck(self):
        # data structure of the deck is a dictionary of the length of self.cards
        # with the card names as keys and the number of copies of the 
        # respective cards as values
        raise NotImplementedError()

    def test_deck_legality(self,min_nr_of_cards = 60):
        # Test if deck contains at least the allowed number of cards
        assert sum(self.deck.values()) >= min_nr_of_cards
        # Test that no nonbasic land appears more than four times
        basic_lands = ['Forest','Plains','Swamp','Mountain','Island']
        for card in self.deck:
            if card not in basic_lands:
                assert self.deck[card] <= 4