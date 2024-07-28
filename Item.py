# Class Item represents an item with a name and a price
# @Gabriel H
class Item:
    def __init__(self, newName = "", newPrice = 0):
        self.setName(newName)
        self.setPrice(newPrice)
        
    def setName(self, newName):
        self.name = newName
    def getName(self):
        return self.name

    def setPrice(self, newPrice):
        self.price = newPrice if newPrice > 0 else 0
    def getPrice(self):
        return self.price

    def __str__(self):
        return f"{self.getName()},{self.getPrice():.2f}"
