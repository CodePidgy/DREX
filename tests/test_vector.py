# system imports --------------------------------------------------------------------- #
import math
import random
import sys

sys.path.append(".")

# local imports ---------------------------------------------------------------------- #
from drex import Vector

runs = 1000
upper_range = 1000
lower_range = 10
angle_range = 359

# initialisation --------------------------------------------------------------------- #
def test_init():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x, y).x == x and Vector(x, y).y == y


def test_call():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        vector = Vector(x, y)
        vector(x + 1.0, y + 1.0)

        assert vector.x == round(x + 1.0, Vector.ACCURACY) and vector.y == round(
            y + 1.0, Vector.ACCURACY
        )


# comparison operations -------------------------------------------------------------- #
def test_eq():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x, y) == Vector(x, y)


def test_ne():
    for _ in range(runs):
        while True:
            x = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            y = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )

            if x != 0.0 and y != 0.0:
                break

        assert Vector(x, y) != Vector(-x, -y)
        assert Vector(x, y) != Vector(-x, y)
        assert Vector(x, y) != Vector(x, -y)


# unary operations ------------------------------------------------------------------- #
def test_abs():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert abs(Vector(-x, -y)) == Vector(abs(x), abs(y))
        assert abs(Vector(-x, y)) == Vector(abs(x), abs(y))
        assert abs(Vector(x, -y)) == Vector(abs(x), abs(y))


def test_round():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert round(Vector(x, y)) == Vector(round(x), round(y))
        assert round(Vector(round(x), y)) == Vector(round(x), round(y))
        assert round(Vector(x, round(y))) == Vector(round(x), round(y))


def test_ceil():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert math.ceil(Vector(x, y)) == Vector(math.ceil(x), math.ceil(y))
        assert math.ceil(Vector(math.ceil(x), y)) == Vector(math.ceil(x), math.ceil(y))
        assert math.ceil(Vector(x, math.ceil(y))) == Vector(math.ceil(x), math.ceil(y))


def test_floor():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert math.floor(Vector(x, y)) == Vector(math.floor(x), math.floor(y))
        assert math.floor(Vector(math.floor(x), y)) == Vector(
            math.floor(x), math.floor(y)
        )
        assert math.floor(Vector(x, math.floor(y))) == Vector(
            math.floor(x), math.floor(y)
        )


def test_trunc():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert math.trunc(Vector(x, y)) == Vector(math.trunc(x), math.trunc(y))
        assert math.trunc(Vector(math.trunc(x), y)) == Vector(
            math.trunc(x), math.trunc(y)
        )
        assert math.trunc(Vector(x, math.trunc(y))) == Vector(
            math.trunc(x), math.trunc(y)
        )


def test_neg():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert -Vector(x, y) == Vector(-x, -y)


# normal arithmetic operations ------------------------------------------------------- #
def test_add():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        number = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        vector = Vector(
            round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            ),
            round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            ),
        )

        assert Vector(x, y) + number == Vector(x + number, y + number)
        assert Vector(x, y) + vector == Vector(x + vector.x, y + vector.y)


def test_sub():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        number = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        vector = Vector(
            round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            ),
            round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            ),
        )

        assert Vector(x, y) - number == Vector(x - number, y - number)
        assert Vector(x, y) - vector == Vector(x - vector.x, y - vector.y)


def test_mul():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        number = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        vector = Vector(
            round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            ),
            round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            ),
        )

        assert Vector(x, y) * number == Vector(x * number, y * number)
        assert Vector(x, y) * vector == Vector(x * vector.x, y * vector.y)


def test_truediv():
    for _ in range(runs):
        while True:
            x = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            y = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            number = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            vector = Vector(
                round(
                    random.randint(-upper_range, upper_range) + random.random(),
                    Vector.ACCURACY,
                ),
                round(
                    random.randint(-upper_range, upper_range) + random.random(),
                    Vector.ACCURACY,
                ),
            )

            if x != 0.0 and y != 0.0 and number != 0.0:
                break

        assert Vector(x, y) / number == Vector(x / number, y / number)
        assert Vector(x, y) / vector == Vector(x / vector.x, y / vector.y)


def test_floordiv():
    for _ in range(runs):
        while True:
            x = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            y = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            number = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            vector = Vector(
                round(
                    random.randint(-upper_range, upper_range) + random.random(),
                    Vector.ACCURACY,
                ),
                round(
                    random.randint(-upper_range, upper_range) + random.random(),
                    Vector.ACCURACY,
                ),
            )

            if x != 0.0 and y != 0.0 and number != 0.0:
                break

        assert Vector(x, y) // number == Vector(x // number, y // number)
        assert Vector(x, y) // vector == Vector(x // vector.x, y // vector.y)


def test_pow():
    for _ in range(runs):
        while True:
            x = random.randint(-lower_range, lower_range)
            y = random.randint(-lower_range, lower_range)
            number = random.randint(-lower_range, lower_range)
            vector = Vector(
                random.randint(-lower_range, lower_range),
                random.randint(-lower_range, lower_range),
            )

            if x != 0.0 and y != 0.0 and number != 0.0:
                break

        assert Vector(x, y) ** number == Vector(x**number, y**number)
        assert Vector(x, y) ** vector == Vector(x**vector.x, y**vector.y)


def test_mod():
    for _ in range(runs):
        while True:
            x = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            y = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            number = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            vector = Vector(
                round(
                    random.randint(-upper_range, upper_range) + random.random(),
                    Vector.ACCURACY,
                ),
                round(
                    random.randint(-upper_range, upper_range) + random.random(),
                    Vector.ACCURACY,
                ),
            )

            if x != 0.0 and y != 0.0 and number != 0.0:
                break

        assert Vector(x, y) % number == Vector(x % number, y % number)
        assert Vector(x, y) % vector == Vector(x % vector.x, y % vector.y)


def test_divmod():
    for _ in range(runs):
        while True:
            x = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            y = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            number = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            vector = Vector(
                round(
                    random.randint(-upper_range, upper_range) + random.random(),
                    Vector.ACCURACY,
                ),
                round(
                    random.randint(-upper_range, upper_range) + random.random(),
                    Vector.ACCURACY,
                ),
            )

            if x != 0.0 and y != 0.0 and number != 0.0:
                break

        assert divmod(Vector(x, y), number) == (
            Vector(divmod(x, number)[0], divmod(y, number)[0]),
            Vector(divmod(x, number)[1], divmod(y, number)[1]),
        )
        assert divmod(Vector(x, y), vector) == (
            Vector(divmod(x, vector.x)[0], divmod(y, vector.y)[0]),
            Vector(divmod(x, vector.x)[1], divmod(y, vector.y)[1]),
        )


# type conversion operations --------------------------------------------------------- #
def test_str():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert str(Vector(x, y)) == f"Vector({x}, {y})"


# representation operations ---------------------------------------------------------- #
def test_repr():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert repr(Vector(x, y)) == f"Vector({x}, {y})"


# custom sequence operations --------------------------------------------------------- #
def test_iter():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert list(Vector(x, y)) == [x, y]


# properties ------------------------------------------------------------------------- #
def test_x():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x, 0.0).x == x


def test_y():
    for _ in range(runs):
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(0.0, y).y == y


# static methods --------------------------------------------------------------------- #
def test_one():
    for _ in range(runs):
        assert Vector.one() == Vector(1.0, 1.0)


def test_unit():
    for _ in range(runs):
        assert Vector.unit() == Vector(1.0, 0.0)


def test_zero():
    for _ in range(runs):
        assert Vector.zero() == Vector(0.0, 0.0)


# methods ---------------------------------------------------------------------------- #
def test_angle():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x, y).angle() == round(
            math.degrees(math.atan2(y, x)), Vector.ACCURACY
        )


def test_angle_btwn():
    for _ in range(runs):
        x_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        x_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x_1, y_1).angle_btwn(Vector(x_2, y_2)) == round(
            math.degrees(math.atan2(y_1, x_1) - math.atan2(y_2, x_2)), Vector.ACCURACY
        )


# TODO: add test for Vector.basis() once it is understood properly


def test_cross():
    for _ in range(runs):
        x_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        x_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x_1, y_1).cross(Vector(x_2, y_2)) == x_1 * y_2 - x_2 * y_1


def test_dist():
    for _ in range(runs):
        x_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        x_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x_1, y_1).dist(Vector(x_2, y_2)) == round(
            math.sqrt((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2), Vector.ACCURACY
        )


def test_dist_sqrd():
    for _ in range(runs):
        x_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        x_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x_1, y_1).dist_sqrd(Vector(x_2, y_2)) == round(
            (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2, Vector.ACCURACY
        )


def test_dot():
    for _ in range(runs):
        x_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        x_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x_1, y_1).dot(Vector(x_2, y_2)) == round(
            x_1 * x_2 + y_1 * y_2, Vector.ACCURACY
        )


def test_lerp():
    for _ in range(runs):
        x_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_1 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        x_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y_2 = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        i_range = round(random.random(), Vector.ACCURACY)

        assert Vector(x_1, y_1).lerp(Vector(x_2, y_2), i_range) == Vector(
            x_1 + i_range * (x_2 - x_1), y_1 + i_range * (y_2 - y_1)
        )


def test_length():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x, y).length() == round(
            math.sqrt(x**2 + y**2), Vector.ACCURACY
        )


def test_length_sqrd():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(), Vector.ACCURACY
        )

        assert Vector(x, y).length_sqrd() == round(x**2 + y**2, Vector.ACCURACY)


def test_normalise():
    for _ in range(runs):
        while True:
            x = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )
            y = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )

            if x != 0.0 and y != 0.0:
                break

        assert math.isclose(
            Vector(x, y).normalise().length(), 1.0, rel_tol=10.0**-Vector.ACCURACY
        )


def test_perp():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(),
            Vector.ACCURACY,
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(),
            Vector.ACCURACY,
        )

        assert Vector(x, y).perp() == Vector(-y, x)


def test_rotate():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(),
            Vector.ACCURACY,
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(),
            Vector.ACCURACY,
        )
        angle = round(
            random.randint(-angle_range, angle_range) + random.random(),
            Vector.ACCURACY,
        )

        assert Vector(x, y).rotate(angle).angle() == (Vector(x, y).angle() + angle) or (
            Vector(x, y).angle() - angle
        )


def test_scale():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(),
            Vector.ACCURACY,
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(),
            Vector.ACCURACY,
        )
        length = round(
            random.randint(-upper_range, upper_range) + random.random(),
            Vector.ACCURACY,
        )

        assert Vector(x, y).scale(length) == Vector(
            x * length / Vector(x, y).length(), y * length / Vector(x, y).length()
        )


def test_snap():
    for _ in range(runs):
        x = round(
            random.randint(-upper_range, upper_range) + random.random(),
            Vector.ACCURACY,
        )
        y = round(
            random.randint(-upper_range, upper_range) + random.random(),
            Vector.ACCURACY,
        )

        while True:
            length = round(
                random.randint(-upper_range, upper_range) + random.random(),
                Vector.ACCURACY,
            )

            if length != 0:
                break

        assert Vector(x, y).snap(length) == Vector(
            round(x / length) * length, round(y / length) * length
        )
