# system imports --------------------------------------------------------------------- #
import math
import random
import sys

sys.path.append(".")

# local imports ---------------------------------------------------------------------- #
from drex import Vector


runs = 1000
lower_range = -10
upper_range = 10
decimal = 10


def test_init():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)

        assert Vector(x, y).x == x and Vector(x, y).y == y


def test_call():
    for _ in range(runs):
        x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)

        vector = Vector(x_1, y_1)
        vector(x_2, y_2)

        assert vector.x == x_2 and vector.y == y_2


def test_eq():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)

        assert Vector(x, y) == Vector(x, y)


def test_ne():
    for _ in range(runs):
        while True:
            x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)

            if x_1 != 0.0 and y_1 != 0.0:
                break

        assert Vector(x_1, y_1) != Vector(-x_1, -y_1)
        assert Vector(x_1, y_1) != Vector(-x_1, y_1)
        assert Vector(x_1, y_1) != Vector(x_1, -y_1)


def test_abs():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)

        assert abs(Vector(-x, -y)) == Vector(abs(x), abs(y))
        assert abs(Vector(-x, y)) == Vector(abs(x), abs(y))
        assert abs(Vector(x, -y)) == Vector(abs(x), abs(y))


def test_round():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_r = round(x)
        y_r = round(y)

        assert round(Vector(x, y)) == Vector(x_r, y_r)
        assert round(Vector(x_r, y)) == Vector(x_r, y_r)
        assert round(Vector(x, y_r)) == Vector(x_r, y_r)


def test_ceil():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_c = math.ceil(x)
        y_c = math.ceil(y)

        assert math.ceil(Vector(x, y)) == Vector(x_c, y_c)
        assert math.ceil(Vector(x_c, y)) == Vector(x_c, y_c)
        assert math.ceil(Vector(x, y_c)) == Vector(x_c, y_c)


def test_floor():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_f = math.floor(x)
        y_f = math.floor(y)

        assert math.floor(Vector(x, y)) == Vector(x_f, y_f)
        assert math.floor(Vector(x_f, y)) == Vector(x_f, y_f)
        assert math.floor(Vector(x, y_f)) == Vector(x_f, y_f)


def test_trunc():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_t = math.trunc(x)
        y_t = math.trunc(y)

        assert math.trunc(Vector(x, y)) == Vector(x_t, y_t)
        assert math.trunc(Vector(x_t, y)) == Vector(x_t, y_t)
        assert math.trunc(Vector(x, y_t)) == Vector(x_t, y_t)


def test_neg():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)

        assert -Vector(x, y) == Vector(-x, -y)


def test_add():
    for _ in range(runs):
        x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        float = round(random.random() * random.randint(lower_range, upper_range), decimal)
        int = random.randint(lower_range, upper_range)
        vector = Vector(x_2, y_2)

        assert Vector(x_1, y_1) + float == Vector(x_1 + float, y_1 + float)
        assert Vector(x_1, y_1) + int == Vector(x_1 + int, y_1 + int)
        assert Vector(x_1, y_1) + vector == Vector(x_1 + x_2, y_1 + y_2)


def test_sub():
    for _ in range(runs):
        x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        float = round(random.random() * random.randint(lower_range, upper_range), decimal)
        int = random.randint(lower_range, upper_range)
        vector = Vector(x_2, y_2)

        assert Vector(x_1, y_1) - float == Vector(x_1 - float, y_1 - float)
        assert Vector(x_1, y_1) - int == Vector(x_1 - int, y_1 - int)
        assert Vector(x_1, y_1) - vector == Vector(x_1 - x_2, y_1 - y_2)


def test_mul():
    for _ in range(runs):
        x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        float = round(random.random() * random.randint(lower_range, upper_range), decimal)
        int = random.randint(lower_range, upper_range)
        vector = Vector(x_2, y_2)

        assert Vector(x_1, y_1) * float == Vector(x_1 * float, y_1 * float)
        assert Vector(x_1, y_1) * int == Vector(x_1 * int, y_1 * int)
        assert Vector(x_1, y_1) * vector == Vector(x_1 * x_2, y_1 * y_2)


def test_truediv():
    for _ in range(runs):
        while True:
            x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            float = round(random.random() * random.randint(lower_range, upper_range), decimal)
            int = random.randint(lower_range, upper_range)
            vector = Vector(x_2, y_2)

            if (
                x_1 != 0.0
                and x_2 != 0.0
                and y_1 != 0.0
                and y_2 != 0.0
                and float != 0.0
                and int != 0
            ):
                break

        assert Vector(x_1, y_1) / float == Vector(x_1 / float, y_1 / float)
        assert Vector(x_1, y_1) / int == Vector(x_1 / int, y_1 / int)
        assert Vector(x_1, y_1) / vector == Vector(x_1 / x_2, y_1 / y_2)


def test_floordiv():
    for _ in range(runs):
        while True:
            x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            float = round(random.random() * random.randint(lower_range, upper_range), decimal)
            int = random.randint(lower_range, upper_range)
            vector = Vector(x_2, y_2)

            if (
                x_1 != 0.0
                and x_2 != 0.0
                and y_1 != 0.0
                and y_2 != 0.0
                and float != 0.0
                and int != 0
            ):
                break

        assert Vector(x_1, y_1) // float == Vector(x_1 // float, y_1 // float)
        assert Vector(x_1, y_1) // int == Vector(x_1 // int, y_1 // int)
        assert Vector(x_1, y_1) // vector == Vector(x_1 // x_2, y_1 // y_2)


def test_pow():
    for _ in range(runs):
        x_1 = round(random.random() * random.randint(0, 10), 10)
        x_2 = round(random.random() * random.randint(0, 10), 10)
        y_1 = round(random.random() * random.randint(0, 10), 10)
        y_2 = round(random.random() * random.randint(0, 10), 10)
        float = round(random.random() * random.randint(0, 10), 10)
        int = random.randint(max(0, lower_range), upper_range)
        vector = Vector(x_2, y_2)

        assert Vector(x_1, y_1) ** float == Vector(x_1**float, y_1**float)
        assert Vector(x_1, y_1) ** int == Vector(x_1**int, y_1**int)
        assert Vector(x_1, y_1) ** vector == Vector(x_1**x_2, y_1**y_2)


def test_mod():
    for _ in range(runs):
        while True:
            x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            float = round(random.random() * random.randint(lower_range, upper_range), decimal)
            int = random.randint(lower_range, upper_range)
            vector = Vector(x_2, y_2)

            if (
                x_1 != 0.0
                and x_2 != 0.0
                and y_1 != 0.0
                and y_2 != 0.0
                and float != 0.0
                and int != 0
            ):
                break

        assert Vector(x_1, y_1) % float == Vector(x_1 % float, y_1 % float)
        assert Vector(x_1, y_1) % int == Vector(x_1 % int, y_1 % int)
        assert Vector(x_1, y_1) % vector == Vector(x_1 % x_2, y_1 % y_2)


def test_divmod():
    for _ in range(runs):
        while True:
            x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            float = round(random.random() * random.randint(lower_range, upper_range), decimal)
            int = random.randint(lower_range, upper_range)
            vector = Vector(x_2, y_2)

            if (
                x_1 != 0.0
                and x_2 != 0.0
                and y_1 != 0.0
                and y_2 != 0.0
                and float != 0.0
                and int != 0
            ):
                break

        assert divmod(Vector(x_1, y_1), float) == (
            Vector(divmod(x_1, float)[0], divmod(y_1, float)[0]),
            Vector(divmod(x_1, float)[1], divmod(y_1, float)[1]),
        )
        assert divmod(Vector(x_1, y_1), int) == (
            Vector(divmod(x_1, int)[0], divmod(y_1, int)[0]),
            Vector(divmod(x_1, int)[1], divmod(y_1, int)[1]),
        )
        assert divmod(Vector(x_1, y_1), vector) == (
            Vector(divmod(x_1, x_2)[0], divmod(y_1, y_2)[0]),
            Vector(divmod(x_1, x_2)[1], divmod(y_1, y_2)[1]),
        )


def test_radd():
    for _ in range(runs):
        x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        float = round(random.random() * random.randint(lower_range, upper_range), decimal)
        int = random.randint(lower_range, upper_range)
        vector = Vector(x_2, y_2)

        assert float + Vector(x_1, y_1) == Vector(float + x_1, float + y_1)
        assert int + Vector(x_1, y_1) == Vector(int + x_1, int + y_1)
        assert vector + Vector(x_1, y_1) == Vector(x_2 + x_1, y_2 + y_1)


def test_rsub():
    for _ in range(runs):
        x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        float = round(random.random() * random.randint(lower_range, upper_range), decimal)
        int = random.randint(lower_range, upper_range)
        vector = Vector(x_2, y_2)

        assert float - Vector(x_1, y_1) == Vector(float - x_1, float - y_1)
        assert int - Vector(x_1, y_1) == Vector(int - x_1, int - y_1)
        assert vector - Vector(x_1, y_1) == Vector(x_2 - x_1, y_2 - y_1)


def test_rmul():
    for _ in range(runs):
        x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
        float = round(random.random() * random.randint(lower_range, upper_range), decimal)
        int = random.randint(lower_range, upper_range)
        vector = Vector(x_2, y_2)

        assert float * Vector(x_1, y_1) == Vector(float * x_1, float * y_1)
        assert int * Vector(x_1, y_1) == Vector(int * x_1, int * y_1)
        assert vector * Vector(x_1, y_1) == Vector(x_2 * x_1, y_2 * y_1)


def test_rtruediv():
    for _ in range(runs):
        while True:
            x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            float = round(random.random() * random.randint(lower_range, upper_range), decimal)
            int = random.randint(lower_range, upper_range)
            vector = Vector(x_2, y_2)

            if (
                x_1 != 0.0
                and x_2 != 0.0
                and y_1 != 0.0
                and y_2 != 0.0
                and float != 0.0
                and int != 0
            ):
                break

        assert float / Vector(x_1, y_1) == Vector(float / x_1, float / y_1)
        assert int / Vector(x_1, y_1) == Vector(int / x_1, int / y_1)
        assert vector / Vector(x_1, y_1) == Vector(x_2 / x_1, y_2 / y_1)


def test_rfloordiv():
    for _ in range(runs):
        while True:
            x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            float = round(random.random() * random.randint(lower_range, upper_range), decimal)
            int = random.randint(lower_range, upper_range)
            vector = Vector(x_2, y_2)

            if (
                x_1 != 0.0
                and x_2 != 0.0
                and y_1 != 0.0
                and y_2 != 0.0
                and float != 0.0
                and int != 0
            ):
                break

        assert float // Vector(x_1, y_1) == Vector(float // x_1, float // y_1)
        assert int // Vector(x_1, y_1) == Vector(int // x_1, int // y_1)
        assert vector // Vector(x_1, y_1) == Vector(x_2 // x_1, y_2 // y_1)


def test_rpow():
    for _ in range(runs):
        x_1 = round(random.random() * random.randint(0, 10), 10)
        x_2 = round(random.random() * random.randint(0, 10), 10)
        y_1 = round(random.random() * random.randint(0, 10), 10)
        y_2 = round(random.random() * random.randint(0, 10), 10)
        float = round(random.random() * random.randint(0, 10), 10)
        int = random.randint(max(0, lower_range), upper_range)
        vector = Vector(x_2, y_2)

        assert float ** Vector(x_1, y_1) == Vector(float**x_1, float**y_1)
        assert int ** Vector(x_1, y_1) == Vector(int**x_1, int**y_1)
        assert vector ** Vector(x_1, y_1) == Vector(x_2**x_1, y_2**y_1)


def test_rmod():
    for _ in range(runs):
        while True:
            x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            float = round(random.random() * random.randint(lower_range, upper_range), decimal)
            int = random.randint(lower_range, upper_range)
            vector = Vector(x_2, y_2)

            if (
                x_1 != 0.0
                and x_2 != 0.0
                and y_1 != 0.0
                and y_2 != 0.0
                and float != 0.0
                and int != 0
            ):
                break

        assert float % Vector(x_1, y_1) == Vector(float % x_1, float % y_1)
        assert int % Vector(x_1, y_1) == Vector(int % x_1, int % y_1)
        assert vector % Vector(x_1, y_1) == Vector(x_2 % x_1, y_2 % y_1)


def test_rdivmod():
    for _ in range(runs):
        while True:
            x_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            x_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_1 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            y_2 = round(random.random() * random.randint(lower_range, upper_range), decimal)
            float = round(random.random() * random.randint(lower_range, upper_range), decimal)
            int = random.randint(lower_range, upper_range)
            vector = Vector(x_2, y_2)

            if (
                x_1 != 0.0
                and x_2 != 0.0
                and y_1 != 0.0
                and y_2 != 0.0
                and float != 0.0
                and int != 0
            ):
                break

        assert divmod(Vector(x_1, y_1), float) == (
            Vector(divmod(x_1, float)[0], divmod(y_1, float)[0]),
            Vector(divmod(x_1, float)[1], divmod(y_1, float)[1]),
        )
        assert divmod(Vector(x_1, y_1), int) == (
            Vector(divmod(x_1, int)[0], divmod(y_1, int)[0]),
            Vector(divmod(x_1, int)[1], divmod(y_1, int)[1]),
        )
        assert divmod(Vector(x_1, y_1), vector) == (
            Vector(divmod(x_1, x_2)[0], divmod(y_1, y_2)[0]),
            Vector(divmod(x_1, x_2)[1], divmod(y_1, y_2)[1]),
        )


def test_str():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)

        assert str(Vector(x, y)) == f"Vector({x}, {y})"


def test_repr():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)

        assert repr(Vector(x, y)) == f"Vector({x}, {y})"


def test_iter():
    for _ in range(runs):
        x = round(random.random() * random.randint(lower_range, upper_range), decimal)
        y = round(random.random() * random.randint(lower_range, upper_range), decimal)

        assert list(Vector(x, y)) == [x, y]
