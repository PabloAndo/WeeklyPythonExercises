class ThresholdEqual(int):

    def __init__(self, x):
        self.x = x
        self.threshold = 2

    def __eq__(self, other):
        if abs(self.x - other.x) <= self.threshold:
            return True
        else:
            return False
