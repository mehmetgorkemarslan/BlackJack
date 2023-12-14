from random import shuffle

class Hand:
    possible_value = []
    def __init__(self, hand):
        self.hand = hand
    
    def draw_a_card(self,deck):
        self.hand.append(deck.pop())
        #do not need to returrn and chance deck list, because list are reference variable


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
    print(gamer.hand, current_deck)
    gamer.draw_a_card(current_deck)
    print(gamer.hand, current_deck)
    pass

if __name__ == "__main__":
    main()