import random

class Cell(object):
    def __init__(self, state=None):
        self._state = state if state else random.randint(0, 1)
        self._next_state = None
        self._i = None
        self._j = None
