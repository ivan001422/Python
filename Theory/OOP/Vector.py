from typing import Union

class Point:

    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

class Vector:

    def __init__(self, *args:Union[Point, tuple]) -> None:
        self._points = []
        self.add(*args)

    def __repr__(self):
        s = ", ".join(repr(s) for s in self._points)
        return f"Vector({s})"

    def __len__(self):
        return len(self._points)

    def __getitem__(self, index):
        return self._points[index]

    @property
    def average(self) -> tuple:
        """Средние координаты всех точек."""
        if not(self._points):raise ValueError("Vector is empty")
        ax = sum(s.x for s in self._points) / len(self._points)
        ay = sum(s.y for s in self._points) / len(self._points)
        return (ax, ay)

    @staticmethod
    def _topoint(point:Union[tuple, Point]) -> Point:
        """
        Преобразует кортеж или Point в точку.

        Args:
            point: Объект Point или кортеж (x, y).

        Returns:
            Point: преобразованная точка.

        Raises:
            TypeError: если аргумент не подходит.
        """
        try:
            if isinstance(point, Point):
                return point
            elif isinstance(point, tuple):
                if len(point) != 2:raise TypeError(f"tuple must have exactly 2 elements, got {len(point)}")
                x = point[0]
                y = point[1]
                return Point(x, y)
            else:
                raise TypeError(f"expected Point or tuple, got {type(point).__name__}")
        except (IndexError, TypeError) as e:
            raise TypeError(f"Invalid argument for topoint: {point!r}") from e

    def add(self, *args) -> None:
        """
        Принимает: tuple | Point
        Делает: Преобразует данные в Point(с проверками)
        Возвращает: None (Добавляет точки в _points)
        """
        for point in args:
            self._points.append(Vector._topoint(point))



vec1 = Vector((1,2), (3,4)) # Инициализация через tuple
print(vec1)

p1 = Point(1,2)
p2 = Point(3, 4)
vec2 = Vector(p1, p2) # Инициализация через Point
print(vec2)

print(vec1.average)
vec1.add(p1,p2)
vec2.add((1,2), (3,4))

print(vec1)
print(vec2)
print(vec1[0])


