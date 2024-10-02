import math

class Circle:
    def __init__(self, radius, x_center=0, y_center=0):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def intersection_area(self, other_circle):
        d = math.sqrt((self.x_center - other_circle.x_center) ** 2 + (self.y_center - other_circle.y_center) ** 2)
        if d >= self.radius + other_circle.radius:
            return 0  # No intersection
        if d <= abs(self.radius - other_circle.radius):
            return math.pi * min(self.radius, other_circle.radius) ** 2

        r1, r2 = self.radius, other_circle.radius
        part1 = r1 ** 2 * math.acos((d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d * r1))
        part2 = r2 ** 2 * math.acos((d ** 2 + r2 ** 2 - r1 ** 2) / (2 * d * r2))
        part3 = 0.5 * math.sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2))
        return part1 + part2 - part3
class Rectangle:
    def __init__(self, width, height, x=0, y=0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def intersection_area(self, other_rectangle):
        x_overlap = max(0, min(self.x + self.width, other_rectangle.x + other_rectangle.width) - max(self.x, other_rectangle.x))
        y_overlap = max(0, min(self.y + self.height, other_rectangle.y + other_rectangle.height) - max(self.y, other_rectangle.y))
        return x_overlap * y_overlap

print(Circle(2).intersection_area(Circle(3)))