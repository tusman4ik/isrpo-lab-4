import unittest

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero_radius(self):
        """Тест площади круга с нулевым радиусом"""
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_positive_radius(self):
        """Тест площади круга с положительным радиусом"""
        res = area(5)
        self.assertEqual(res, 78.53981633974483)

    def test_area_negative_radius(self):
        """Тест площади круга с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            area(-5)

    def test_perimeter_zero_radius(self):
        """Тест периметра круга с нулевым радиусом"""
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_positive_radius(self):
        """Тест периметра круга с положительным радиусом"""
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)

    def test_perimeter_negative_radius(self):
        """Тест периметра круга с отрицательным радиусом"""
        with self.assertRaises(ValueError):
            perimeter(-5)


if __name__ == '__main__':
    unittest.main()