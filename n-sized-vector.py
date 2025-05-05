""" This script defines a class Vector which can be initialized to any dimension """

from typing import Union
import math

class Vector:
    def __init__(self, *values: float):
        # Use a tuple to create a vector of n-dimensions
        self._values = tuple(float(v) for v in values)
        
        print(self) # Print to console once a new Vector is created

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


    # Mathematical Methods from here
    def __sub__(self, other: Union[float, "Vector"]) -> "Vector":
        if isinstance(other, (int, float)):
            # Check if the other element is of type int or float
            return Vector(*(v - other for v in self))
        
        elif isinstance(other, Vector):
            # If not int or float, check if they are of Vector type
            if len(self) != len(other):
                # If the other element is of type Vector, they both need to have the same length
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

# --- Class definition end for class Vector ---
