import unittest

def perimeter(a, b):
    return (a + b) * 2

class RectangleTestCase(unittest.TestCase):
    def test_rectangle_plus(self):
        res = perimeter(10, 20)
        self.assertEqual(res, 60)

    def test_square_plus(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
    def test_rectangle_plus1(self):
        res = perimeter(10, 20)
        self.assertEqual(res, 60)

    def test_square_plus1(self):
        res = perimeter(10, 10)
        self.assertEqual(res, 40)
