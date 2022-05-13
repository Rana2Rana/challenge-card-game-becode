from card import Card
import random

class Player:
    """ constructor of Player class """
    def __init__(self):   
        
        self.Player = []
        self.card = []       # card is  List of cards that the player has in his hands
        self.history = []   # history is a list of card that  will contain all cards played by the playe
        self.turn_count = 0
        self.number_of_cards = int()

    def play(self):
        
        Card = random.choice(self.card) # to pick a card from cards list randomly
        self.history.append(Card) 
        print(f"{PLAYER_NAME}{TURN_COUNT} played: {CARD_NUMBER} {CARD_SYMBOL_ICON}")
        return self.card
    
    def __str__(self) -> str:
        return self.card
    

# Creating a Deck Class
class Deck(Card):
    def __init__(self,color= ["Black", "Red"], icon =["♥", "♦", "♣", "♠"],value = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  ) -> None:
        super().__init__(color,icon,value)
        self.cards = [] # is attributete which is going to contain a list of instances of Card Class
        self.color = color
        self.icon = icon
        self.value = value
       
    def fill_deck(self):

        """a fill_deck function which creat all the 52 cards
        it return the list of cards """

        for b in self.color:
            if b == "Black":
                for i in self.icon:
                    if i == "♣" or i == "♠":
                        for v in self.value:
                            self.cards.append(Card(b,i, v))
            else:
                for i in self.icon:
                    if i == "♥" or i == "♦":
                        for v in self.value:
                            self.cards.append(Card(b,i, v))
        print(len(self.cards))
        return self.cards

    def shuffle(self) -> list:
        """ The method that will shuffle all the list of cards """

        random.shuffle(self.cards)
        print(self.cards)

    def distribute(self,player) -> list:
        """ a fuction that has a Player list as a parameter
        and return list of list of cards that each player has in his hand """
        
        self.player = player
        card = [[] for n in range(len(self.player))]
       
        t =len(self.cards)/len(self.player)     # To calculate the number of each group of list that will be with each player
        for i in (card): 
            for m in(self.cards):
                i.append(m)
                if len(i) == t: 
                    print(len(i))
                    break
        return card
       
    def __str__(self) -> str:
        
        return f"{self.cards}"