# future imports --------------------------------------------------------------------- #
from __future__ import annotations

# system imports --------------------------------------------------------------------- #
import math

# third-pary imports ----------------------------------------------------------------- #
import pygame

# local imports ---------------------------------------------------------------------- #
from ..vector import Vector

# line class ------------------------------------------------------------------------- #
class Line:
    # initialisation ----------------------------------------------------------------- #
    def __init__(
        self,
        start: Vector,
        end: Vector,
        width: int = 1,
        colour: list = [255, 255, 255, 255],
    ) -> None:
        self.start = start
        self.end = end
        self.width = width
        self.colour = colour

    # properties --------------------------------------------------------------------- #
    @property
    def colour(self) -> list:
        return self.__colour

    @colour.setter
    def colour(self, colour: list) -> None:
        if type(colour) not in [list, tuple]:
            raise TypeError("'colour' must be of type 'list' or 'tuple'")

        if len(colour) > 4 or len(colour) < 3:
            raise Exception("'colour' must have 3 or 4 items")

        if len(colour) == 3:
            colour.append(255)

        self.__colour = colour

    @property
    def start(self) -> Vector:
        return self.__start

    @start.setter
    def start(self, start: Vector) -> None:
        if type(start) != Vector:
            raise TypeError(f"'start' must be of type 'Vector', not {type(start)}")

        self.__start = start

    @property
    def end(self) -> Vector:
        return self.__end

    @end.setter
    def end(self, end: Vector) -> None:
        if type(end) != Vector:
            raise TypeError(f"'end' must be of type 'Vector', not {type(end)}")

        self.__end = end

    @property
    def width(self) -> int:
        return self.__width

    @width.setter
    def width(self, width: int):
        if type(width) != int:
            raise TypeError(f"'width' must be of type 'int', not {type(width)}")

        self.__width = width

    # public methods ----------------------------------------------------------------- #
    def angle(self) -> float:
        return round(
            math.degrees(
                math.atan2(self.end.y - self.start.y, self.end.x - self.start.x)
            ),
            Vector.ACCURACY,
        )

    def draw(
        self,
        surface,
        offset: Vector = None,
    ) -> None:
        if type(surface) != type(pygame.Surface((0, 0))):
            raise TypeError("'surface' must be of type 'pygame.Surface'")

        if offset != None:
            if type(offset) != Vector:
                raise TypeError("'offset' must be of type 'Vector'")
        else:
            offset = Vector.zero()

        pygame.draw.line(
            surface,
            self.__colour,
            [*self.__start + offset],
            [*self.__end + offset],
            self.__width,
        )

    def gradient(self) -> float:
        return round(
            (self.end.y - self.start.y) / (self.end.x - self.start.x), Vector.ACCURACY
        )

    def intersect(self, other: Line) -> bool:
        if type(other) not in (Line, Vector):
            raise TypeError("'other' must be of type 'Line'")

        def orientation(a, b, c):
            val = (float(b.y - a.y) * (c.x - b.x)) - (float(b.x - a.x) * (c.y - b.y))

            if val > 0:
                return 1
            elif val < 0:
                return -1
            else:
                return 0

        def on_segment(a, b, c):
            if (
                (b.x <= max(a.x, c.x))
                and (b.x >= min(a.x, c.x))
                and (b.y <= max(a.y, c.y))
                and (b.y >= min(a.y, c.y))
            ):
                return True
            else:
                return False

        orientation_1 = orientation(self.start, self.end, other.start)
        orientation_2 = orientation(self.start, self.end, other.end)
        orientation_3 = orientation(other.start, other.end, self.start)
        orientation_4 = orientation(other.start, other.end, self.end)

        if orientation_1 != orientation_2 and orientation_3 != orientation_4:
            return True
        elif orientation_1 == 0 and on_segment(self.start, other.start, self.end):
            return True
        elif orientation_2 == 0 and on_segment(self.start, other.end, self.end):
            return True
        elif orientation_3 == 0 and on_segment(other.start, self.start, other.end):
            return True
        elif orientation_4 == 0 and on_segment(other.start, self.end, other.end):
            return True
        else:
            return False

    def intersect_point(self, other: Line) -> Vector:
        if type(other) not in (Line, Vector):
            raise TypeError("'other' must be of type 'Line'")

        if not self.intersect(other):
            return False

        value = (
            (self.start.x - other.start.x) * (other.start.y - other.end.y)
            - (self.start.y - other.start.y) * (other.start.x - other.end.x)
        ) / (
            (self.start.x - self.end.x) * (other.start.y - other.end.y)
            - (self.start.y - self.end.y) * (other.start.x - other.end.x)
        )

        return Vector(
            self.start.x + value * (self.end.x - self.start.x),
            self.start.y + value * (self.end.y - self.start.y),
        )

    def length(self) -> float:
        return round(
            math.sqrt(abs((self.end.x - self.start.x) + (self.end.y - self.start.y))),
            Vector.ACCURACY,
        )

    def length_sqrd(self) -> float:
        return round(
            (self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2,
            Vector.ACCURACY,
        )

    def middle(self) -> Vector:
        return (self.start + self.end) / 2

    def mirror(self, point: Vector) -> Vector:
        if type(point) != Vector:
            raise TypeError("'point' must be of type 'Vector'")

        return self.start + (point - self.start).rotate(
            (self.angle() - (point - self.start).angle()) * 2
        )

    def normal(self, point: Vector = None) -> Line:
        if type(point) != Vector:
            raise TypeError("'point' must be of type 'Vector'")

        if not self.on_line(point):
            raise Exception("'point' must be on line")

        return Line(point, point + Vector(10, 0).rotate(self.angle() - 90))

    def normal_to(self, point: Vector = None) -> Line:
        if type(point) != Vector:
            raise TypeError("'point' must be of type 'Vector'")

        return Line(self.start + (point - self.start).project(self.vector()), point)

    def on_line(self, point: Vector) -> bool:
        if type(point) != Vector:
            raise TypeError("'point' must be of type 'Vector'")

        sort = self.sort_x()

        if sort.start.x <= point.x and sort.end.x >= point.x:
            if math.isclose(
                self.start.dist(point) + self.end.dist(point),
                self.length(),
                abs_tol=0.01,
            ):
                return True

        return False

    def reflect(self, point: Vector, reflect_point: Vector) -> Vector:
        if type(point) != Vector:
            raise TypeError("'point' must be of type 'Vector'")

        if type(reflect_point) != Vector:
            raise TypeError("'reflect_point' must be of type 'Vector'")

        if not self.on_line(reflect_point):
            raise Exception("'reflect_point' must be on line")

        return self.normal(reflect_point).mirror(point)

    def rotate(self, angle: float | int, point: Vector = None) -> Line:
        if type(angle) not in [float, int]:
            raise TypeError("'angle' must be of type 'float' or 'int'")

        if point != None:
            if type(point) != Vector:
                raise TypeError("'point' must be of type 'Vector'")
        else:
            point = self.middle()

        return Line(
            self.start.rotate(angle, point),
            self.end.rotate(angle, point),
            self.width,
        )

    def side(self, point: Vector) -> int:
        if type(point) != Vector:
            raise TypeError(f"'point' must be of type 'Vector', not {type(point)}")

        sort = self.sort_y()

        vec_1 = Vector(sort.end.x - sort.start.x, sort.end.y - sort.start.y)
        vec_2 = Vector(sort.end.x - point.x, sort.end.y - point.y)

        if sort.end.x > sort.start.x:
            if vec_1.x * vec_2.y - vec_1.y * vec_2.x > 0:
                return 1
            elif vec_1.x * vec_2.y - vec_1.y * vec_2.x < 0:
                return -1
            else:
                return 0
        elif sort.end.x < sort.start.x:
            if vec_1.x * vec_2.y - vec_1.y * vec_2.x < 0:
                return 1
            elif vec_1.x * vec_2.y - vec_1.y * vec_2.x > 0:
                return -1
            else:
                return 0
        else:
            return 0

    def sort_x(self) -> Line:
        if self.start.x > self.end.x:
            return Line(self.end, self.start)

        return self

    def sort_y(self) -> Line:
        if self.start.y > self.end.y:
            return Line(self.end, self.start)

        return self

    def vector(self) -> Vector:
        return self.end - self.start
