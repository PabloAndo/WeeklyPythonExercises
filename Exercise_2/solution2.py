def myrange2(start, stop=None, step=1):

    result = []
    while True:

        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1
        if start > stop - 1:
            break

        result.append(start)
        start += step

    return result


def myrange3(start, stop=None, step=1):

    while True:

        if stop is None:
            stop = start
            start = 0
        if step is None:
            step = 1
        if start > stop - 1:
            break

        yield start
        start += step
