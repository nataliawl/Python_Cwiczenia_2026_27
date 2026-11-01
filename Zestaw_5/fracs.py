import math
import unittest

def find_common_denominator(frac1, frac2):
    if frac1[1] == 0 or frac2[1] == 0:
        raise ZeroDivisionError
    comm_denominator = math.lcm(frac1[1], frac2[1])

    new_frac1 = [comm_denominator / frac1[1], comm_denominator]
    new_frac2 = [comm_denominator / frac2[1], comm_denominator]
    return new_frac1, new_frac2

def reduce_two_fracs(frac1, frac2):
    if frac1[1] == 0 or frac2[1] == 0:
        raise ZeroDivisionError

    comm_devisor_1 = math.gcd(frac1[0], frac2[1])
    comm_devisor_2 = math.gcd(frac1[1], frac2[0])
    new_frac1 = [frac1[0] / comm_devisor_1, frac1[1] / comm_devisor_2]
    new_frac2 = [frac2[0]/ comm_devisor_2, frac2[1] / comm_devisor_1]

    return new_frac1,new_frac2

def add_frac(frac1, frac2):  # frac1 + frac2
    if frac1[1] == 0 or frac2[1] == 0:
        raise ZeroDivisionError
    new_frac1, new_frac2 = find_common_denominator(frac1, frac2)
    return [new_frac1[0] + new_frac2[0], new_frac1[1]]

def sub_frac(frac1, frac2): # frac1 - frac2
    if frac1[1] == 0 or frac2[1] == 0:
        raise ZeroDivisionError
    new_frac1, new_frac2 = find_common_denominator(frac1, frac2)
    return [new_frac1[0] - new_frac2[0], new_frac1[1]]

def mul_frac(frac1, frac2): # frac1 * frac2
    if frac1[1] == 0 or frac2[1] == 0:
        raise ZeroDivisionError
    new_frac1, new_frac2 = reduce_two_fracs(frac1, frac2)
    return [new_frac1[0] * new_frac2[0], new_frac1[1] * new_frac2[1]]

def div_frac(frac1, frac2):  # frac1 / frac2
    if frac1[1] == 0 or frac2[1] == 0 or is_zero(frac2):
        raise ZeroDivisionError
    rev_frac2 = [frac2[1], frac2[0]]
    return mul_frac(frac1, rev_frac2)

def is_positive(frac):  # bool, czy dodatni
    if frac[1] == 0:
        raise ZeroDivisionError
    if (frac[0] <= 0 and frac[1] < 0) or (frac[0] >= 0 and frac[1] > 0):
        return True
    return False

def is_zero(frac):  # bool, typu [0, x]
    if frac[1] == 0:
        raise ZeroDivisionError
    return True if frac[0] == 0 else False

def cmp_frac(frac1, frac2):  # -1 | 0 | +1
    if frac1[1] == 0 or frac2[1] == 0:
        raise ZeroDivisionError
    float_frac1 = frac2float(frac1)
    float_frac2 = frac2float(frac2)
    if float_frac1 == float_frac2:
        return 0
    if float_frac1 > float_frac2:
        return -1
    return 1

def frac2float(frac) -> float:  # konwersja do float
    if frac[1] == 0:
        raise ZeroDivisionError
    return float(frac[0] / frac[1])

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)


class TestFractions(unittest.TestCase):

    def setUp(self):
        self.banned = [0, 0]
        self.zero = [0, 1]
        self.half = [1, 2]
        self.half_2 = [-1, -2]
        self.half_minus = [-1, 2]
        self.one_third = [1, 3]
        self.one_third_2 = [2, 6]
        self.two_third = [2, 3]
        self.four = [8,2]

    def test_add_frac(self):
        self.assertRaises(ZeroDivisionError, add_frac, self.banned, self.one_third)
        self.assertEqual(add_frac(self.half, self.one_third), [5, 6])

    def test_sub_frac(self):
        self.assertRaises(ZeroDivisionError, sub_frac, self.banned, self.one_third)
        self.assertEqual(sub_frac(self.half, self.one_third), [1, 6])
        self.assertEqual(sub_frac(self.one_third, self.half), [-1, 6])

    def test_mul_frac(self):
        self.assertRaises(ZeroDivisionError, mul_frac, self.banned, self.one_third)
        self.assertEqual(mul_frac(self.half, self.one_third), [1 , 6])
        self.assertEqual(mul_frac(self.two_third, self.half), [1, 3])

    def test_div_frac(self):
        self.assertRaises(ZeroDivisionError, div_frac, self.one_third, self.zero)
        self.assertRaises(ZeroDivisionError, div_frac, self.banned, self.one_third)
        self.assertEqual(div_frac(self.half, self.one_third), [3 , 2])
        self.assertEqual(div_frac(self.two_third, self.one_third), [2, 1])

    def test_is_positive(self):
        self.assertRaises(ZeroDivisionError, is_positive, self.banned)
        self.assertTrue(is_positive(self.half))
        self.assertTrue(is_positive(self.half_2))
        self.assertFalse(is_positive(self.half_minus))

    def test_is_zero(self):
        self.assertRaises(ZeroDivisionError, is_zero, self.banned)
        self.assertTrue(is_zero(self.zero))
        self.assertFalse(is_zero(self.half))

    def test_cmp_frac(self):
        self.assertRaises(ZeroDivisionError, cmp_frac, self.banned, self.one_third)
        self.assertEqual(cmp_frac(self.half, self.one_third), -1)
        self.assertEqual(cmp_frac(self.one_third, self.half), 1)
        self.assertEqual(cmp_frac(self.one_third, self.one_third_2), 0)

    def test_frac2float(self):
        self.assertRaises(ZeroDivisionError, frac2float, self.banned)
        self.assertEqual(frac2float(self.four), 4)
        self.assertEqual(frac2float(self.zero), 0)
        self.assertEqual(frac2float(self.one_third), float(1/3))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy