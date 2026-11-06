import unittest
from .points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        if x1 >= x2 or y1 >= y2:
            raise ValueError("Górny róg musi być wyżej od dolnego")

        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.horizontal = self.pt2.x - self.pt1.x
        self.vertical = self.pt2.y - self.pt1.y

    def __str__(self):      # "[(x1, y1), (x2, y2)]"
        return '[' + str(self.pt1) + ', ' + str(self.pt2) + ']'

    def __repr__(self):     # "Rectangle(x1, y1, x2, y2)"
        return 'Rectangle(' + str(self.pt1.x) + ', ' + str(self.pt1.y) + ', ' + str(self.pt2.x) + ', ' + str(self.pt2.y)  + ')'

    def __eq__(self, other):   # obsługa rect1 == rect2
        if isinstance(other, Rectangle):
            if self.pt1.x == other.pt1.x and self.pt1.y == other.pt1.y:
                return self.pt2.x == other.pt2.x and self.pt2.y == other.pt2.y
        return False

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):           # zwraca środek prostokąta
        center_pt = self.pt1 + self.pt2
        return Point(center_pt.x / 2, center_pt.y / 2)

    def area(self):            # pole powierzchni
        return self.horizontal * self.vertical

    def move(self, x, y):      # przesunięcie o (x, y)
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y

# Kod testujący moduł.

class TestRectangle(unittest.TestCase):
   def setUp(self):
       self.rectangle24 = Rectangle(2, 4, 4, 8)
       self.rectangle24_clone = Rectangle(2, 4, 4, 8)
       self.rectangle46 = Rectangle(4, 6, 6, 10)
       self.square3 = Rectangle(3, 3, 6, 6)
       self.pom_int = 3

   def test_init(self):
       self.assertRaises(ValueError, Rectangle, 4, 8 , 2, 4)
       self.assertRaises(ValueError, Rectangle, 4, 4, 8, 4)

   def test_str(self):
       self.assertEqual(str(self.rectangle24), "[(2, 4), (4, 8)]")

   def test_repr(self):
       self.assertEqual(repr(self.rectangle24), "Rectangle(2, 4, 4, 8)")

   def test_eq(self):
       self.assertTrue(self.rectangle24 == self.rectangle24_clone)
       self.assertFalse(self.rectangle24 == self.square3)
       self.assertFalse(self.rectangle24 == self.pom_int)

   def test_ne(self):
       self.assertFalse(self.rectangle24 != self.rectangle24_clone)
       self.assertTrue(self.rectangle24 != self.square3)
       self.assertTrue(self.rectangle24 != self.pom_int)

   def test_center(self):
       self.assertTrue(self.rectangle24.center() == Point(3, 6))

   def test_area(self):
       self.assertTrue(self.rectangle24.area() == 8)
       self.assertTrue(self.square3.area() == 9)

   def test_move(self):
       self.rectangle24.move(2, 2)
       self.assertTrue(self.rectangle24 == self.rectangle46)
       self.setUp()

if __name__ == '__main__':
    unittest.main()

