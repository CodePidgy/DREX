# future imports --------------------------------------------------------------------- #
from __future__ import annotations

# system imports --------------------------------------------------------------------- #
import copy
import math
import operator
from typing import Union

# vector class ----------------------------------------------------------------------- #
class Vector:
    # initialisation ----------------------------------------------------------------- #
    def __init__(self, x: Union[float, int], y: Union[float, int]) -> None:
        self.x = x
        self.y = y

    def __call__(self, x: Union[float, int], y: Union[float, int]) -> None:
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

    def __gt__(self, other) -> bool:
        raise NotImplementedError("'Vector' object does not support '>'")

    def __ge__(self, other) -> bool:
        raise NotImplementedError("'Vector' object does not support '>='")

    def __lt__(self, other) -> bool:
        raise NotImplementedError("'Vector' object does not support '<'")

    def __le__(self, other) -> bool:
        raise NotImplementedError("'Vector' object does not support '<='")

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

    def __pos__(self) -> Vector:
        return Vector(operator.pos(self.x), operator.pos(self.y))

    def __neg__(self) -> Vector:
        return Vector(operator.neg(self.x), operator.neg(self.y))

    def __invert__(self) -> Vector:
        return Vector(~self.x, ~self.y)

    # normal arithmetic operations --------------------------------------------------- #
    def __add__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a + other for a in self))
        else:
            result = Vector(*(a + b for a, b in zip(self, other)))

        return result

    def __sub__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a - other for a in self))
        else:
            result = Vector(*(a - b for a, b in zip(self, other)))

        return result

    def __mul__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a * other for a in self))
        else:
            result = Vector(*(a * b for a, b in zip(self, other)))

        return result

    def __truediv__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a / other for a in self))
        else:
            result = Vector(*(a / b for a, b in zip(self, other)))

        return result

    def __floordiv__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a // other for a in self))
        else:
            result = Vector(*(a // b for a, b in zip(self, other)))

        return result

    def __pow__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a ** other for a in self))
        else:
            result = Vector(*(a ** b for a, b in zip(self, other)))

        return result

    def __mod__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a % other for a in self))
        else:
            result = Vector(*(a % b for a, b in zip(self, other)))

        return result

    def __divmod__(self, other: Union[float, int, Vector]) -> list:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result_1 = Vector(*(divmod(a, other)[0] for a in self))
            result_2 = Vector(*(divmod(a, other)[1] for a in self))
        else:
            result_1 = Vector(*(divmod(a, b)[0] for a, b in zip(self, other)))
            result_2 = Vector(*(divmod(a, b)[1] for a, b in zip(self, other)))

        return result_1, result_2

    def __and__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a & other for a in self))
        else:
            result = Vector(*(a & b for a, b in zip(self, other)))

        return result

    def __or__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a | other for a in self))
        else:
            result = Vector(*(a | b for a, b in zip(self, other)))

        return result

    def __xor__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a ^ other for a in self))
        else:
            result = Vector(*(a ^ b for a, b in zip(self, other)))

        return result

    def __lshift__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a << other for a in self))
        else:
            result = Vector(*(a << b for a, b in zip(self, other)))

        return result

    def __rshift__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(a >> other for a in self))
        else:
            result = Vector(*(a >> b for a, b in zip(self, other)))

        return result

    # reflected arithmetic operations ------------------------------------------------ #
    def __radd__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other + a for a in self))
        else:
            result = Vector(*(b + a for a, b in zip(self, other)))

        return result

    def __rsub__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other - a for a in self))
        else:
            result = Vector(*(b - a for a, b in zip(self, other)))

        return result

    def __rmul__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other * a for a in self))
        else:
            result = Vector(*(b * a for a, b in zip(self, other)))

        return result

    def __rtruediv__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other / a for a in self))
        else:
            result = Vector(*(b / a for a, b in zip(self, other)))

        return result

    def __rfloordiv__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other // a for a in self))
        else:
            result = Vector(*(b // a for a, b in zip(self, other)))

        return result

    def __rpow__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other ** a for a in self))
        else:
            result = Vector(*(b ** a for a, b in zip(self, other)))

        return result

    def __rmod__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other % a for a in self))
        else:
            result = Vector(*(b % a for a, b in zip(self, other)))

        return result

    def __rdivmod__(self, other: Union[float, int, Vector]) -> list:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result_1 = Vector(*(divmod(other, a)[0] for a in self))
            result_2 = Vector(*(divmod(other, a)[1] for a in self))
        else:
            result_1 = Vector(*(divmod(b, a)[0] for a, b in zip(self, other)))
            result_2 = Vector(*(divmod(b, a)[1] for a, b in zip(self, other)))

        return result_1, result_2

    def __rand__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other & a for a in self))
        else:
            result = Vector(*(b & a for a, b in zip(self, other)))

        return result

    def __ror__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other | a for a in self))
        else:
            result = Vector(*(b | a for a, b in zip(self, other)))

        return result

    def __rxor__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other ^ a for a in self))
        else:
            result = Vector(*(b ^ a for a, b in zip(self, other)))

        return result

    def __rlshift__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other << a for a in self))
        else:
            result = Vector(*(b << a for a, b in zip(self, other)))

        return result

    def __rrshift__(self, other: Union[float, int, Vector]) -> Vector:
        if type(other) not in (float, int, Vector):
            raise TypeError("'other' must be of type 'float', 'int', or 'Vector'")

        if type(other) != Vector:
            result = Vector(*(other >> a for a in self))
        else:
            result = Vector(*(b >> a for a, b in zip(self, other)))

        return result

    # augmented assignment operations ------------------------------------------------ #
    def __iadd__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__add__(other)

    def __isub__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__sub__(other)

    def __imul__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__mul__(other)

    def __itruediv__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__truediv__(other)

    def __ifloordiv__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__floordiv__(other)

    def __ipow__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__pow__(other)

    def __imod__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__mod__(other)

    def __iand__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__and__(other)

    def __ior__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__or__(other)

    def __ixor__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__xor__(other)

    def __ilshift__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__lshift__(other)

    def __irshift__(self, other: Union[float, int, Vector]) -> Vector:
        return self.__rshift__(other)

    # type conversion operations ----------------------------------------------------- #
    def __bool__(self) -> bool:
        raise NotImplementedError("'Vector' object does not support 'bool()'")

    def __float__(self) -> Vector:
        return Vector(float(self.x), float(self.y))

    def __int__(self) -> Vector:
        return Vector(int(self.x), int(self.y))

    def __str__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    # representation operations ------------------------------------------------------ #
    def __repr__(self) -> str:
        return self.__str__()

    # custom sequence operations ----------------------------------------------------- #
    def __iter__(self) -> iter:
        return (self.x, self.y).__iter__()

    # copying operations ------------------------------------------------------------- #
    def __copy__(self) -> Vector:
        return Vector(copy.copy(self.x), copy.copy(self.y))

    def __deepcopy__(self, memo: dict = None) -> Vector:
        if memo != None:
            if type(memo) != dict:
                raise TypeError("'memo' must be of type 'dict'")
        else:
            memo = {}

        return Vector(copy.deepcopy(self.x, memo), copy.deepcopy(self.y, memo))

    # properties --------------------------------------------------------------------- #
    @property
    def x(self) -> Union[float, int]:
        return self.__x

    @x.setter
    def x(self, x: Union[float, int]) -> None:
        if type(x) not in (float, int):
            raise TypeError("'x' must be of type 'float' or 'int'")

        self.__x = x

    @property
    def y(self) -> Union[float, int]:
        return self.__y

    @y.setter
    def y(self, y: Union[float, int]) -> None:
        if type(y) not in (float, int):
            raise TypeError("'y' must be of type 'float' or 'int'")

        self.__y = y

    # static methods ----------------------------------------------------------------- #
    @staticmethod
    def one() -> Vector:
        return Vector(1, 1)

    @staticmethod
    def unit() -> Vector:
        return Vector(1, 0)

    @staticmethod
    def zero() -> Vector:
        return Vector(0, 0)

    # methods ------------------------------------------------------------------------ #
    def angle(self) -> float:
        return math.degrees(math.atan2(self.y, self.x))

    def angle_btwn(self, other: Vector) -> float:
        if type(other) != Vector:
            raise TypeError("'other' must be of type 'Vector'")

        return self.angle() - other.angle()

    def basis(self, x: Vector, y: Vector) -> Vector:
        if type(x) != Vector:
            raise TypeError("'x' must be of type 'Vector'")

        if type(y) != Vector:
            raise TypeError("'y' must be of type 'Vector'")

        return Vector(self.dot(x) / x.length_sqrd(), self.dot(y) / y.length_sqrd())

    def cross(self, other: Vector) -> float:
        if type(other) != Vector:
            raise TypeError("'other' must be of type 'Vector'")

        return self.x * other.y - self.y * other.x

    def dist(self, other: Vector) -> float:
        return math.sqrt(self.dist_sqrd(other))

    def dist_sqrd(self, other) -> float:
        if type(other) != Vector:
            raise TypeError("'other' must be of type 'Vector'")

        return (self.x - other.x) ** 2 + (self.y - other.y) ** 2

    def dot(self, other: Vector) -> float:
        if type(other) != Vector:
            raise TypeError("'other' must be of type 'Vector'")

        return self.x * other.x + self.y * other.y

    def lerp(self, other: Vector, i_range: Union[float, int]) -> Vector:
        if type(other) != Vector:
            raise TypeError("'other' must be of type 'Vector'")

        if type(i_range) not in (float, int):
            raise TypeError("'i_range' must be of type 'float' or 'int'")

        return Vector(
            self.x + (other.x - self.x) * i_range, self.y + (other.y - self.y) * i_range
        )

    def length(self) -> float:
        return math.sqrt(self.length_sqrd())

    def length_sqrd(self) -> float:
        return self.x ** 2 + self.y ** 2

    def normalise(self) -> float:
        return self.scale(1)

    def perp(self) -> Vector:
        return Vector(-self.y, self.x)

    def project(self, other: Vector) -> Vector:
        if type(other) != Vector:
            raise TypeError("'other' must be of type 'Vector'")

        return (self.dot(other) / other.length_sqrd()) * other

    def rotate(self, angle: Union[float, int], point: Vector = None) -> Vector:
        if type(angle) not in (float, int):
            raise TypeError("'angle' must be of type 'float' or 'int'")

        if point != None:
            if type(point) != Vector:
                raise TypeError("'point' must be of type 'Vector'")
        else:
            point = Vector.zero()

        angle = math.radians(angle)

        cos = math.cos(angle)
        sin = math.sin(angle)

        return Vector(
            ((self.x - point.x) * cos - (self.y - point.y) * sin) + point.x,
            ((self.x - point.x) * sin + (self.y - point.y) * cos) + point.y,
        )

    def scale(self, length: Union[float, int]) -> Vector:
        if type(length) not in (float, int):
            raise TypeError("'length' must be of type 'float' or 'int'")

        if type(length) != float:
            length = float(length)

        return Vector(self.x * length / self.length(), self.y * length / self.length())

    def snap(self, d: int) -> Vector:
        if type(d) != int:
            raise TypeError("'d' must be of type 'int'")

        return Vector(
            math.floor(self.x * 10 ** d + 0.5) / 10 ** d,
            math.floor(self.y * 10 ** d + 0.5) / 10 ** d,
        )
