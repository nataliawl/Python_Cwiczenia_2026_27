import unittest
from .points import Point

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        # Chcemy, aby x1 < x2, y1 < y2.
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

    def intersection(self, other): # część wspólna prostokątów
        if not isinstance(other, Rectangle):
            raise ValueError("Argument musi być prostokątem!")
        if (self.pt2.x < other.pt1.x or other.pt2.x < self.pt1.x
                or self.pt2.y < other.pt1.y or other.pt2.y < self.pt1.y):
            return None
        return Rectangle(max(self.pt1.x, other.pt1.x), max(self.pt1.y, other.pt1.y),
                         min(self.pt2.x, other.pt2.x), min(self.pt2.y, other.pt2.y))

    def cover(self, other): # prostokąt nakrywający oba
        if not isinstance(other, Rectangle):
            raise ValueError("Argument musi być prostokątem!")
        return Rectangle(min(self.pt1.x, other.pt1.x), min(self.pt1.y, other.pt1.y),
                         max(self.pt2.x, other.pt2.x), max(self.pt2.y, other.pt2.y))

    def make4(self): # zwraca krotkę czterech mniejszych
        center_pt = self.center()
        rec_A = Rectangle(self.pt1.x , center_pt.y , center_pt.x , self.pt2.y)
        rec_B = Rectangle(center_pt.x , center_pt.y , self.pt2.x , self.pt2.y)
        rec_C = Rectangle(center_pt.x , self.pt1.y , self.pt2.x , center_pt.y)
        rec_D = Rectangle(self.pt1.x , self.pt1.y , center_pt.x , center_pt.y)
        return rec_A, rec_B, rec_C, rec_D

        # A-------B   po podziale  A---+---B
        # |       |                |   |   |
        # |       |                +---+---+
        # |       |                |   |   |
        # D-------C                D---+---C

# Kod testujący moduł.

class TestRectangle(unittest.TestCase):
   def setUp(self):
       self.rectangle24 = Rectangle(2, 4, 4, 8)
       self.rectangle24_clone = Rectangle(2, 4, 4, 8)
       self.rectangle46 = Rectangle(4, 6, 6, 10)
       self.rectangle510 = Rectangle(5, 10, 7, 12)
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

   def test_intersection(self):
       self.assertRaises(ValueError, self.rectangle24.intersection, self.pom_int)
       rec36 = self.rectangle24.intersection(self.square3)
       self.assertTrue(rec36 == Rectangle(3, 4, 4, 6))
       rec_none = self.rectangle24.intersection(self.rectangle510)
       self.assertTrue(rec_none is None)

   def test_cover(self):
       self.assertRaises(ValueError, self.rectangle24.cover, self.pom_int)
       rec23 = self.rectangle24.cover(self.square3)
       self.assertTrue(rec23 == Rectangle(2, 3, 6, 8))

   def test_make4(self):
       rec_A, rec_B, rec_C, rec_D = self.rectangle24.make4()
       self.assertTrue(rec_A == Rectangle(2, 6, 3, 8))
       self.assertTrue(rec_B == Rectangle(3, 6, 4, 8))
       self.assertTrue(rec_C == Rectangle(3, 4, 4, 6))
       self.assertTrue(rec_D == Rectangle(2, 4, 3, 6))

if __name__ == '__main__':
    unittest.main()

