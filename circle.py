import math


def area(r):
    """
    Args:
        r (float|int): радиус круга
    Return:
        (float|int): площадь круга
    """
    if r < 0:
        raise ValueError("Радиус не может быть негативным")
    return math.pi * r * r


def perimeter(r):
    """
    Args:
        r (float|int): радиус круга
    Return:
        (float|int): периметр круга
    """
    if r < 0:
        raise ValueError("Радиус не может быть негативным")
    return 2 * math.pi * r