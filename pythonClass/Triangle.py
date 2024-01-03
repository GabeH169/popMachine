# @Gabriel Haro-Villa
# Class Triangle represents a triangle. It can use the base and height
# to get the area of the triangle.
class Triangle:
    def __init__(self, base =1, height =1):
        self.setBase(base)
        self.setHeight(height)

    def setBase(self, base):
        if base <= 0:
            raise ValueError(f"Illegal argument for triangle base: {base}")
        self.base = base

    def setHeight(self, height):
        if height <= 0:
            raise ValueError(f"Illegal argument for triangle height: {height}")
        self.height = height
    
    def getBase(self):
        return self.base
    
    def getHeight(self):
        return self.height

    # getArea calculates the area of the triangle using (base * height) / 2
    # @return the area of the triangle
    def getArea(self):
        self.area = (self.base * self.height) / 2
        return self.area
    
    def __str__(self):
        return (f"Base: {self.base}, Height: {self.height}")