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
        colour: list = [255, 255, 255, 255],
        width: int = 1,
    ) -> None:
        self.start = start
        self.end = end
        self.colour = colour
        self.width = width

    # properties --------------------------------------------------------------------- #
    @property
    def colour(self) -> list:
        return self.__colour

    @colour.setter
    def colour(self, colour: list | tuple) -> None:
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
        """
        Returns the angle of the `Line`

        Returns:
            result (`float`): The angle of the `Line`

        Example:
            >>> Line(Vector.zero(), Vector(1, 1)).angle()
            45.0
        """
        return round(
            math.degrees(
                math.atan2(self.end.y - self.start.y, self.end.x - self.start.x)
            ),
            Vector.ACCURACY,
        )

    def draw(
        self,
        surface,
        colour: list = None,
        offset: Vector = None,
    ) -> None:
        """
        Draws the `Line` to the given surface with an optional offset

        Args:
            surface (`pygame.Surface`): The surface to draw the `Line` to
            offset (`Vector`, optional): The offset to draw the `Line` with
        """
        if type(surface) != type(pygame.Surface([0, 0])):
            raise TypeError("'surface' must be of type 'pygame.Surface'")

        if colour is not None:
            if type(colour) not in [list, tuple]:
                raise TypeError("'colour' must be of type 'list' or 'tuple'")
            if len(colour) > 4 or len(colour) < 3:
                raise Exception("'colour' must have 3 or 4 items")
        else:
            colour = self.__colour

        if offset != None:
            if type(offset) != Vector:
                raise TypeError("'offset' must be of type 'Vector'")
        else:
            offset = Vector.zero()

        pygame.draw.line(
            surface,
            colour,
            [*self.__start + offset],
            [*self.__end + offset],
            self.__width,
        )

    def gradient(self) -> float:
        """
        Returns the gradient of the `Line`

        Returns:
            result (`float`): The gradient of the `Line`

        Example:
            >>> Line(Vector.zero(), Vector(1, 1)).gradient()
            1.0
        """
        return round(
            (self.end.y - self.start.y) / (self.end.x - self.start.x), Vector.ACCURACY
        )

    def intersect(self, other: Line) -> bool:
        """
        Returns whether or not the `Line` intersects with another `Line`

        Args:
            other (`Line`): The other `Line` to check for intersection

        Returns:
            result (`bool`): Whether or not the `Line`s intersect

        Example:
            >>> Line(Vector.zero(), Vector(1, 1)).intersect(
                    Line(Vector(0, 1),Vector(1, 0))
                )
            True
        """

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
        """
        Returns the point of intersection between the `Line` and another `Line`

        Args:
            other (`Line`): The other `Line` to check for the point of intersection

        Returns:
            result (`Vector`): The point of intersection between the `Line`s

        Example:
            >>> Line(Vector.zero(), Vector(1, 1)).intersect_point(
                    Line(Vector(0, 1),Vector(1, 0))
                )
            Vector(0.5, 0.5)
        """

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
        """
        Returns the length of the `Line`

        Returns:
            result (`float`): The length of the `Line`

        Example:
            >>> Line(Vector.zero(), Vector(2, 0)).length()
            2.0
        """

        return round(
            math.sqrt(
                abs((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2)
            ),
            Vector.ACCURACY,
        )

    def length_sqrd(self) -> float:
        """
        Returns the squared length of the `Line`

        Returns:
            result (`float`): The squared length of the `Line`

        Example:
            >>> Line(Vector.zero(), Vector(2, 0)).length_sqrd()
            4.0
        """

        return round(
            (self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2,
            Vector.ACCURACY,
        )

    def middle(self) -> Vector:
        """
        Returns the middle point of the `Line`

        Returns:
            result (`Vector): The middle point of the `Line`

        Example:
            >>> Line(Vector.zero(), Vector(2, 0)).middle()
            Vector(1.0, 0.0)
        """

        return (self.start + self.end) / 2

    def mirror(self, point: Vector) -> Vector:
        """
        Returns the point mirrored across the `Line`

        Args:
            point (`Vector`): The point to mirror

        Returns:
            result (`Vector`): The mirrored point

        Example:
            >>> Line(Vector.zero(), Vector(1, 1)).mirror(Vector(0, 1))
            Vector(1.0, 0.0)
        """

        if type(point) != Vector:
            raise TypeError("'point' must be of type 'Vector'")

        return self.start + (point - self.start).rotate(
            (self.angle() - (point - self.start).angle()) * 2
        )

    def normal(self, point: Vector = None, length: float | int = 1) -> Line:
        """
        Returns the normal `Line` of the `Line`

        Args:
            point (`Vector`): The point on the `Line` that will be the start of the
            normal `Line`
            length (`float`): The length of the normal `Line`

        Returns:
            result (`Line`): The normal `Line` of the `Line`

        Example:
            >>> Line(Vector.zero(), Vector(0, 1)).normal()
            Line(Vector(0.0, 0.5), Vector(1.0, 0.5))
        """

        if point != None:
            if type(point) != Vector:
                raise TypeError("'point' must be of type 'Vector'")
        else:
            point = self.middle()

        if not self.on_line(point):
            raise ValueError("'point' must be on line")

        if type(length) not in (float, int):
            raise TypeError("'length' must be of type 'float' or 'int'")

        return Line(point, point + Vector(length, 0).rotate(self.angle() - 90))

    def normal_to(self, point: Vector = None) -> Line:
        """
        Returns the normal `Line` of the `Line` that starts along the `Line` and end at
        `point`

        Args:
            point (`Vector`): The point that the normal `Line` will end at

        Returns:
            result (`Line`): The normal `Line` of the `Line` to `point`

        Example:
            >>> Line(Vector.zero(), Vector(2, 2)).normal_to(Vector(1, 0))
            Line(Vector(0.5, 0.5), Vector(1.0, 0.0))
        """

        if type(point) != Vector:
            raise TypeError("'point' must be of type 'Vector'")

        return Line(self.start + (point - self.start).project(self.vector()), point)

    def on_line(self, point: Vector) -> bool:
        """
        Returns whether or not a `Vector` is on the `Line`

        Args:
            point (`Vector`): The `Vector` to check

        Returns:
            result (`bool`): Whether or not the `Vector` is on the `Line`

        Example:
            >>> Line(Vector.zero(), Vector(1, 1)).on_line(Vector(0.5, 0.5))
            True
        """

        if type(point) != Vector:
            raise TypeError("'point' must be of type 'Vector'")

        sort = self.sort_x()

        if sort.start.x <= point.x and sort.end.x >= point.x:
            if math.isclose(
                self.start.dist(point) + self.end.dist(point),
                self.length(),
                abs_tol=Vector.ACCURACY,
            ):
                return True

        return False

    def reflect(self, point: Vector, reflect_point: Vector) -> Vector:
        """
        Returns the `point` reflected off of the `Line` at `reflect_point`

        Args:
            point (`Vector`): The point to reflect
            reflect_point (`Vector`): The point to reflect off of

        Returns:
            result (`Vector`): The reflected point

        Example:
            >>> Line(Vector.zero(), Vector(2, 2)).reflect(Vector(1, 0), Vector(1, 1))
            Vector(2.0, 1.0)
        """

        if type(point) != Vector:
            raise TypeError("'point' must be of type 'Vector'")

        if type(reflect_point) != Vector:
            raise TypeError("'reflect_point' must be of type 'Vector'")

        if not self.on_line(reflect_point):
            raise Exception("'reflect_point' must be on Line")

        return self.normal(reflect_point).mirror(point)

    def rotate(self, angle: float | int, point: Vector = None) -> Line:
        """
        Returns the `Line` rotated by `angle` around `point`

        Args:
            angle (`float`): The angle to rotate the `Line` by
            point (`Vector`, optional): The point to rotate the `Line` around

        Returns:
            result (`Line`): The rotated `Line`

        Example:
            >>> Line(Vector.zero(), Vector(1, 0)).rotate(90)
            Line(Vector(0.5, -0.5), Vector(0.5, 0.5))
            >>> Line(Vector.zero(), Vector(1, 0)).rotate(90, Vector.zero())
            Line(Vector(0.0, 0.0), Vector(0.0, 1.0))
        """

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
            self.colour,
            self.width,
        )

    def side(self, point: Vector) -> int:
        """
        Returns an int based on what side of the `Line` a `point` is on; 1 for above,
        0 for on, -1 for below

        Args:
            point (`Vector`): The point to check

        Returns:
            result (`int`): The side of the `Line` the `point` is on

        Example:
            >>> Line(Vector(0, 1), Vector(2, 1)).side(Vector(1, 0))
            1
            >>> Line(Vector(0, 1), Vector(2, 1)).side(Vector(1, 1))
            0
            >>> Line(Vector(0, 1), Vector(2, 1)).side(Vector(1, 2))
            -1
        """

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
        """
        Returns the `Line` with its start and end `Vector` sorted by x ascending

        Returns:
            result (`Line`): The sorted `Line`

        Example:
            >>> Line(Vector(2, 1), Vector(1, 1)).sort_x()
            Line(Vector(1.0, 1.0), Vector(2.0, 1.0))
        """

        if self.start.x > self.end.x:
            return Line(self.end, self.start)

        return self

    def sort_y(self) -> Line:
        """
        Returns the `Line` with its start and end `Vector` sorted by y ascending

        Returns:
            result (`Line`): The sorted `Line`

        Example:
            >>> Line(Vector(1, 2), Vector(1, 1)).sort_y()
            Line(Vector(1.0, 1.0), Vector(1.0, 2.0))
        """

        if self.start.y > self.end.y:
            return Line(self.end, self.start)

        return self

    def vector(self) -> Vector:
        """
        Returns the `Line` as a `Vector`

        Returns:
            result (`Vector`): The `Line` as a `Vector`

        Example:
            >>> Line(Vector.zero(), Vector(1, 1)).vector()
            Vector(1.0, 1.0)
            >>> Line(Vector(1, 0), Vector(2, 0)).vector()
            Vector(1.0, 0.0)
        """

        return self.end - self.start
