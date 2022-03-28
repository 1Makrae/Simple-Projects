def Main():
    cardcounter()
def cardcounter():
    count = 0
    deck = decksize()
    cards = []
    while (cards != "stop"):
        cards = cardactivity()
        card


def decksize():
    return input("How many decks are being used total?\n")

def cardactivity():
    return input("What cards have been played?")

Main()