from random import shuffle

class Hand:
    def __init__(self, hand):
        self.hand = hand


def game_start():
    #It creates a deck, shuffles, and draws a total of 4 cards for 2 people
    deck = [
    2,3,4,5,6,7,8,9,"J","Q","K","A",
    2,3,4,5,6,7,8,9,"J","Q","K","A",
    2,3,4,5,6,7,8,9,"J","Q","K","A",
    2,3,4,5,6,7,8,9,"J","Q","K","A"]
    shuffle(deck)
    gamer = Hand([deck.pop(i) for i in range(2)])
    croupier = Hand([deck.pop(i) for i in range(2)])
    return gamer, croupier, deck

def main():
    gamer, croupier, current_deck = game_start()
    print(gamer.hand, current_deck)
    pass

if __name__ == "__main__":
    main()