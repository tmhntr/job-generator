from abc import ABC, abstractmethod


class Screen(ABC):
    _next = None
    layout: list[list] = [[]]

    def __init__(self, next=None):
        self.set_next(next)

    @abstractmethod
    def update(self, event, values, window):
        pass

    def set_next(self, next):
        if next is None:
            print("next is None")
        self._next = next

    def next(self):
        if self._next is not None:
            self._next()

