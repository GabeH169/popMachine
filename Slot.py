# Class Slot represents a slot in a pop machine that holds an
# item and tracks the quantity in stock
# @Gabriel H
from Item import Item
class Slot:
  
    def setItem(self, newItem):
        self.item = newItem
    def getItem(self):
        return self.item
    
    def setQuantity(self, newQuantity):
        self.quantity = newQuantity if newQuantity > 0 else 0
    def getQuantity(self):
        return self.quantity
    
    def __init__(self, item, quantity=0):
        self.setItem(item)
        self.setQuantity(quantity)

    # purchase deducts the amount from the quantity field
    # @param amount is the amount deducted
    # @return a str containing the item and the quantity
    def purchase(self, amount):
        if amount > 0 and self.getQuantity() >= amount:
            self.setQuantity(self.getQuantity() - amount)
    def __str__(self):
        return f'{self.getItem()}, {self.quantity}'
