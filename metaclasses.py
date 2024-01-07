def sum(self):
    return self.max + self.min


P = type("Point", (), {"max": 100, "min": 5, "sum": sum})
a = P()
print(a.sum())


class Meta(type):
    def __init__(cls, name, base, attrs):
        cls.max = 10
        cls.min = 0


class Point(metaclass=Meta):
    def get_coords(self):
        return (0, 0)


b = Point()
print(b.min)
