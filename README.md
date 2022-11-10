pydnbdev
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

## Install

``` sh
pip install pydnbdev
```

## How to use

This package defines a Deck of playing cards

``` python
from pydnbdev.deck import Deck
```

``` python
d = Deck()
d
```

    A♣️; 2♣️; 3♣️; 4♣️; 5♣️; 6♣️; 7♣️; 8♣️; 9♣️; 10♣️; J♣️; Q♣️; K♣️; A♦️; 2♦️; 3♦️; 4♦️; 5♦️; 6♦️; 7♦️; 8♦️; 9♦️; 10♦️; J♦️; Q♦️; K♦️; A❤️; 2❤️; 3❤️; 4❤️; 5❤️; 6❤️; 7❤️; 8❤️; 9❤️; 10❤️; J❤️; Q❤️; K❤️; A♠️; 2♠️; 3♠️; 4♠️; 5♠️; 6♠️; 7♠️; 8♠️; 9♠️; 10♠️; J♠️; Q♠️; K♠️

``` python
d.shuffle()
d
```

    5♠️; 2♦️; 4♣️; A♣️; K♦️; 8♣️; 10♦️; K♠️; 2❤️; 10♣️; 10♠️; 6❤️; Q♣️; 3♠️; K❤️; 8♦️; 2♣️; Q♠️; 10❤️; 7❤️; 6♣️; 6♠️; K♣️; J♦️; 4♦️; 9♦️; A♠️; 9♠️; 7♠️; 2♠️; J❤️; 7♣️; 4❤️; 3❤️; 9♣️; Q❤️; 8♠️; A❤️; 5❤️; 8❤️; 5♦️; 4♠️; J♣️; A♦️; 6♦️; 3♦️; 5♣️; Q♦️; 7♦️; 3♣️; J♠️; 9❤️

``` python
d.pop()
```

    9❤️