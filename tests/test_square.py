import unittest

from geometric_lib.square import area, perimeter

class SquareTestCase(unittest.TestCase):
    def test_area_zero_side(self):
        """Тест площади квадрата с нулевой стороной"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive_side(self):
        """Тест площади квадрата с положительной стороной"""
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_negative_side(self):
        """Тест площади квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_zero_side(self):
        """Тест периметра квадрата с нулевой стороной"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_side(self):
        """Тест периметра квадрата с положительной стороной"""
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_negative_side(self):
        """Тест периметра квадрата с отрицательной стороной"""
        with self.assertRaises(ValueError):
            perimeter(-5)


if __name__ == '__main__':
    unittest.main()