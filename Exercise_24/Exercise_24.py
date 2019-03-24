class Foo(object):

    _instances = []

    def __new__(cls, x):

        if x in cls._instances:
            pass
        else:
            cls._instances.append(x)
            return super(Foo, cls).__new__(cls)

    def __init__(self, x):
        self.x = x


class Uniquish():
    _instances = []

    def __new__(cls, x):

        if x in cls._instances:
            pass
        else:
            cls._instances.append(x)
            return super(Uniquish, cls).__new__(cls)

    def __init__(self, x):
        self.x = x


class Bar(Uniquish):
    def __init__(self, x):
        self.x = x


f1 = Foo(10)
f2 = Foo(10)
f3 = Foo(10)

s = {f1, f2, f3}

for i in s:
    print(i)

b1 = Bar(10)
b2 = Bar(10)
b3 = Bar(10)

r = {b1, b2, b3}
for i in r:
    print(r)
