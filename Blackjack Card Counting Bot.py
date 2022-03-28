def Main():
    cardcounter()
def cardcounter():
    count = 0
    deck =int(decksize())
    cards = []
    while (cards != "stop"):
        cards = cardactivity()
        for card in cards:
            if (card == "A") or (card == "J") or (card == "Q") or (card == "K") or (card == "1"):
                count = count - 1
            elif (card == "2") or (card == "3") or (card == "4") or (card == "5") or (card == "6"):
                count = count + 1
        print("count:")
        print(count)
        print("truecount:")
        print(count/deck)



def decksize():
    return input("How many decks are being used total?\n")

def cardactivity():
    return input("What cards have been played?\n")

Main()
