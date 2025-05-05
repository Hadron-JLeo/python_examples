""" This script defines a class Vector which can scale to any dimension """

from typing import Union
import math

class Vector:
    def __init__(self, *values: float):
        self._values = tuple(float(v) for v in values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, index):
        return self._values[index]

    def __iter__(self):
        return iter(self._values)

    def __repr__(self):
        return f"Vector{self._values}"

    def __eq__(self, other):
        return isinstance(other, Vector) and self._values == other._values

    def __add__(self, other: Union[float, "Vector"]) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(*(v + other for v in self))
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must be of the same dimension")
            return Vector(*(a + b for a, b in zip(self, other)))
        return NotImplemented

    def __sub__(self, other: Union[float, "Vector"]) -> "Vector":
        if isinstance(other, (int, float)):
            return Vector(*(v - other for v in self))
        elif isinstance(other, Vector):
            if len(self) != len(other):
                raise ValueError("Vectors must be of the same dimension")
            return Vector(*(a - b for a, b in zip(self, other)))
        return NotImplemented

    def magnitude(self) -> float:
        return math.sqrt(sum(x ** 2 for x in self))

    def normalize(self) -> "Vector":
        mag = self.magnitude()
        if mag == 0:
            raise ZeroDivisionError("Cannot normalize a zero vector")
        return Vector(*(x / mag for x in self))

