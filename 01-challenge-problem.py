class Point:
    def __init__(self, coordinate_X, coordinate_Y):
        self.coordinate_X = coordinate_X
        self.coordinate_Y = coordinate_Y


class Rectangle:
    def __init__(self, top_cordinate, width, height):
        self.top_cordinate = top_cordinate
        self.width = width
        self.height = height

        bottom_x_cordinate = top_cordinate.coordinate_X + width
        bottom_y_cordinate = top_cordinate.coordinate_Y + height
        self.bottom_cordinate = Point(bottom_x_cordinate, bottom_y_cordinate)

    def calc_area(self):
        return self.width * self.height

    def display_co_ordinates(self):
        print('Starting Point (X)): ' + str(self.top_cordinate.coordinate_X))
        print('Starting Point (Y)): ' + str(self.top_cordinate.coordinate_Y))
        print('End Point X-Axis (Top Right): ' + str(self.bottom_cordinate.coordinate_X))
        print('End Point Y-Axis (Bottom Left): ' + str(self.bottom_cordinate.coordinate_Y))


top_cordinate = Point(50,100)
width =90
height = 10
redctangle = Rectangle(top_cordinate, width, height)

print(redctangle.calc_area())
redctangle.display_co_ordinates()
