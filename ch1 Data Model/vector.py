from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # If we did not implement __repr__, vector instances would be shown in the console like <Vector object at 0x10e100070>.
    # when no custom __str__ is available, Python will call __repr__ as a fallback.
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    # operator: +
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # operator: *
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(3, 4)
v2 = Vector(2, 1)
print v1 + v2
print v1 * 3
print abs(v1)


# Python offers a rich selection of numeric types, from the built-ins to decimal.Decimal and fractions.Fraction,

