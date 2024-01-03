# @Gabriel Haro-Villa
# Class Soda represents a soda with a name, price, and ounces.
from Item import Item
class Soda(Item):
    def __init__(self, name="", price=0, ounces=0):
        super().__init__(name, price)
        self.setOunces(ounces)

    def setOunces(self, ounces):
        if ounces > 0:
            self.ounces = ounces
        else:
            self.ounces = 0
    
    def getOunces(self):
        return self.ounces
    
    def __str__(self):
        return super().__str__() + f', {self.ounces}'
    
