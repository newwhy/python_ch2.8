# class MyStr

class MyStr:
    def __init__(self, s):
        self.s = s

    def __truediv__(self, other):
        return self.s.split(other)




s = MyStr('Hello Python')


