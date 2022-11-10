# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/card.ipynb.

# %% auto 0
__all__ = ['Card']

# %% ../nbs/card.ipynb 3
class Card:

    suits = ["♣️", "♦️", "❤️", "♠️"]
    ranks = [None, "A"] + [str(x) for x in range(2,11)]  + ["J", "Q", "K"]

    "Represents a standard playing card."
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
        self.suit_nm= self.suits[self.suit]
        self.rank_nm = self.ranks[self.rank]

    def __eq__(self, other): 
        return (self.suit, self.rank) == (other.suit, other.rank)

    def __lt__(self, other): 
        return (self.suit, self.rank) < (other.suit, other.rank)

    def __str__(self): 
        return f'{self.rank_nm}{self.suit_nm}'
    
    __repr__ = __str__


