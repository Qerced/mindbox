import math


class GeometryCalculator:
    @staticmethod
    def circle_area(radius: int | float) -> float:
        """
        Вычисляет площадь круга по его радиусу.

        :param radius: Радиус круга
        :return: Площадь круга

        >>> GeometryCalculator.circle_area(5)
        78.53981633974483
        """
        return math.pi * radius ** 2

    @staticmethod
    def triangle_area(
        side1: int | float, side2: int | float, side3: int | float
    ) -> float:
        """
        Вычисляет площадь треугольника по трём его сторонам.

        :param side1: Длина первой стороны
        :param side2: Длина второй стороны
        :param side3: Длина третьей стороны
        :return: Площадь треугольника

        >>> GeometryCalculator.triangle_area(3, 4, 5)
        6.0
        """
        # Полупериметр треугольника
        s = (side1 + side2 + side3) / 2
        # Площадь треугольника по формуле Герона
        return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
