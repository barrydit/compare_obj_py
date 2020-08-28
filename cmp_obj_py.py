class Square():
    def __init__(self, s):
        self.s1 = s

square_one = Square(5)
square_one_sm = square_one

def object_is(obj1, obj2): 
    if obj1 is obj2: 
        return True 
    else:
        return False 

print(object_is(square_one, square_one_sm))