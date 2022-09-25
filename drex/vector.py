# future imports --------------------------------------------------------------------- #
from __future__ import annotations

# system imports --------------------------------------------------------------------- #
import math

# vector class ----------------------------------------------------------------------- #
class Vector:
    # initialisation ----------------------------------------------------------------- #
    def __init__(self, x: float | int, y: float | int) -> None:
        self.x = x
        self.y = y

    def __call__(self, x: float | int, y: float | int) -> None:
        self.x = x
        self.y = y

    # comparison operations ---------------------------------------------------------- #
    def __eq__(self, other) -> bool:
        if type(other) != Vector:
            return False
        else:
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False

    def __ne__(self, other) -> bool:
        if type(other) != Vector:
            return True
        else:
            if self.x != other.x or self.y != other.y:
                return True
            else:
                return False

    # unary operations --------------------------------------------------------------- #
    def __abs__(self) -> Vector:
        return Vector(abs(self.x), abs(self.y))

    def __round__(self) -> Vector:
        return Vector(round(self.x), round(self.y))

    def __ceil__(self) -> Vector:
        return Vector(math.ceil(self.x), math.ceil(self.y))

    def __floor__(self) -> Vector:
        return Vector(math.floor(self.x), math.floor(self.y))

    def __trunc__(self) -> Vector:
        return Vector(math.trunc(self.x), math.trunc(self.y))

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y)

    # normal arithmetic operations --------------------------------------------------- #
    def __add__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[a + other for a in self])
        else:
            result = Vector(*[a + b for a, b in zip(self, other)])

        return result

    def __sub__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[a - other for a in self])
        else:
            result = Vector(*[a - b for a, b in zip(self, other)])

        return result

    def __mul__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[a * other for a in self])
        else:
            result = Vector(*[a * b for a, b in zip(self, other)])

        return result

    def __truediv__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[a / other for a in self])
        else:
            result = Vector(*[a / b for a, b in zip(self, other)])

        return result

    def __floordiv__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[a // other for a in self])
        else:
            result = Vector(*[a // b for a, b in zip(self, other)])

        return result

    def __pow__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[a**other for a in self])
        else:
            result = Vector(*[a**b for a, b in zip(self, other)])

        return result

    def __mod__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[a % other for a in self])
        else:
            result = Vector(*[a % b for a, b in zip(self, other)])

        return result

    def __divmod__(self, other: float | int | Vector) -> list:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result_1 = Vector(*[divmod(a, other)[0] for a in self])
            result_2 = Vector(*[divmod(a, other)[1] for a in self])
        else:
            result_1 = Vector(*[divmod(a, b)[0] for a, b in zip(self, other)])
            result_2 = Vector(*[divmod(a, b)[1] for a, b in zip(self, other)])

        return result_1, result_2

    # reflected arithmetic operations ------------------------------------------------ #
    def __radd__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[other + a for a in self])
        else:
            result = Vector(*[b + a for a, b in zip(self, other)])

        return result

    def __rsub__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[other - a for a in self])
        else:
            result = Vector(*[b - a for a, b in zip(self, other)])

        return result

    def __rmul__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[other * a for a in self])
        else:
            result = Vector(*[b * a for a, b in zip(self, other)])

        return result

    def __rtruediv__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[other / a for a in self])
        else:
            result = Vector(*[b / a for a, b in zip(self, other)])

        return result

    def __rfloordiv__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[other // a for a in self])
        else:
            result = Vector(*[b // a for a, b in zip(self, other)])

        return result

    def __rpow__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[other**a for a in self])
        else:
            result = Vector(*[b**a for a, b in zip(self, other)])

        return result

    def __rmod__(self, other: float | int | Vector) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result = Vector(*[other % a for a in self])
        else:
            result = Vector(*[b % a for a, b in zip(self, other)])

        return result

    def __rdivmod__(self, other: float | int | Vector) -> list:
        if type(other) not in (float, int, Vector):
            raise TypeError(
                f"'other' must be of type 'float', 'int', or 'Vector', not {type(other)}"
            )

        if type(other) != Vector:
            result_1 = Vector(*[divmod(other, a)[0] for a in self])
            result_2 = Vector(*[divmod(other, a)[1] for a in self])
        else:
            result_1 = Vector(*[divmod(b, a)[0] for a, b in zip(self, other)])
            result_2 = Vector(*[divmod(b, a)[1] for a, b in zip(self, other)])

        return result_1, result_2

    # type conversion operations ----------------------------------------------------- #
    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    # representation operations ------------------------------------------------------ #
    def __repr__(self) -> str:
        return self.__str__()

    # custom sequence operations ----------------------------------------------------- #
    def __iter__(self) -> iter:
        return (self.x, self.y).__iter__()

    # properties --------------------------------------------------------------------- #
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float | int) -> None:
        if type(x) not in (float, int):
            raise TypeError(f"'x' must be of type 'float' or 'int', not {type(x)}")

        if type(x) == int:
            x = float(x)

        if x == -0.0:
            x = 0.0

        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float | int) -> None:
        if type(y) not in (float, int):
            raise TypeError(f"'y' must be of type 'float' or 'int', not {type(y)}")

        if type(y) == int:
            y = float(y)

        if y == -0.0:
            y = 0.0

        self.__y = y

    # static methods ----------------------------------------------------------------- #
    @staticmethod
    def one() -> Vector:
        """
        Returns a `Vector` with the value `(1, 1)`

        Returns:
            result (Vector): `Vector` with the value `(1, 1)`
        """

        return Vector(1, 1)

    @staticmethod
    def unit() -> Vector:
        """
        Returns a `Vector` with the value `(1, 0)`

        Returns:
            result (Vector): `Vector` with the value `(1, 0)`
        """

        return Vector(1, 0)

    @staticmethod
    def zero() -> Vector:
        """
        Returns a `Vector` with the value `(0, 0)`

        Returns:
            result (Vector): `Vector` with the value `(0, 0)`
        """

        return Vector(0, 0)

    # methods ------------------------------------------------------------------------ #
    def angle(self) -> float:
        """
        Returns the angle of the vector from `Vector(0, 0)` in degrees.

        Returns:
            result (float): The angle of the vector

        Example:
            >>> Vector(1, 1).angle()
            45.0
        """

        return math.degrees(math.atan2(self.y, self.x))

    def angle_btwn(self, other: Vector) -> float:
        """
        Returns the angle between two vectors in degrees.

        Args:
            other (Vector): The other vector

        Returns:
            result (float): The angle between the two vectors

        Example:
            >>> Vector(1, 0).angle_btwn(Vector(0, 1))
            -90.0
        """

        if type(other) != Vector:
            raise TypeError(f"'other' must be of type 'Vector', not {type(other)}")

        return self.angle() - other.angle()

    def basis(self, x: Vector, y: Vector) -> Vector:
        """
        Returns the vector in the basis of two vectors.

        Args:
            x (Vector): The x vector
            y (Vector): The y vector

        Returns:
            result (Vector): The basis vector

        Example:
            >>> Vector(1, 0).basis(Vector(1, 1), Vector(0, 1))
            Vector(0.5, 0.0)

        Todo:
            * Research and update docstring
        """

        if type(x) != Vector:
            raise TypeError(f"'x' must be of type 'Vector', not {type(x)}")

        if type(y) != Vector:
            raise TypeError(f"'y' must be of type 'Vector', not {type(y)}")

        return Vector(self.dot(x) / x.length_sqrd(), self.dot(y) / y.length_sqrd())

    def cross(self, other: Vector) -> float:
        """
        Returns the cross product of two vectors.

        Args:
            other (Vector): The other vector

        Returns:
            result (float, int): The cross product of the vectors

        Example:
            >>> Vector(1, 0).cross(Vector(0, 1))
            1.0
        """

        if type(other) != Vector:
            raise TypeError(f"'other' must be of type 'Vector', not {type(other)}")

        return self.x * other.y - self.y * other.x

    def dist(self, other: Vector) -> float:
        """
        Returns the distance between two vectors.

        Args:
            other (Vector): The other vector

        Returns:
            result (float): The distance between the vectors

        Example:
            >>> Vector(0, 0).dist(Vector(2, 0))
            2.0
        """

        return math.sqrt(self.dist_sqrd(other))

    def dist_sqrd(self, other) -> float:
        """
        Returns the squared distance between two vectors.

        Args:
            other (Vector): The other vector

        Returns:
            result (float): The squared distance between the vectors

        Example:
            >>> Vector(0, 0).dist(Vector(2, 0))
            4.0
        """

        if type(other) != Vector:
            raise TypeError(f"'other' must be of type 'Vector', not {type(other)}")

        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def dot(self, other: Vector) -> float:
        """
        Returns the dot product of two vectors.

        Args:
            other (Vector): The other vector

        Returns:
            result (float): The dot product of the vectors

        Example:
            >>> Vector(1, 0).dot(Vector(0, 1))
            0.0
        """

        if type(other) != Vector:
            raise TypeError(f"'other' must be of type 'Vector', not {type(other)}")

        return self.x * other.x + self.y * other.y

    def lerp(self, other: Vector, i_range: float | int) -> Vector:
        """
        Returns the linear interpolation between two vectors.

        Args:
            other (Vector): The other vector

        Returns:
            result (Vector): The linear interpolation between the vectors

        Example:
            >>> Vector(0, 0).lerp(Vector(2, 0), 0.5)
            Vector(1.0, 0.0)
        """

        if type(other) != Vector:
            raise TypeError(f"'other' must be of type 'Vector', not {type(other)}")

        if type(i_range) not in (float, int):
            raise TypeError(
                f"'i_range' must be of type 'float' or 'int', not {type(i_range)}"
            )

        return Vector(
            self.x + (other.x - self.x) * i_range, self.y + (other.y - self.y) * i_range
        )

    def length(self) -> float:
        """
        Returns the length (magnitude) of the vector.

        Returns:
            result (float): The length (magnitude) of the vector

        Example:
            >>> Vector(2, 0).length()
            2.0
        """

        return math.sqrt(self.length_sqrd())

    def length_sqrd(self) -> float:
        """
        Returns the squared length (magnitude) of the vector.

        Returns:
            result (float): The squared length (magnitude) of the vector

        Example:
            >>> Vector(2, 0).length_sqrd()
            4.0
        """

        return self.x**2 + self.y**2

    def normalise(self) -> float:
        """
        Returns the normalised vector.

        Returns:
            result (Vector): The normalised vector

        Example:
            >>> Vector(5, 0).normalise()
            Vector(1.0, 0.0)
        """

        return self.scale(1)

    def perp(self) -> Vector:
        """
        Return the perpendicular vector.

        Returns:
            result (Vector): The perpendicular vector

        Example:
            >>> Vector(0, 1).perp()
            Vector(-1.0, 0.0)
        """

        return Vector(-self.y if self.y != 0.0 else 0.0, self.x)

    def project(self, other: Vector) -> Vector:
        """
        Returns the projection of the vector onto another vector.

        Args:
            other (Vector): The other vector

        Returns:
            result (Vector): The projected vector

        Example:
            >>> Vector(1, 1).project(Vector(2, 0))
            Vector(1.0, 0.0)
        """

        if type(other) != Vector:
            raise TypeError(f"'other' must be of type 'Vector', not {type(other)}")

        return (self.dot(other) / other.length_sqrd()) * other

    def rotate(self, angle: float | int, point: Vector = None) -> Vector:
        """
        Returns the vector rotated vector around `point` or `Vector(0, 0)`.

        Args:
            angle (float, int): The angle to rotate the vector by in degrees
            point (Vector): optional; The point to rotate the vector around

        Returns:
            result (Vector): The rotated vector

        Example:
            >>> Vector(0, 1).rotate(-90)
            Vector(1.0, 0.0)
            >>> Vector(2, 2).rotate(-90, Vector(2, 1))
            Vector(3, 2)
        """

        if type(angle) not in (float, int):
            raise TypeError(
                f"'angle' must be of type 'float' or 'int', not {type(angle)}"
            )

        if point != None:
            if type(point) != Vector:
                raise TypeError(f"'point' must be of type 'Vector', not {type(point)}")
        else:
            point = Vector.zero()

        angle = math.radians(angle)

        cos = math.cos(angle)
        sin = math.sin(angle)

        return Vector(
            round(((self.x - point.x) * cos - (self.y - point.y) * sin) + point.x, 10),
            round(((self.x - point.x) * sin + (self.y - point.y) * cos) + point.y, 10),
        )

    def scale(self, length: float | int) -> Vector:
        """
        Returns the vector scaled to a certain `length`.

        Args:
            length (float | int): The length to scale the vector to

        Returns:
            result (Vector): The scaled vector

        Example:
            >>> Vector(1, 0).scale(5)
            Vector(5.0, 0.0)
        """

        if type(length) not in (float, int):
            raise TypeError(
                f"'length' must be of type 'float' or 'int', not {type(length)}"
            )

        if type(length) != float:
            length = float(length)

        return Vector(self.x * length / self.length(), self.y * length / self.length())

    def snap(self, value: int) -> Vector:
        """
        Returns the vector with `x` and `y` snapped to the nearest multiple of
        `value`.

        Args:
            value (int): The value to snap the vector to

        Returns:
            result (Vector): The snapped vector

        Example:
            >>> Vector(7, 1).snap(10)
            Vector(10, 0)
        """

        if type(value) != int:
            raise TypeError(f"'value' must be of type 'int', not {type(value)}")

        return Vector(
            math.floor(self.x * 10**value + 0.5) / 10**value,
            math.floor(self.y * 10**value + 0.5) / 10**value,
        )
