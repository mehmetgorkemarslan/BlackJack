from random import shuffle

class Hand:
    possible_value = []
    
    def calculate_value(self):
        #It calculates the value of the hand.
        def calculate_value_in(hand):
            value = 0
            for card in hand:
                if card in ["J","Q","K"]:
                    value += 10
                elif card == "A":
                    pass
                else:
                    value += int(card)
            return value
        if not "A" in self.hand:
            value = calculate_value_in(self.hand)
            self.possible_value = [value]
        else:
            # It can be enhanced with a nested list.
            a_count = self.hand.count("A")
            if a_count == 1:
                value = calculate_value_in(self.hand)
                self.possible_value = [value+1 ,value+11]
            elif a_count == 2:
                value = calculate_value_in(self.hand)
                self.possible_value = [value+2, value+12, value+22]
            elif a_count == 3:
                value = calculate_value_in(self.hand)
                self.possible_value = [value+3, value+13, value+23, value+33]
            else:
                value = calculate_value_in(self.hand)
                self.possible_value = [value+4, value+14, value+24,value+34, value+44]
        self.possible_value.sort()
                
    def __init__(self, hand):
        self.hand = hand
        self.calculate_value()

    def draw_a_card(self,deck):
        self.hand.append(deck.pop())
        #do not need to returrn and chance deck list, because list are reference variable.
        self.calculate_value()

def game_start():
    #It creates a deck, shuffles, and draws a total of 4 cards for 2 people.
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
    a = "~"*18
    gamer, croupier, current_deck = game_start()
    print(gamer.hand)
    print(gamer.possible_value)
    print(a)
    while True:
        go = input("Pick Card? y/n: ")
        if go == "y":
            gamer.draw_a_card(current_deck)
            print(gamer.hand)
            print(gamer.possible_value)
            print(a)
        else:
            break
    pass

if __name__ == "__main__":
    main()