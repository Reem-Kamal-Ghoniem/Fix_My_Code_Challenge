#!/usr/bin/python3
class Square:
    def __init__(self, width=0):
        self.width = width

    def area_of_my_square(self):
        """ Area of the square """
        if self.width < 0:
            return "Width must be non-negative"
        return self.width * self.width

    def perimeter_of_my_square(self):
        return self.width * 4

    def __str__(self):
        return "{}/{}".format(self.width, self.width)

if __name__ == "__main":
    s = Square(width=12)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.perimeter_of_my_square())
