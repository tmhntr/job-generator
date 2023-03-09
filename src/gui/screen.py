from abc import ABC, abstractmethod


class Screen(ABC):
    screen_name: str
    _next = None
    layout: list[list] = [[]]


    @abstractmethod
    def update(self, event, values, window):
        pass


