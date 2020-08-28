class Shape():
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,l,w):
        self.width = l
        self.length = w

    def calculate_perimeter(self):
        return 2*(self.width+self.length)

class Square(Shape):
    def __init__(self,l):
        self.s1 = l

    def calculate_perimeter(self):
        return 4*self.s1

    def change_length(self,p):
        self.s1 = self.s1+p

square = Square(40)
square.what_am_i()
rect = Rectangle(20,40)
rect.what_am_i()