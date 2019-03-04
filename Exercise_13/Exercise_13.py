
import random


class RandMemory():

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._history = []

    @property
    def get(self):
        number = random.randint(self.start, self.end)
        self._history.append(number)
        return number

    def history(self):
        return self._history


if __name__ == '__main__':
    r = RandMemory(1, 100)  # produces integers between 1 and 100
    print(r.get)          # returns a number
    print(r.get)          # returns a number
    print(r.get)          # returns a number
    print(r.history())    # returns a list of numbers previously generated
