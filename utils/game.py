from numpy import insert    
from player import Deck, Player


class Board:
    """ Constructor of Board class
    which has 
    1. players as a list of all players
    2. turn_count to display the number of turn in the game
    3. active_cards as an attribute that contain tha last card played by each player
    4. history_cards as an attribute that will contain all the cards played since the start of the game
   """
    def __init__(self) -> None:
        self.players = []
        self.turn_count = 0
        self.active_cards = ""    
        self.history_cards = [] 

    def start_game(self):
        start = True
        game = Deck()
        game.fill_deck()
        game.shuffle()
        number_of_players = int(input("Enter the number of players: "))
        
        for z in range(number_of_players):
           x = Player()
           y = input("Enter the name of the player: ")
           self.players.insert(z,x.Player(y))
        print(self.players)
        Player_card = game.distribute(self.players)
        for each_player in self.players:
            each_player.play()           
        



# a = Board()
# print(a.start_game())
        
        
        # while start == True: