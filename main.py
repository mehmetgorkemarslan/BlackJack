from random import shuffle
"""
Desteleri Tutacak
Özellikler:
    Kart çekme          21>= olursa yok daha                       kart çekme yapıldı
    Değer Hesaplama
"""
class Cards:
    deck = [
    2,3,4,5,6,7,8,9,10,"J","Q","K","A",
    2,3,4,5,6,7,8,9,10,"J","Q","K","A",
    2,3,4,5,6,7,8,9,10,"J","Q","K","A",
    2,3,4,5,6,7,8,9,10,"J","Q","K","A"
    ]
    shuffle(deck)
    # eli tanımla , 2 kart çek, destenin değerini hesapla, 
    def __init__(self):
        self.hand = []
        self.pick_a_card()
        self.pick_a_card()
        self.calculate_value()

    # Bi kart çekerek hand e ekler. Desteyi ve eli güncelliyor
    def pick_a_card(self):
        self.hand.append(self.deck.pop())

    # Kartların değerini hesaplıyor ve .value içine atıyo. değer 21den büyükse almıyor.
    def calculate_value(self):
        value = 0
        a_count = 0
        for card in self.hand:
            if card in range(2,11):
                value += card
            elif card in ["J", "Q", "K"]:
                value += 10
            else:
                value += 1
                a_count += 1
        values = [value + 10*x for x in range(a_count+1) if value + 10*x <= 21]
        self.value = values


"""
Oyuncuları Tutacak
Özellikler:
    Aynı Kart Varsa İkiye Bölme Özelliği
    Kaç tane istenirse O kadar el açma                      Yapıldı
    Üzerinden deste oluşturma
"""
class Player:
    def __init__(self, count_of_hands):
        self.hands:dict = {}
        for i in range(count_of_hands):
            self.hands[i+1] = Cards()




Gamer = Player(int(input("İstediğin El sayısı: ")))
for hand in Gamer.hands:
    print(Gamer.hands[hand].hand)
    print(Gamer.hands[hand].value)