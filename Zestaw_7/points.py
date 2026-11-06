import math
import unittest

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self):  # zwraca string "(x, y)"
        return '(' + str(self.x) + ", " + str(self.y) + ')'

    def __repr__(self): # zwraca string "Point(x, y)"
        return 'Point' + str(self)

    def __eq__(self, other):   # obsługa point1 == point2
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other):  # v1 + v2
        if not isinstance(other, Point):
            raise TypeError
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):  # v1 - v2
        if not isinstance(other, Point):
            raise TypeError
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, other):  # v1 * v2, iloczyn skalarny, zwraca liczbę
        if not isinstance(other, Point):
            raise TypeError
        return self.x * self.y + other.x * other.y

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D, zwraca liczbę
        if not isinstance(other, Point):
            raise TypeError
        return self.x * other.y - self.y * other.x

    def length(self):         # długość wektora
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __hash__(self):
        return hash((self.x, self.y))   # bazujemy na tuple, immutable points

# Kod testujący moduł.


class TestPoint(unittest.TestCase):
    def setUp(self):
        self.point24 = Point(2, 4)
        self.point24_clone = Point(2, 4)
        self.point32 = Point(3,2)
        self.pom_int = 5

    def test_str(self):
        self.assertEqual(str(self.point24), '(2, 4)')

    def test_repr(self):
        self.assertEqual(repr(self.point24), 'Point(2, 4)')

    def test_eq(self):
        self.assertTrue(self.point24 == self.point24_clone)
        self.assertFalse(self.point24 == self.point32)
        self.assertFalse(self.point24 == self.pom_int)

    def test_ne(self):
        self.assertFalse(self.point24 != self.point24_clone)
        self.assertTrue(self.point24 != self.point32)
        self.assertTrue(self.point24 != self.pom_int)

    def test_add(self):
        self.assertRaises(TypeError, lambda: self.point24 + self.pom_int)
        self.assertEqual(self.point24 + self.point24, Point(4, 8))

    def test_sub(self):
        self.assertRaises(TypeError, lambda: self.point24 - self.pom_int)
        self.assertEqual(self.point24 - self.point24, Point(0, 0))

    def test_mul(self):
        self.assertEqual(self.point24 * self.point24, 16)
        self.assertRaises(TypeError, lambda: self.point24 * self.pom_int)

    def test_cross(self):
        self.assertRaises(TypeError, lambda: self.point24.cross(self.pom_int))
        self.assertEqual(self.point24.cross(self.point24), 0)

    def test_length(self):
        self.assertEqual(self.point24.length(), math.sqrt(20))

if __name__ == '__main__':
    unittest.main()