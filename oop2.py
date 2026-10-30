import math
class Circle:
    def __init__(self, r):
        self.radius = r
    def get_area(self):
        return math.pi * self.radius * self.radius
    def get_circumference(self):
        return 3.14 * self.radius*2
    def print_details(self):
        print("Radius: ", self.radius)
        print("Circumference is", self.get_circumference())
        print("Area is", self.get_area())
circle_1 = Circle(5)
circle_1.print_details()

#TODO branching,pull request, merging