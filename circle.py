import math


def area(r):
    """
    Args:
        r (float|int): радиус круга
    Return:
        (float|int): площадь круга
    """
    return math.pi * r * r


def perimeter(r):
     """
    Args:
        r (float|int): радиус круга
    Return:
        (float|int): периметр круга
    """
    return 2 * math.pi * r

