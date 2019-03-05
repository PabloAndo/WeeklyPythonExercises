
def mygetter(*args):

    def inner(s):
        # for each element i in args, get s[i]
        # return a tuple of the results
        if len(args) == 1:
            return s[args[0]]
        else:
            return tuple(s[i] for i in args)
    return inner

    def getter(elements):

        if len(args) == 1:
            if elements is list:
                for element in elements:
                    print('hola')

        else:
            pass

    return getter


g1 = mygetter(-1)
g1([10, 20, 30])  # returns 30

g2 = mygetter(0, -1)
g2([10, 20, 30])  # returns (10, 30)

g3 = mygetter('b')
d = {'a': 1, 'b': 2, 'c': 3}
g3(d)             # returns 2

d = {'a': 5, 'b': 3, 'c': 7, 'd': 4, 'e': 6}
print(d.items())
