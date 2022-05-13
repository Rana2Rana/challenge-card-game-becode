class Symbol:
    """ Class representing the symbols of the cards """

    def __init__(self, color, icon) -> str:
        """Constructor of This Class"""
        self.color = color
        self.icon = icon

class Card(Symbol):  # The Card class inherits from Symbol class
    def __init__(self, color, icon, value) -> str:
        super().__init__(color, icon)
        self.value = value

    
    def __str__ (self):    # def the function that creat one card
        
        return f"{self.color}{self.icon}{self.value}"

# C = Card('Black',"♠","6")
# print(C)
