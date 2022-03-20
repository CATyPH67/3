class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "%s %s " % (self.x, self.y)


class Rectangle:

    def __init__(self, point1: Point, point2: Point):
        if (point1.x >= point2.x) or (point1.y >= point2.y):
            raise Exception("A rectangle with such vertices cannot exist")

        self.point1 = point1
        self.point2 = point2

    def __str__(self):
        return "%s %s " % (self.point1, self.point2)

    def is_entered_in(self, rec: "Rectangle"):
        if (self.point1.x >= rec.point1.x) and (self.point1.y >= rec.point1.y) \
                and (self.point2.x <= rec.point2.x) and (self.point2.y <= rec.point2.y):
            return True
        else:
            return False

    def find_perimetr(self):
        return ((self.point2.x - self.point1.x) + (self.point2.y - self.point1.y)) * 2
