class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def computeArea(self):
        area = (self.height * self.width)
        return area

    def printAttributes(self):
        print('Height = {}'.format(self.height))
        print('Width = {}'.format(self.width))

r = Rectangle(7, 8)
Rectangle.printAttributes(r)
print ('-'*10)
print('Area = {}'.format(Rectangle.computeArea(r)))