from random import shuffle

def game_start():
    deck = [
    2,3,4,5,6,7,8,9,"J","Q","K","A",
    2,3,4,5,6,7,8,9,"J","Q","K","A",
    2,3,4,5,6,7,8,9,"J","Q","K","A",
    2,3,4,5,6,7,8,9,"J","Q","K","A"]
    shuffle(deck)
    gamer_hand = [deck.pop(i) for i in range(2)]
    croupier_hand = [deck.pop(i) for i in range(2)]
    return gamer_hand, croupier_hand, deck

def main():
    gamer_hand, croupier_hand, current_deck = game_start()
    print(gamer_hand, croupier_hand, current_deck)
    pass

if __name__ == "__main__":
    main()