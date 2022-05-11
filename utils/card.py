class Symbol:
    """ Class representing the symbols of the cards """

    def __init__(self, color, icon) -> str:
        """Constructor of This Class"""
        self.color = color
        self.icon = icon

class Card(Symbol):
    def __init__(self, color, icon, value) -> str:
        super().__init__(color, icon)
        self.value = value

    
    def generating_cards(self):
        
        return f"{self.color}{self.icon}{self.value}"

# call the card to generate the cards
colorr = ["Black", "Red"]
iconn = ["♥", "♦", "♣", "♠"]
vallue = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
counter_of_cardes = 0
for each_color in colorr:
    for each_icon in iconn:
        for each_value in vallue:
            C = Card("Black","♦","3")
            print(C.generating_cards())

            #counter_of_cardes += 1

            
#print(counter_of_cardes)
           