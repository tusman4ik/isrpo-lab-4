
def area(a):
    """
    Args:
        a(float|int): длинна стороны квадрата
    Returns:
        (float|int): площадь квадрата
    """

    if a < 0:
        raise ValueError("Сторона не может быть негативной")
    return a * a


def perimeter(a):
    """
    Args:
        a(float|int): длинна стороны квадрата
    Returns:
        (float|int): периметр квадрата
    """
    if a < 0:
        raise ValueError("Сторона не может быть негативной")
    return 4 * a
