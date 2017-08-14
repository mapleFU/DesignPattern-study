"""
装饰者模式:我想做一些别的事情
"""


def five():
    return 5


def add_five(func):
    def fun():
        return func() + 5
    return fun


@add_five
def deco_zero():
    return 0


def test_one():
    assert deco_zero() == five()

if __name__ == '__main__':
    test_one()