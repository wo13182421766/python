def my_abs(x, y):
    if not isinstance((x, y), (int, float)):
        raise TypeError('error val type')
    if x >= y:
        return x / y
    else:
        return x / 0


def test_main():
    print(__name__)

