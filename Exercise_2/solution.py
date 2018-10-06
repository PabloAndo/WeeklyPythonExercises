# WPE Exercise 2
import sys


def myrange2(*args):

    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1

    elif len(args) == 2:
        start, stop = args
        if stop is None:
            stop = start
            start = 0
        step = 1

    elif len(args) == 3:
        start, stop, step = args
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1

    elif len(args) == 0 or len(args) > 3:
        print('[ERROR] Invalid arguments')
        sys.exit(0)

    result = []

    while True:

        if start > stop - 1:
            break

        result.append(start)
        start += step
    return result


def myrange3(*args):

    if len(args) == 1:
        start = 0
        stop = args[0]
        step = 1
    elif len(args) == 2:
        start, stop = args
        if stop is None:
            stop = start
            start = 0
    elif len(args) == 3:
        start, stop, step = args
        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1

    elif len(args) == 0 or len(args) > 3:
        print('[ERROR]: Invalid arguments')
        sys.exit(0)

    while True:

        if start > stop - 1:
            break

        yield start

        start += step


args = [10, None, None]

if __name__ == '__main__':

    # print('----pythonRange----')
    # print(range(*args))
    # for x in range(*args):
    #     print(x)

    print('----myrange2----')
    print(myrange2(*args))

    print('----myrange3----')
    print(myrange3(*args))
    for x in myrange3(*args):
        print(x)
