# system imports --------------------------------------------------------------------- #
import math
import random
import sys

sys.path.append(".")

# local imports ---------------------------------------------------------------------- #
from drex import Vector


def test_init():
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)

    assert Vector(x, y).x == x and Vector(x, y).y == y


def test_call():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)

    vector = Vector(x_1, y_1)
    vector(x_2, y_2)

    assert vector.x == x_2 and vector.y == y_2


def test_eq():
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)

    assert Vector(x, y) == Vector(x, y)


def test_ne():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)

    assert Vector(x_1, y_1) != Vector(-x_1, -y_1)
    assert Vector(x_1, y_1) != Vector(-x_1, y_1)
    assert Vector(x_1, y_1) != Vector(x_1, -y_1)


def test_abs():
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)

    assert abs(Vector(-x, -y)) == Vector(abs(x), abs(y))
    assert abs(Vector(-x, y)) == Vector(abs(x), abs(y))
    assert abs(Vector(x, -y)) == Vector(abs(x), abs(y))


def test_round():
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)
    x_r = round(x)
    y_r = round(y)

    assert round(Vector(x, y)) == Vector(x_r, y_r)
    assert round(Vector(x_r, y)) == Vector(x_r, y_r)
    assert round(Vector(x, y_r)) == Vector(x_r, y_r)


def test_ceil():
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)
    x_c = math.ceil(x)
    y_c = math.ceil(y)

    assert math.ceil(Vector(x, y)) == Vector(x_c, y_c)
    assert math.ceil(Vector(x_c, y)) == Vector(x_c, y_c)
    assert math.ceil(Vector(x, y_c)) == Vector(x_c, y_c)


def test_floor():
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)
    x_f = math.floor(x)
    y_f = math.floor(y)

    assert math.floor(Vector(x, y)) == Vector(x_f, y_f)
    assert math.floor(Vector(x_f, y)) == Vector(x_f, y_f)
    assert math.floor(Vector(x, y_f)) == Vector(x_f, y_f)


def test_trunc():
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)
    x_t = math.trunc(x)
    y_t = math.trunc(y)

    assert math.trunc(Vector(x, y)) == Vector(x_t, y_t)
    assert math.trunc(Vector(x_t, y)) == Vector(x_t, y_t)
    assert math.trunc(Vector(x, y_t)) == Vector(x_t, y_t)


def test_neg():
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)

    assert -Vector(x, y) == Vector(-x, -y)


def test_add():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-1, 10000)
    vector = Vector(x_2, y_2)

    assert Vector(x_1, y_1) + float == Vector(x_1 + float, y_1 + float)
    assert Vector(x_1, y_1) + int == Vector(x_1 + int, y_1 + int)
    assert Vector(x_1, y_1) + vector == Vector(x_1 + x_2, y_1 + y_2)


def test_sub():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-1, 10000)
    vector = Vector(x_2, y_2)

    assert Vector(x_1, y_1) - float == Vector(x_1 - float, y_1 - float)
    assert Vector(x_1, y_1) - int == Vector(x_1 - int, y_1 - int)
    assert Vector(x_1, y_1) - vector == Vector(x_1 - x_2, y_1 - y_2)


def test_mul():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-1, 10000)
    vector = Vector(x_2, y_2)

    assert Vector(x_1, y_1) * float == Vector(x_1 * float, y_1 * float)
    assert Vector(x_1, y_1) * int == Vector(x_1 * int, y_1 * int)
    assert Vector(x_1, y_1) * vector == Vector(x_1 * x_2, y_1 * y_2)


def test_truediv():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-10, 10)
    vector = Vector(x_2, y_2)

    assert Vector(x_1, y_1) / float == Vector(x_1 / float, y_1 / float)
    assert Vector(x_1, y_1) / int == Vector(x_1 / int, y_1 / int)
    assert Vector(x_1, y_1) / vector == Vector(x_1 / x_2, y_1 / y_2)


def test_floordiv():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-10, 10)
    vector = Vector(x_2, y_2)

    assert Vector(x_1, y_1) // float == Vector(x_1 // float, y_1 // float)
    assert Vector(x_1, y_1) // int == Vector(x_1 // int, y_1 // int)
    assert Vector(x_1, y_1) // vector == Vector(x_1 // x_2, y_1 // y_2)


def test_pow():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-10, 10)
    vector = Vector(x_2, y_2)

    assert Vector(x_1, y_1)**float == Vector(x_1**float, y_1**float)
    assert Vector(x_1, y_1)**int == Vector(x_1**int, y_1**int)
    assert Vector(x_1, y_1)**vector == Vector(x_1**x_2, y_1**y_2)


def test_mod():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-10, 10)
    vector = Vector(x_2, y_2)

    assert Vector(x_1, y_1) % float == Vector(x_1 % float, y_1 % float)
    assert Vector(x_1, y_1) % int == Vector(x_1 % int, y_1 % int)
    assert Vector(x_1, y_1) % vector == Vector(x_1 % x_2, y_1 % y_2)


def test_divmod():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-10, 10)
    vector = Vector(x_2, y_2)

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
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-1, 10000)
    vector = Vector(x_2, y_2)

    assert float + Vector(x_1, y_1) == Vector(float + x_1, float + y_1)
    assert int + Vector(x_1, y_1) == Vector(int + x_1, int + y_1)
    assert vector + Vector(x_1, y_1) == Vector(x_2 + x_1, y_2 + y_1)


def test_rsub():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-1, 10000)
    vector = Vector(x_2, y_2)

    assert float - Vector(x_1, y_1) == Vector(float - x_1, float - y_1)
    assert int - Vector(x_1, y_1) == Vector(int - x_1, int - y_1)
    assert vector - Vector(x_1, y_1) == Vector(x_2 - x_1, y_2 - y_1)


def test_rmul():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-1, 10000)
    vector = Vector(x_2, y_2)

    assert float * Vector(x_1, y_1) == Vector(float * x_1, float * y_1)
    assert int * Vector(x_1, y_1) == Vector(int * x_1, int * y_1)
    assert vector * Vector(x_1, y_1) == Vector(x_2 * x_1, y_2 * y_1)


def test_rtruediv():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-10, 10)
    vector = Vector(x_2, y_2)

    assert float / Vector(x_1, y_1) == Vector(float / x_1, float / y_1)
    assert int / Vector(x_1, y_1) == Vector(int / x_1, int / y_1)
    assert vector / Vector(x_1, y_1) == Vector(x_2 / x_1, y_2 / y_1)


def test_rfloordiv():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-10, 10)
    vector = Vector(x_2, y_2)

    assert float // Vector(x_1, y_1) == Vector(float // x_1, float // y_1)
    assert int // Vector(x_1, y_1) == Vector(int // x_1, int // y_1)
    assert vector // Vector(x_1, y_1) == Vector(x_2 // x_1, y_2 // y_1)


def test_rpow():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-10, 10)
    vector = Vector(x_2, y_2)

    print(float)

    assert float**Vector(x_1, y_1) == Vector(float**x_1, float**y_1)
    assert int**Vector(x_1, y_1) == Vector(int**x_1, int**y_1)
    assert vector**Vector(x_1, y_1) == Vector(x_2**x_1, y_2**y_1)


def test_rmod():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-10, 10)
    vector = Vector(x_2, y_2)

    assert float % Vector(x_1, y_1) == Vector(float % x_1, float % y_1)
    assert int % Vector(x_1, y_1) == Vector(int % x_1, int % y_1)
    assert vector % Vector(x_1, y_1) == Vector(x_2 % x_1, y_2 % y_1)


def test_rdivmod():
    x_1 = round(random.random() * random.randint(-10, 10), 10)
    x_2 = round(random.random() * random.randint(-10, 10), 10)
    y_1 = round(random.random() * random.randint(-10, 10), 10)
    y_2 = round(random.random() * random.randint(-10, 10), 10)
    float = round(random.random() * random.randint(-10, 10), 10)
    int = random.randint(-10, 10)
    vector = Vector(x_2, y_2)

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
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)

    assert str(Vector(x, y)) == f"Vector({x}, {y})"

def test_repr():
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)

    assert repr(Vector(x, y)) == f"Vector({x}, {y})"

def test_iter():
    x = round(random.random() * random.randint(-10, 10), 10)
    y = round(random.random() * random.randint(-10, 10), 10)

    assert list(Vector(x, y)) == [x, y]
